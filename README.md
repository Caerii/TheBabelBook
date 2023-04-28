# TheBabelBook
The Library of Babel, now with GPT-3!

# How it works
The user is first asked to provide a book title, and a book description.
GPT-3 will generate subheadings for the book, and you can click on any of the subheadings, to either expand more subheadings for that chapter, or to have GPT-3 start writing things for that chapter. You can also provide a description for the
This allows you to explore infinitely nested ideas inside of the book, depending on what you find interesting.

# Purpose & Motivation
The purpose of this web application is to allow for the creation of a user-defined book of any kind.
It utilizes GPT-3 to generate subheadings for a book, which can be infinitely nested. I think getting people to play around with the power of language models offers a lot for our creativity, and I think it would be fun to make it easy to play with. I personally read a lot of books, and the concept of a generative book is a fascinating concept that we are now capable of creating. I think co-creating is a better term though, and I think it will lead to new kinds of content creation.

# Python Packages
openai, flask, datetime, time 

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
Can be found in data.sql file 




