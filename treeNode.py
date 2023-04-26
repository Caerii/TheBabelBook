from baseObject import baseObject

class tree(baseObject):
    def __init__(self):
        self.setup('jakirab_sofia_treenode')
        self.d = {}
    def toList(self):
        l = []
        for row in self.data:
            s = f"{row['ParentNodeID']}~{row['NodeID']}~{row['NodeLabel']}~{row['NodeData']}~{row['NodeLevel']}"
            # example string
            # s = "1 (book1 first test of addtreenode route 3)"  
            l.append(s)
        return l
    def create_treeNode(self, ParentNodeID, NodeLabel, NodeData, NodeLevel):
        t = tree()
        self.d['ParentNodeID'] = ParentNodeID
        self.d['NodeLabel'] = NodeLabel
        self.d['NodeData'] = NodeData
        self.d['NodeLevel'] = NodeLevel
        t.set(self.d)
        t.insert()
        print(t.data)
    def read_treeNodeByID(self, NodeID):
        '''This should populate the page with existing treenode data'''
        t = tree()
        t.getByField('NodeID', NodeID)
        return t.data
        # t.getAll() # get all records
        # l = t.toList() # convert to list
        # print(l)
        # 
        ## product_index = makeMenu('Select Product', t.toList()) ##(replace with button request with post request)##
        # print("Here is the stuff:\n")
        # print(t.data[product_index]['ParentNodeID'])
        # print(t.data[product_index]['NodeLabel'])
        # print(t.data[product_index]['NodeData'])
        # print(t.data[product_index]['NodeLevel'])
    def read_treenodeChildren(self, ParentNodeID):
        '''This should populate the page with existing treenode data'''
        t = tree()
        t.getAll()
        l = t.toList()
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
                    childElement = cols[1:4]
                    childList.append(childElement)
        print(childList)
        return childList

    def read_treeNodeAll(self):
        '''Read out all of the available treenodes'''
        t = tree()
        t.getAll() # get all records
        l = t.toList() # convert to list
        return l # return the list
    def update_treeNode(self, NodeID, NodeLabel, NodeData):
        '''This will change the specific treenode label and data based on the NodeID given'''
        t = tree()
        t.getAll()
        # after getting all the nodes, we need to find the node that matches the NodeID
        # then we need to update the NodeLabel and NodeData
        

        ## product_index = makeMenu('Select Book', t.toList()) ##(replace with button request with post request)##

        # print("t.data!!! :", t.data)
        # p_index = t.data[product_index]['NodeID']
        # print(f"product index: {product_index}")
        # t.data[product_index]['ParentNodeID'] = None
        # t.data[product_index]['NodeLabel'] = 'bookvygt6ty'
        # t.data[product_index]['NodeData'] = 'this time the dog chased the cat' 
        # t.data[product_index]['NodeLevel'] = '4'
        t.update(product_index)
    def delete_treeNode(self, NodeID):
        t = tree()
        t.getAll()
        ##product_index = makeMenu('Select Product', t.toList())  ##(replace with button request with post request)##
        t_index = t.data[product_index]['NodeID']
        t.deleteById(t_index) #delete record by id
        print("Deleted product with id: " + str(t_index))


        