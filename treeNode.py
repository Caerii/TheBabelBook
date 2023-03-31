from baseObject import baseObject

class tree(baseObject):
    def __init__(self):
        self.setup('TreeNode')
    def toList(self):
        l = []
        for row in self.data:
            s = f"{row['ParentNodeID']} ({row['NodeLabel']} {row['NodeData']} {row['NodeLevel']})"  
            l.append(s)
        return l