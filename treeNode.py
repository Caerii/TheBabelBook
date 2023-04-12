from baseObject import baseObject

class tree(baseObject):
    def __init__(self):
        self.setup('jakirab_sofia_treenode')
        self.d = {}
    def toList(self):
        l = []
        for row in self.data:
            s = f"{row['ParentNodeID']} ({row['NodeLabel']} {row['NodeData']} {row['NodeLevel']})"  
            l.append(s)
        return l
    def create_treeNode(self, ParentNodeID, NodeLabel, NodeData, NodeLevel):
        self.d['ParentNodeID'] = None
        self.d['NodeLabel'] = 'book1'
        self.d['NodeData'] = 'there once was a dog'
        self.d['NodeLevel'] = '3'
        t.set(d)
        t.insert()
        print(t.data)
    def read_treeNode(self, ParentNodeID, NodeLabel, NodeData, NodeLevel):
        t = tree()
        t.getAll() # get all records
        ## product_index = makeMenu('Select Product', t.toList()) ##(replace with button request with post request)##
        print("Here is the stuff:\n")
        print(t.data[product_index]['ParentNodeID'])
        print(t.data[product_index]['NodeLabel'])
        print(t.data[product_index]['NodeData'])
        print(t.data[product_index]['NodeLevel'])
    def update_treeNode(self, ParentNodeID, NodeLabel, NodeData, NodeLevel):
        t = tree()
        t.getAll()
        ## product_index = makeMenu('Select Book', t.toList()) ##(replace with button request with post request)##
        print("t.data!!! :", t.data)
        p_index = t.data[product_index]['NodeID']
        print(f"product index: {product_index}")
        t.data[product_index]['ParentNodeID'] = None
        t.data[product_index]['NodeLabel'] = 'bookvygt6ty'
        t.data[product_index]['NodeData'] = 'this time the dog chased the cat' 
        t.data[product_index]['NodeLevel'] = '4'
        t.update(product_index)
    def delete_treeNode(self, ParentNodeID, NodeLabel, NodeData, NodeLevel):
        t = tree()
        t.getAll()
        ##product_index = makeMenu('Select Product', t.toList())  ##(replace with button request with post request)##
        t_index = t.data[product_index]['NodeID']
        t.deleteById(t_index) #delete record by id
        print("Deleted product with id: " + str(t_index))


        