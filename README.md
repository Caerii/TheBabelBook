# TheBabelBook
The Library of Babel, now with GPT-3!


# How it works
The user is first asked to provide a book title, and a book description.
GPT-3 will generate subheadings for the book, and you can click on any of the subheadings, to either expand more subheadings for that chapter, or to have GPT-3 start writing things for that chapter. You can also provide a description for the
This allows you to explore infinitely nested ideas inside of the book, depending on what you find interesting.


# Drawings Describing How The Interface Works
![IMG_6617](https://user-images.githubusercontent.com/123018982/235555336-d039d533-e777-45f3-be25-6da5e3fab2fb.jpg)
![IMG_6618](https://user-images.githubusercontent.com/123018982/235557075-56229e36-0eb2-4c9e-b4f2-fa5e6b24e1ff.jpg)

# Pictures Describing How The Interface Works





# Pictures Describing How The Queries Work

 



# How Does The export_treeNode Recursor Work?
This method exports a list of tree nodes as a string by taking three parameters, starterID, childList, and read_treenodeChildren. 
  starterID: this specifies the starting node ID, if an ID is not provided, it will be assumed that the root node is the starting node. 
  childList: this specifies the list of children that are attached to the current node. If the current node is not provided, the child nodes of the current node will be read by using read_treenodeChildren. 
First, the method will check if the starterID parameter = 1, if it does, it will read the label and data of the root node and create a string representation of it, which will then be appended to the exportString attribute of the class. Then, if the childList parameter is not None, the method will loop through each childNode in the list. The method will create a string representation of each childNode by striniing the node data and node label together with tab spaces, which will be appended to the exportString attribute of the class. 
![IMG_6632](https://user-images.githubusercontent.com/123018982/236074484-d40804cf-6799-4fc4-9ba9-1a4f37df7c65.jpg)





# Purpose & Motivation
The purpose of this web application is to allow for the creation of a user-defined book of any kind.
It utilizes GPT-3 to generate subheadings for a book, which can be infinitely nested. I think getting people to play around with the power of language models offers a lot for our creativity, and I think it would be fun to make it easy to play with. I personally read a lot of books, and the concept of a generative book is a fascinating concept that we are now capable of creating. I think co-creating is a better term though, and I think it will lead to new kinds of content creation.


# Python Packages
openai, flask, datetime, time 

<<<<<<< Updated upstream
=======
install them with `pip install -r requirements.txt`
>>>>>>> Stashed changes

# Application Login Credentials
username: o@o
password: 12345


# Relational Schema and Purpose of Each Table
![image](https://user-images.githubusercontent.com/123018982/235201241-34b18173-ddfa-4b5a-864c-7be7152991f5.png)

User Table: to keep track of user information such as name and password within the database. 

TreeNode Table: to keep track of tree data that is generated on the website, keeps track of information such as NodeID, NodeLabel, NodeLevel and ParentNodeID

Session Table: to keep track of the session that a user was on, allowing them to go back to that session at a later time. 

# Custom Select Queries
Query 1: totalNodeCount
Query 2: layersDeep
Query 3: totalChildCount

# SQL Schema File 
Can be found in /old/data.sql file 




