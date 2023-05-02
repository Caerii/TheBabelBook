from flask import Flask
from flask import render_template
from flask import request,session, redirect, url_for, escape,send_from_directory,make_response 
from flask_session import Session
from datetime import timedelta
from user import user
import mysecrets
import time
import openai
from treeNode import tree

#create Flask app instance
app = Flask(__name__,static_url_path='')


#Configure serverside sessions 
app.config['SECRET_KEY'] = '56hdtryhRTg'
app.config['SESSION_PERMANENT'] = True
app.config['SESSION_TYPE'] = 'filesystem'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(hours=24)
sess = Session()
sess.init_app(app)

#Basic root route - show the word 'homepage'
@app.route('/')  #route name
def home(): #view function
    return render_template('main.html', title='Home')
    #return 'homepage'

@app.context_processor
def inject_user():
    return dict(me=session.get('user'))

@app.context_processor
def inject_url_for():
    return dict(url_for=url_for)

@app.route('/confirm',methods=['GET','POST'])
def confirm():
    #product = request.form.get('product')
    product = session['product']
    ship = request.form.get('ship')
    return render_template('confirm.html',product=product,ship=ship)

#test setting a session:
@app.route('/set')
def set():
    session['key'] = 'value'
    return 'ok'

#test getting a session:
@app.route('/get')
def get():
    return session.get('key', 'not set')

@app.route('/main')
def main():
    if checkSession() == False: 
        return redirect('/login')
    if session['user']['role'] == 'admin':
        return render_template('main.html', title='Main menu') 
    else:
        return render_template('user_main.html', title='Main menu') 

@app.route('/users/manage',methods=['GET','POST'])
def manage_user():
    if checkSession() == False or session['user']['role'] != 'admin': 
        return redirect('/login')
    o = user()
    t = tree()
    t.getAll() # get all the nodes
    o.attachRelated('Book',t)

    action = request.args.get('action') 
    pkval = request.args.get('pkval')
    if action is not None and action == 'delete':
        o.deleteById(request.args.get('pkval'))
        return render_template('ok_dialog.html',msg= "Deleted.")
    if action is not None and action == 'insert':
        d = {}
        d['name'] = request.form.get('name')
        d['email'] = request.form.get('email')
        d['role'] = request.form.get('role')
        d['password'] = request.form.get('password')
        d['password2'] = request.form.get('password2')
        o.set(d)
        if o.verify_new():
            o.insert()
            return render_template('ok_dialog.html',msg= "User added.")
        else:
            return render_template('users/add.html',obj = o)
    if action is not None and action == 'update':
        o.getById(pkval)
        o.data[0]['name'] = request.form.get('name')
        o.data[0]['email'] = request.form.get('email')
        o.data[0]['role'] = request.form.get('role')
        o.data[0]['password'] = request.form.get('password')
        o.data[0]['password2'] = request.form.get('password2')
        if o.verify_update():
            o.update()
            return render_template('ok_dialog.html',msg= "User updated. <")
        else:
            return render_template('users/manage.html',obj = o)
       
        
    if pkval is None:
        o.getAll()
        return render_template('users/list.html',objs = o)
    if pkval == 'new':
        o.createBlank()
        return render_template('users/add.html',obj = o)
    else:
        o.getById(pkval)
        return render_template('users/manage.html',obj = o)

#view sessions
@app.route('/sessions')
def sessions():
    if checkSession() == False: 
        return redirect('/login')
    return render_template('sessions.html', title='Sessions')

#display form   
@app.route('/enterName')
def enterName():
    return render_template('nameForm.html')

#process form   
@app.route('/submitName',methods=['GET','POST'])
def submitName():
    username = request.form.get('myname')
    othername = request.form.get('othername')
    print(othername)
    print(username)
    #At this point we would INSERT the user's name to the mysql table
    return render_template('message.html',msg='name '+str(username)+' added!')

@app.route('/customqueries', methods=['GET','POST'])
def customqueries():
    t = tree()

    action = request.args.get('action')

    #if action is not None and action == 'howManyLayersDeep':
        #layersCount = t.export_treeNodePruned()
        #return render_template('customqueries.html', layersDeep = layersCount)
    
    if action is not None and action == 'numberOfNodes':
        nodeCount = t.howManyNodes()
        return render_template('customqueries.html', totalNodeCount = nodeCount)
    
    if action is not None and action == 'numberOfChildren':
        t.getAll()
        nodeID = t.data[0]['NodeID']
        childCount = t.howManyChildren(nodeID)
        return render_template('customqueries.html', totalChildCount = childCount)

    return render_template('customqueries.html')

