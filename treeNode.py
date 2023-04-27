from baseObject import baseObject

class tree(baseObject):
    def __init__(self):
        self.setup('jakirab_sofia_treenode')
        self.d = {}
        self.children = []
    def toList(self):
        l = []
        for row in self.data:
            s = f"{row['ParentNodeID']}~{row['NodeID']}~{row['NodeLabel']}~{row['NodeData']}~{row['NodeLevel']}"
            # example string
            # s = "1 (book1 first test of addtreenode route 3)"  
            l.append(s)
        return l
    def clear(self):
        self.d = {} # for tree
        self.data = [] # for sql
    def create_treeNode(self, ParentNodeID, NodeLabel, NodeData, NodeLevel):
        self.clear()
        self.d['ParentNodeID'] = ParentNodeID
        self.d['NodeLabel'] = NodeLabel
        self.d['NodeData'] = NodeData
        self.d['NodeLevel'] = NodeLevel
        self.set(self.d)
        print("created treenode",self.d)
        self.insert()
        print(self.data)
        
    def read_treeNodeByID(self, NodeID):
        '''This should populate the page with existing treenode data'''
        
        self.getByField('NodeID', NodeID)

        # if this runs into an error, it is because the node id is not in the database
        # keep blank into self.data then

        if self.data is None:
            self.data = []
            return self.data

        return self.data
    def read_treenodeChildren(self, ParentNodeID):
        '''This should populate the page with existing treenode data'''
        # t = tree()
        self.getAll()
        l = self.toList()
        # l = self.read_treeNodeAll()
        # print("this is l",l)
        childList = []
        # for all the nodes in the list, only show the ones with the chosen parent node id
        # if the parent node id is none, then we need to get all the nodes that have a parent node id of none
        # go through the list and find all the
        for row in l:
            cols = row.split('~')
            currentParentNode = cols[0] # this is the parent node id
            if currentParentNode == 'None':
                pass
            else:
                if int(currentParentNode) == ParentNodeID:
                    # print(cols[1:4])
                    # print("currentParentNode!!!!!!!!!!",currentParentNode)
                    # print("ParentNodeID!!!!!!!!!!",ParentNodeID)
                    childElement = cols[0:4]
                    #print(childElement)
                    childList.append(childElement)
        # print(childList)
        self.children = childList
        return childList

    def read_treeNodeAll(self):
        '''Read out all of the available treenodes'''
        t = tree()
        t.getAll()
        l = t.toList() 
        return l # return the list
    def update_treeNode(self, NodeID, NodeLabel, NodeData):
        '''This will change the specific treenode label and data based on the NodeID given'''
        self.getByField('NodeID', NodeID)
        if self.exists():
            self.d['NodeLabel'] = NodeLabel
            self.d['NodeData'] = NodeData
            self.set(self.d)
            self.update()
            print("updated treenode",self.d)

    def delete_treeNode(self, NodeID):
        self.deleteById(NodeID)
        print("Deleted node with id: " + str(NodeID))


        