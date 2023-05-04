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

Now that you have clicked on that number, scroll to the bottom of this page to input information about what you want the book to be about. You can also input information about what you want the chapters to be about. Change the personality of the writer by typing something of your choosing. 
<img width="1204" alt="image" src="https://user-images.githubusercontent.com/123018982/236079635-ba55699b-d423-4399-a9bc-c1324f369ca8.png">

If you input something under "Describe Book Chapters You Want!", you will now have chapters that you can click on and create new stories for those chapters by clicking on the numbers next to the chapters! 
<img width="1204" alt="image" src="https://user-images.githubusercontent.com/123018982/236080322-eee37f29-1eb8-42db-9412-dbbc4fedbdfc.png">

To change information regarding a current node, click on the drop down menu under "Select a node to update:". You can then enter new information regarding the node label and node data for that node. If you want to delete or cascade delete a node, use the drop down menu to choose which ones to delete. If you want to delete the whole book use the "Start New Book" button. To export the stories, click on the "Export TreeNode" button, and choose whether you want it to be numbered or in tabs + newline form. 
<img width="1204" alt="image" src="https://user-images.githubusercontent.com/123018982/236081539-5e9e84df-e5f2-4aa5-8f95-5d253a3e63bb.png">

Go back to the main menu and click on the "Custom Queries" button to view how many nodes are in the tree, how many layers are in the tree, or how many children are in the tree. 
<img width="1204" alt="image" src="https://user-images.githubusercontent.com/123018982/236081974-7031ac99-d456-47fa-8193-1da4f5f86d78.png">


# Drawings Describing How The Queries Work
 howManyNodes() Query:
 ![IMG_6633](https://user-images.githubusercontent.com/123018982/236083428-e4ea39be-7fb1-4a2c-a174-323cd2195aef.jpg)

 howmanyChildren() Query:
 ![IMG_6634](https://user-images.githubusercontent.com/123018982/236085316-5b9e1afc-b6f0-47e3-941b-15fe3c3efb79.jpg)

 
 howManyLayers() Query:
 


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