@app.route('/editor', methods=['GET','POST'])
@app.route('/editor?<int:ParentNodeID>&<int:NodeID>')
def editor(ParentNodeID=0, NodeID=1):
    t = tree()
    print("Start ParentNodeID",ParentNodeID)
    print("Start NodeID",NodeID)
    

    # set ParentNodeID and nodeID based on URL arguments
    NodeID_new = request.args.get('nodeid')
    if NodeID_new is not None and NodeID_new != '':
        NodeID = int(NodeID_new)

    ParentNodeID_new = request.args.get('parentid')
    if ParentNodeID_new is not None and ParentNodeID_new != '':
        if ParentNodeID_new == 'None':
            ParentNodeID_new = 0
        print("Before int casting", ParentNodeID_new)
        ParentNodeID = int(ParentNodeID_new)

    childList = t.read_treenodeChildren(NodeID) # read all the children of the current node we are only on the root node
    print("line 183 childList",childList)

    action = request.args.get('action')

    # NodeID = (int)(request.args.get('nodeid')) # grab the nodeid from the url
    # print("line 199 nodeid",NodeID)

    if action is not None and action == 'addTreeNode':
        print("ADDING NEW TREE NODE!!!!!!!!!")
        NodeLabel = request.form.get('node_label')
        NodeData = request.form.get('node_data')
        # grab the parent args and use it to create the child
        NodeLevel = '1' # default value before we add a counter to the tree
        # tchild = tree() # must create new child node
        NodeIDNew = request.args.get('nodeid') # grab the nodeid from the url
        ParentNodeIDNew = request.args.get('parentid') # grab the parentid from the url
        # overwrite NodeID and ParentNodeID
        NodeID = NodeIDNew
        ParentNodeID = ParentNodeIDNew

        t.create_treeNode(NodeIDNew, NodeLabel, NodeData, NodeLevel) # fill child with data from form
        # time.sleep(2)
        # grab the data of the tchild
        # nodeidchild = tchild.data[0]['NodeID']
        # nodeidparent = tchild.data[0]['ParentNodeID']
        # print("add new child nodeidparent",nodeidparent)
        # print("add new child nodeidchild",nodeidchild)
        return redirect(url_for('editor', parentid=ParentNodeIDNew, nodeid=NodeIDNew))

    if action is not None and action == 'updateTreeNode':
        UpdateNodeID = request.form.get('node_to_update') #this is the nodeID of the node to update
        UpdateNodeLabel = request.form.get('node_label')
        UpdateNodeData = request.form.get('node_data')
        # if any of these fields are empty, we just want to keep the old data
        if UpdateNodeLabel == '' or UpdateNodeLabel is None:
            UpdateNodeLabel = t.getTreeNodeLabelByNodeID(UpdateNodeID)
        if UpdateNodeData == '' or UpdateNodeData is None:
            UpdateNodeData = t.getTreeNodeDataByNodeID(UpdateNodeID)

        NodeID = request.args.get('nodeid') # grab the nodeid from the url
        t.update_treeNode(UpdateNodeID, UpdateNodeLabel, UpdateNodeData)

        return redirect(url_for('editor', parentid=ParentNodeID, nodeid=NodeID))
        
    if action is not None and action == 'deleteTreeNode':
        DeleteNodeID = request.form.get('node_to_delete') #this is the nodeID of the node to delete
        print("DeleteNodeID",DeleteNodeID)
        # request arguments
        NodeID = request.args.get('nodeid') # grab the nodeid from the url
        ParentNodeID = request.args.get('parentid') # grab the parentid from the url
        print("NodeID from url DELETE",NodeID)
        print("ParentNodeID from url DELETE",ParentNodeID)
        error = t.delete_treeNode(DeleteNodeID)
        if error == -1:
            print("Error deleting node")
            return redirect(url_for('editor', parentid=ParentNodeID, nodeid=NodeID))
        return redirect(url_for('editor', parentid=ParentNodeID, nodeid=NodeID))

    if action is not None and action == 'cascadeDelete':
        DeleteNodeID = request.form.get('node_to_cascade')
        NodeID = request.args.get('nodeid') # grab the nodeid from the url
        ParentNodeID = request.args.get('parentid') # grab the parentid from the url
        t.cascadeDelete(DeleteNodeID)
        return redirect(url_for('editor', parentid=ParentNodeID, nodeid=NodeID))

    if action is not None and action == 'startNewBook':
        t.deleteAll()
        return redirect(url_for('editor', parentid=0, nodeid=1))

    if action is not None and action == 'exportTreeNode':
        currentNodeID = t.data[0]['NodeID'] #grab the nodeid
        t.export_treeNode(1) # export the tree to a string
        stringList = t.exportString # grab the string
        return render_template('export.html', tree=t, stringList=stringList)

    if action is not None and action == 'generateChapters':
        user_prompt = request.form.get('prompt')
        openAIKey = mysecrets.OPENAI_API_KEY # Set the OpenAI API key
        NodeIDNew = request.args.get('nodeid') # grab the nodeid from the url
        
        t.export_treeNode(1) # export the tree to a string
        stringList = t.exportString # grab the string
        promptSoFar = t.generatePromptFromRootToCurrentNodesChildren(NodeIDNew, stringList) # generate the prompt
        # split the prompt into a list by the new line character
        promptSoFarList = promptSoFar.split('\n')
        # take the last line of the prompt
        lastLine = promptSoFarList[-1]
        # split by space
        lastLineList = lastLine.split(' ')
        lastNumber = lastLineList[0]

        # pass the promptSoFar generateChapters
        chapterList = t.generateChapters(user_prompt, openAIKey, promptSoFar, howManyChapters=5) # generate the chapters
        t.generateNodesBasedOnChapters(chapterList, NodeIDNew) # add to the current tree

        return redirect(url_for('editor', parentid=ParentNodeID, nodeid=NodeID))

    if action is not None and action == 'generateNodeWords':
        user_prompt = request.form.get('chapter_words') # grab the user input
        openAIKey = mysecrets.OPENAI_API_KEY # Set the OpenAI API key
        CurrentNodeID = request.args.get('nodeid') # grab the nodeid from the url

        t.export_treeNode(1) # export the tree to a string
        stringList = t.exportString # grab the string
        promptSoFar = t.generatePromptFromRootToCurrentNodesChildren(CurrentNodeID, stringList) # generate the prompt

        text_output = t.generateNodeWriting(user_prompt, openAIKey, promptSoFar, CurrentNodeID) # generate the writing in a node
        print(text_output)
        t.update_treeNode(CurrentNodeID, t.getTreeNodeLabelByNodeID(CurrentNodeID), t.getTreeNodeDataByNodeID(CurrentNodeID) + text_output) # update the node with the new text
        return redirect(url_for('editor', parentid=ParentNodeID, nodeid=NodeID))



    if (request.args.get('nodeid')) is not None and request.args.get('nodeid') != '': # this will update the nodeid if we are on a child node
        if(int(request.args.get('nodeid')) >= 1):
            # ParentNodeID = (int)(request.args.get('parentid')) # grab the parentid from the url
            NodeID = (int)(request.args.get('nodeid')) # grab the nodeid from the url
            
            print("ParentNodeID From Args line 235",ParentNodeID)
            print("NodeID From Args line 236",NodeID)
            # print("tree.data",t.data[0])
            t.read_treenodeChildren(NodeID)
            return render_template('editor.html', tree=t, parentid=ParentNodeID, nodeid=NodeID)

    # grab the nodeid from the url
    NodeID = request.args.get('nodeid')
    ParentNodeID = request.args.get('parentid')
    print("NodeID FINAL REFRESH",NodeID)
    print("ParentNodeID FINAL REFRESH",ParentNodeID)
    return render_template('editor.html', tree=t, parentid=ParentNodeID, nodeid=NodeID)

