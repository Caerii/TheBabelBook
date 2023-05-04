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
When the user interface is first opened, it will show this page. Click on the "editor" button to begin using the BabelBook! 
<img width="1204" alt="image" src="https://user-images.githubusercontent.com/123018982/236076791-12e5b247-39ea-4f1c-8ae7-40468e18f316.png">

Enter a Node Label of your choosing such as, "The Cat" and click on the "Add TreeNode" button. You can also add Node Data of your choosing such as, "dogs fighting". You can choose to add one or the other, or both! This will create a new treenode. 
<img width="1204" alt="image" src="https://user-images.githubusercontent.com/123018982/236078521-21be67e7-0ca0-4401-943a-3e4049379d27.png">

If you scroll to the bottom of the page, you can see the Node Label and Node Data that you inputted, as shown here. Click on the number to edit this node, and add information to it. 
<img width="1204" alt="image" src="https://user-images.githubusercontent.com/123018982/236078899-e00f1a8a-c304-4b74-a843-d7628cde90ca.png">









# Drawings Describing How The Queries Work

 



# How Does The export_treeNode Recursor Work?
This method exports a list of tree nodes as a string by taking three parameters, starterID, childList, and read_treenodeChildren. 
  starterID: this specifies the starting node ID, if an ID is not provided, it will be assumed that the root node is the starting node. 
  childList: this specifies the list of children that are attached to the current node. If the current node is not provided, the child nodes of the current node will be read by using read_treenodeChildren. 
First, the method will check if the starterID parameter = 1, if it does, it will read the label and data of the root node and create a string representation of it, which will then be appended to the exportString attribute of the class. Then, if the childList parameter is not None, the method will loop through each childNode in the list. The method will create a string representation of each childNode by striniing the node data and node label together with tab spaces, which will be appended to the exportString attribute of the class. 
![IMG_6632](https://user-images.githubusercontent.com/123018982/236074710-96fd3ea9-4ce1-4d0c-9c6d-eec052da2fde.jpg)






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




