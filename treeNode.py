from baseObject import baseObject
import openai

class tree(baseObject):
    def __init__(self):
        '''SQL SCHEMA:
        CREATE TABLE IF NOT EXISTS `jakirab_sofia_treenode` (
             '''
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
    def create_treeNode(self, ParentNodeID, NodeLabel, NodeData, NodeLevel=1):
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
        # make arguments into integer
        ParentNodeID = int(ParentNodeID)
        self.getAll()
        l = self.toList()
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
        self.getAll()
        listNodes = self.toList()
        # Extract the index of the node with the given NodeID
        index = 0
        for node in listNodes:
            cols = node.split('~')
            if cols[1] == str(NodeID):
                break 
            index += 1
        print("updating with NodeID",NodeID)
        if self.exists():
            self.data[index]['NodeLabel'] = NodeLabel
            self.data[index]['NodeData'] = NodeData
            # self.set(self.d)
            print("index",index)
            self.update(index)
            print("updated treenode",self.data[index])

    def delete_treeNode(self, NodeID):
        '''This will delete the specific treenode based on the NodeID given'''
        # if there is children, just print a warning instead of deleting
        childList = self.read_treenodeChildren(NodeID)
        if childList != []:
            print("This node has children, please use cascade delete instead")
            return -1
        self.deleteById(NodeID)
        print("Deleted node with id: " + str(NodeID))

    # def cascadeDelete(self, NodeID):
    #     '''This will delete all the nodes under the given node id NodeID except for the node itself'''
    #     # if you are deleting the root node, then you are deleting the whole tree, so we create a new root node for you
    #     if NodeID == 1:
    #         self.create_treeNode(0, 'root', 'root')
    #     childList = self.read_treenodeChildren(NodeID)
    #     print("childList",childList)
    #     for child in reversed(childList): # go through the list backwards so that the children are deleted first before the parent
    #         print("child",child)
    #         self.cascadeDelete(child[1])
    #     print("Deleting all children of node: " + str(NodeID) + " except for the node itself")
    #     self.delete_treeNode(NodeID)

    def cascadeDelete(self, NodeID):
        '''This will delete all the nodes under the given node id NodeID except for the node itself'''
        # if you are deleting the root node, then you are deleting the whole tree, so we create a new root node for you
        if NodeID == 1:
            self.create_treeNode(0, 'root', 'root')
        childList = self.read_treenodeChildren(NodeID)
        print("childList",childList)
        for child in reversed(childList): # go through the list backwards so that the children are deleted first before the parent
            print("child",child)
            self.cascadeDelete(child[1])
        print("Deleting all children of node with id: " + str(NodeID))
        self.delete_children(NodeID) # delete all the children of the node
        print("Deleted all children of node with id: " + str(NodeID))

    def delete_children(self, NodeID):
        '''This will delete all the children of the given node id NodeID'''
        childList = self.read_treenodeChildren(NodeID)
        for child in childList:
            self.deleteById(child[1])

    def getTreeParentIDByNodeID(self, NodeID):
        '''This will return the parent node id of the given node id'''
        self.getByField('NodeID', NodeID)
        # if the node id is 0, then it is the root node, and it has no parent node id
        if self.exists():
            ParentNodeID = self.data[0]['ParentNodeID']
            if ParentNodeID == None or NodeID == 0:    
                return 0
            return self.data[0]['ParentNodeID']
        else:
            return None

    def getTreeNodeLabelByNodeID(self, NodeID):
        '''This will return the node label of the given node id'''
        self.getByField('NodeID', NodeID)
        if self.exists():
            return self.data[0]['NodeLabel']
        else:
            return None

    def export_treeNode(self, starterID=None, childList=None, tabMultiplier=0):
        '''This will export the tree into a string'''
        if starterID == 1: # if it is the root node, then add it to the string
            nodeLabel = self.data[0]['NodeLabel'] #grab the node label
            nodeData = self.data[0]['NodeData'] #grab the node data
            string = nodeLabel + '~' + nodeData + '\n' # create the string
            self.exportString.append(string) # add it to the list
            childList = self.read_treenodeChildren(starterID) # get the children of the first node, as the base case
        if childList is not None: # if the child list is not none, then we can explore it
            for child in childList: 
                string =  '\t'*tabMultiplier + child[2] + '~' + child[3]
                self.exportString.append(string)
                nextChildNodeID = (int)(child[1])
                nextChildList = self.read_treenodeChildren(nextChildNodeID)
                if nextChildList == []: # if it is empty, then do not explore it
                    pass
                self.export_treeNode(childList=nextChildList, tabMultiplier=tabMultiplier+1) # explore the next child list

    # AI Functions
    def generateChapters(self, userPrompt, openAIKey, promptSoFar, howManyChapters=5):
        '''This will generate a list of chapters based on the user prompt'''
        
        formatting = "Here is what we have written in the book so far: \n\""
        prompt = f"Please generate a list of {howManyChapters} chapter subheadings for the book with the description as <{userPrompt}> in a numbered, bulleted list structured as follows:\n \"1. example_subtitle1 \n 2. example_subtitle2\" \n Here are {howManyChapters} new chapters based on the description and written work so far:\n"
        prompt = formatting + promptSoFar + "\"" + prompt
        
        # Call the OpenAI API with the prompt to generate a list of book subtitles
        # Format the list as "Please generate a list of chapter subheadings for the book with the {user_prompt} in a numbered, bulleted list"
        openai.api_key = openAIKey
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
            text_output = text_output.replace(str(i+1)+".", str(i+1) + "-")

        # create a list of the generated chapter subheadings
        chapterList = text_output.split("\n")
        # remove first new line
        chapterList.pop(0)
        # split each element of the list by space
        for i in range(len(chapterList)):
            chapterList[i] = chapterList[i].split(" ")
            # remove the first element of the list, which is the number
            chapterList[i].pop(0)
            # join the list back together with spaces
            chapterList[i] = " ".join(chapterList[i])

        print("prompt: ", prompt)

        return chapterList # returns a string of the generated list of chapter subheadings

    def generateNodesBasedOnChapters(self, chapterList, NodeID):
        '''This will generate nodes based on the chapter list'''
        # create a list of nodes based on the chapter list
        for i in range(len(chapterList)):
            # create node for each chapter
            print("Creating node for chapter: " + chapterList[i])
            self.create_treeNode(ParentNodeID=NodeID, NodeLabel=chapterList[i], NodeData="")

    # def generatePromptFromRootToCurrentNode(self, currentNodeID, wholeBook):
    #     '''This will generate a prompt string from the root node to the current node'''
    #     def extract_and_format(node_list, depth=0): # depth is the number of tabs
    #         nonlocal chapter_number, subchapter_numbers, formatted_prompt 
    #         # nonlocal variables work by allowing you to assign to variables in an outer (but not global) scope. 

    #         while node_list: # while the node list is not empty, you can explore it
    #             node = node_list.pop(0).strip() # pop the first element of the list
    #             if not node or node[0] == "#": # if the node is empty or starts with a #, then continue
    #                 continue

    #             if depth == 0: # if the depth is 0, then it is a chapter
    #                 chapter_number += 1 # increment the chapter number
    #                 subchapter_numbers = [0] # reset the subchapter numbers
    #                 formatted_prompt += "{}. {}\n".format(chapter_number, node) # add the chapter number and the node to the prompt
    #             else: # if the depth is not 0, then it is a subchapter
    #                 while len(subchapter_numbers) < depth: # while the length of the subchapter numbers is less than the depth, then add a 0
    #                     subchapter_numbers.append(0) # add a 0
    #                 subchapter_numbers[-1] += 1 # increment the last element of the subchapter numbers
    #                 subchapter_number_string = ".".join(str(x) for x in subchapter_numbers) # create a string of the subchapter numbers

    #                 if node.endswith("~"): # if the node ends with a ~, then it is a node
    #                     formatted_prompt += "{}.{} {}\n".format(str(chapter_number), subchapter_number_string, node[:-1]) # add the chapter number, subchapter number, and node to the prompt
    #                     subchapter_numbers.append(0) # add a 0 to the subchapter numbers
    #                 else: # if the node does not end with a ~, then it is a subnode
    #                     formatted_prompt += "{}.{} {}\n".format(str(chapter_number), subchapter_number_string, node) # add the chapter number, subchapter number, and node to the prompt

    #             if node_list and node_list[0].startswith("\t"): # if the node list is not empty and the first element of the node list starts with a tab, then it is a subnode
    #                 sub_nodes = [] # create a list of subnodes
    #                 while node_list and node_list[0].startswith("\t"): # while the node list is not empty and the first element of the node list starts with a tab, then it is a subnode
    #                     sub_nodes.append(node_list.pop(0)[1:]) # add the subnode to the list of subnodes
    #                 extract_and_format(sub_nodes, depth + 1) # recursively call the function to add the subnodes to the prompt
    #                 subchapter_numbers.pop() # remove the last element of the subchapter numbers

    #             # Reset subchapter_numbers for nodes with the same depth
    #             if depth > 0: # if the depth is greater than 0, then it is a subchapter
    #                 subchapter_numbers = subchapter_numbers[:depth] # reset the subchapter numbers

    #     currentNodeLabel = self.getTreeNodeLabelByNodeID(currentNodeID) # get the current node label
    #     currentNodeIndex = -1 # initialize the current node index
    #     for i in range(len(wholeBook)): # for each element in the whole book
    #         if currentNodeLabel in wholeBook[i]: # if the current node label is in the element of the whole book
    #             currentNodeIndex = i # set the current node index to the index of the element of the whole book
    #             break

    #     wholeBook = wholeBook[:currentNodeIndex + 1] # set the whole book to be the whole book up to the current node index

    #     chapter_number = 0 # initialize the chapter number
    #     subchapter_numbers = [] # initialize the subchapter numbers
    #     formatted_prompt = (
    #         "You are generating an original work. The following is a book with a list of chapter headings and their content.\n"
    #         "The ~ symbol separates the chapter heading from the content\n"
    #     )

    #     extract_and_format(wholeBook) # call the extract_and_format function to generate the prompt

    #     # print("final prompt string", formatted_prompt)
    #     return formatted_prompt
    def generatePromptFromRootToCurrentNode(self, currentNodeID, wholeBook):
        def extract_and_format(node_list, depth=0):
            nonlocal chapter_number, subchapter_numbers, formatted_prompt

            while node_list:
                node = node_list.pop(0).strip()
                if not node or node[0] == "#":
                    continue

                if depth == 0:
                    chapter_number += 1
                    subchapter_numbers = [0]
                    formatted_prompt += "{}. {}\n".format(chapter_number, node)
                else:
                    while len(subchapter_numbers) < depth:
                        subchapter_numbers.append(0)
                    subchapter_numbers[-1] += 1
                    subchapter_number_string = ".".join(str(x) for x in subchapter_numbers)

                    if node.endswith("~"):
                        formatted_prompt += "{}.{} {}\n".format(str(chapter_number), subchapter_number_string, node[:-1])
                        subchapter_numbers.append(0)
                    else:
                        formatted_prompt += "{}.{} {}\n".format(str(chapter_number), subchapter_number_string, node)

                if node_list and node_list[0].startswith("\t"):
                    sub_nodes = []
                    while node_list and node_list[0].startswith("\t"):
                        sub_nodes.append(node_list.pop(0)[1:])
                    extract_and_format(sub_nodes, depth + 1)
                    subchapter_numbers.pop()

                if depth > 0:
                    subchapter_numbers = subchapter_numbers[:depth]

        currentNodeLabel = self.getTreeNodeLabelByNodeID(currentNodeID)
        currentNodeIndex = -1
        for i in range(len(wholeBook)):
            if currentNodeLabel in wholeBook[i]:
                currentNodeIndex = i
                break

        # Find the last child node one layer down below the current node
        last_child_index = currentNodeIndex
        while last_child_index + 1 < len(wholeBook) and wholeBook[last_child_index + 1].startswith("\t"):
            last_child_index += 1

        wholeBook = wholeBook[:last_child_index + 1]

        chapter_number = 0
        subchapter_numbers = []
        formatted_prompt = (
            "You are generating an original work. The following is a book with a list of chapter headings and their content.\n"
            "The ~ symbol separates the chapter heading from the content\n"
        )

        extract_and_format(wholeBook)
        print("final prompt string", formatted_prompt)

        return formatted_prompt


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
    def export_treeNodePruned(self, starterID=None, childList=None, tabMultiplier=0, howManyLayersDeep=None):
        if starterID == 1: # if it is the root node, then add it to the string
            nodeLabel = self.data[0]['NodeLabel'] #grab the node label
            nodeData = self.data[0]['NodeData'] #grab the node data
            string = nodeLabel + '~' + nodeData + '\n' # create the string
            self.exportString.append(string) # add it to the list
            childList = self.read_treenodeChildren(starterID) # get the children of the first node, as the base case
        if childList is not None: # if the child list is not none, then we can explore it
            for child in childList:
                if howManyLayersDeep is not None and tabMultiplier >= howManyLayersDeep:
                    return # stop recursion if current depth is greater than or equal to howManyLayersDeep
                string =  '         '*tabMultiplier + child[2] + '~' + child[3]
                self.exportString.append(string)
                nextChildNodeID = (int)(child[1])
                nextChildList = self.read_treenodeChildren(nextChildNodeID)
                if nextChildList == []: # if it is empty, then do not explore it
                    pass
            self.export_treeNodePruned(childList=nextChildList, tabMultiplier=tabMultiplier+1, howManyLayersDeep=howManyLayersDeep)

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

    def howManyChildren(self, nodeID):
        '''Return the number of children of a given node'''
        entireNode = self.read_treeNodeByID(nodeID)
        nodeID = entireNode[0]['NodeID']
        children = self.read_treenodeChildren(nodeID)
        print(nodeID)
        return len(children)

