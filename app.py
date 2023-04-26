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
    return render_template('editor.html', title='Home')
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
    # if checkSession() == False or session['user']['role'] != 'admin': 
    #     return redirect('/login')
    o = user()
    # l = location()
    # l.getAll()
    # o.attachRelated('location',l)


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

@app.route('/generateBook', methods=['GET','POST'])
def generateBook():
    user_prompt = request.form.get('prompt')
    prompt = f"Please generate a list of chapter subheadings for the book with a book with the description as <{user_prompt}> in a numbered, bulleted list.\n 1. example_subtitle1 \n 2. example_subtitle2 \n New chapter based on description:"
    # Call the OpenAI API with the prompt to generate a list of book subtitles
    # Format the list as "Please generate a list of chapter subheadings for the book with the {user_prompt} in a numbered, bulleted list"
    openai.api_key = mysecrets.OPENAI_API_KEY # Set the OpenAI API key
    generated_list = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=160,
        n=1,
        stop=None,
        temperature=0.9,
    )
    text_output = generated_list.choices[0].text
    # Format the output so that it replaces periods with new line characters
    # text_output = text_output.replace(" ", "\n")
    # Create a list, each element of the list is composed of the integer, a period, space, and all of the words until the next number
    for i in range (len(text_output)):
        # text_output = str(i+1)
        text_output = text_output.replace(str(i+1)+".", str(i+1) + " -")

    # Return the generated list of subtitles
    return render_template('generated_book.html', text_output=text_output)

@app.route('/editor', methods=['GET','POST'])
def editor(ParentNodeID=None):
    t = tree()

    action = request.args.get('action') 
    pkval = request.args.get('pkval')

    if action is not None and action == 'addTreeNode':
        ParentNodeID = request.args.get('ParentNodeID')
        # ParentNodeID = request.form.get('ParentNodeID')
        NodeLabel = request.form.get('node_label')
        NodeData = request.form.get('node_data')
        NodeLevel = '1'
        # t.data
        t.create_treeNode(ParentNodeID, NodeLabel, NodeData, NodeLevel)
        # return render_template('editor.html', tree=t)
        return redirect(url_for('editor', ParentNodeID=ParentNodeID))
    if action is not None and action == 'readTreeNode':
        # t.read_treeNodeAll()
        t.read_treenodeChildren(1)
        return render_template('editor.html', tree=t)
    return render_template('editor.html', tree=t, ParentNodeID=ParentNodeID)

@app.route('/addTreeNode', methods=['GET','POST'])
def addTreeNode():
    t = tree()
    ParentNodeID = None
    NodeLabel = 'book1'
    NodeData = 'first test of addtreenode route'
    NodeLevel = '3'
    t.create_treeNode(ParentNodeID, NodeLabel, NodeData, NodeLevel)

    return render_template('editor.html', t=t)

@app.route('/readTreeNode', methods=['GET','POST'])
def readTreeNode():
    """Based on the nodeID, list all the children of that nodeID"""
    t = tree()
    # t.read_treeNodeAll()
    t.read_treenodeChildren(1)
    # t.read_treeNodeByID(1)
    return render_template('editor.html', t=t)

def updateTreeNode():
    t = tree()
    t.update_treeNode()
    return render_template('editor.html', t=t)

def deleteTreeNode():
    t = tree()
    t.delete_treeNode()
    return render_template('editor.html', t=t)

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


