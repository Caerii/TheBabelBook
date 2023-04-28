from baseObject import baseObject

class tree(baseObject):
    def __init__(self):
        self.setup('jakirab_sofia_treenode')
        self.d = {}
        self.children = []
        self.exportString = []
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
        print("creating with ParentNodeID",ParentNodeID)
        if ParentNodeID == '':
            ParentNodeID = 0
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


    def export_treeNode(self, starterID=None, childList=None, tabMultiplier=0):
        if starterID == 1: # if it is the root node, then add it to the string
            nodeLabel = self.data[0]['NodeLabel'] #grab the node label
            nodeData = self.data[0]['NodeData'] #grab the node data
            string = nodeLabel + '~' + nodeData + '\n' # create the string
            self.exportString.append(string) # add it to the list
            childList = self.read_treenodeChildren(starterID) # get the children of the first node, as the base case
        if childList is not None: # if the child list is not none, then we can explore it
            for child in childList: 
                string =  '         '*tabMultiplier + child[2] + '~' + child[3]
                self.exportString.append(string)
                nextChildNodeID = (int)(child[1])
                nextChildList = self.read_treenodeChildren(nextChildNodeID)
                if nextChildList == []: # if it is empty, then do not explore it
                    pass
                self.export_treeNode(childList=nextChildList, tabMultiplier=tabMultiplier+1) # explore the next child list
    # CUSTOM SELECT QUERIES BELOW ##############################################
        
    def showChildListSizeLargerThan(self, size):
        '''This will show the child list size larger than the given integer number'''
        self.read_treeNodeChildren(1) 
        # if child in treeNodeChildren > 

        # call read_treenodechildren(1) to get everything
        # you will get a childlist
        # use a for loop to go through all the childlists, and keep a list [] of the ones that are larger than the given integer number
        # the list will just be the node ids that have childlists with lengths longer than the given integer number
        # []
        pass
        # basically you provide a number and it will show all the nodes that have a child list size larger than that number
    def showChildListSizeSmallerThan(self, size):
        '''This will show the child list size smaller than the given integer number'''
        pass
        # basically you provide a number and it will show all the nodes that have a child list size smaller than that number
    def export_treeNodePruned(self, starterID=None, childList=None, tabMultiplier=0, howManyLayersDeep=1):
        if starterID == 1: # if it is the root node, then add it to the string
            nodeLabel = self.data[0]['NodeLabel'] #grab the node label
            nodeData = self.data[0]['NodeData'] #grab the node data
            string = nodeLabel + '~' + nodeData + '\n' # create the string
            self.exportString.append(string) # add it to the list
            childList = self.read_treenodeChildren(starterID) # get the children of the first node, as the base case
        if childList is not None: # if the child list is not none, then we can explore it
            for child in childList: 
                string =  '         '*tabMultiplier + child[2] + '~' + child[3]
                self.exportString.append(string)
                nextChildNodeID = (int)(child[1])
                nextChildList = self.read_treenodeChildren(nextChildNodeID)
                if nextChildList == []: # if it is empty, then do not explore it
                    pass
                self.export_treeNode(childList=nextChildList, tabMultiplier=tabMultiplier+1)
        # you start at a a counter of howManyLayersDeep
        # everytime you call the function recursively, you subtract 1 from howManyLayersDeep
        # if howManyLayersDeep is 0, then you stop and do not go deeper
        # if howManyLayersDeep is 1, then you go one layer deep
        # if howManyLayersDeep is 2, then you go two layers deep, etc

    def searchKeywordInAllNodes(self, keywordString):
        '''Return a list of nodes that contain the keyword string'''
        pass

    def howManyNodes(self):
        '''Return the number of nodes in the tree'''
        nodes = self.read_treeNodeAll()
        print(len(nodes))
        return len(nodes)

    def howManyChildren(self,nodeID):
        '''Return the number of children of a given node'''
        
        #use read_treeNodeChildren to get all of the data
        #
        pass