# user login/logout routes
@app.route('/login',methods = ['GET','POST'])
def login():
    '''
    -check login
    -set session
    -redirect to menu
    -check session on login pages
    '''
    if request.form.get('email') is not None and request.form.get('password') is not None:
        u = user()
        u.getAll()
        print(u.data)
        if u.tryLogin(request.form.get('email'),request.form.get('password')):
            print('login ok')
            session['user'] = u.data[0]
            session['active'] = time.time()
            
            return redirect('main')
        else:
            print('login failed')
            return render_template('login.html', title='Login', msg='Incorrect username or password.')
    else:
        if 'msg' not in session.keys() or session['msg'] is None:
            m = 'Type your email and password to continue.'
        else:
            m = session['msg']
            session['msg'] = None
        return render_template('login.html', title='Login', msg=m)
@app.route('/logout',methods = ['GET','POST'])
def logout():
    if session.get('user') is not None:
        del session['user']
        del session['active']
    return render_template('login.html', title='Login', msg='You have logged out.')


# endpoint route for static files
@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)
def checkSession():
    if 'active' in session.keys():
        timeSinceAct = time.time() - session['active']
        print(timeSinceAct)
        if timeSinceAct > 500:
            session['msg'] = 'Your session has timed out.'
            return False
        else:
            session['active'] = time.time()
            return True
    else:
        return False      
  
if __name__ == '__main__':
   app.run(host='127.0.0.1',debug=True)   




