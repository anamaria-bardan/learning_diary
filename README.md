# ***learning_diary***
Project created Based on The Complete Python/PostgreSQL Course 2.0 
From < https://www.udemy.com/course/complete-python-postgresql-database-course/> 
Section 3

## ***Project details***
- The scope of the project is simple - tracking one's learning progress
- when running the porgram the user gets the following Menu and is prompted to make a selection
```
Please select one of the following options:
    1. Add a new entry for today
    2. view entries
    3. Exit
    
    Your selection: 
```
- For 1 the user will be prompted to input the date and content of what they have learned
```
what have you learned today?
Input the date:
```
- For 2 all the DB entries logged thus far will be displayed
- 3 - self explanatory

## ***Main takeaways***:

### **Coding workflow**
- If separate files are used in the project, each file should have functions having the same purpose 
	- Ex: database.py should only have functions that read and write to and from the database, those functions should not also deal with user input
- Try to make the code as readable as possible, turn into functions everything that can be turned into a function - main body should be clean and readable, got to function defs for more details

### **Sqlite**
- Use sqlite3 module to connect to sqlite DB
	- You can open as many connections as you want (connection limits do not apply here as there is no server involved)
	- Always close the connections at the end
- Only one connection at a time can modify the DB

- basic commands for working with SQLite
```
-- importing the module
import sqlite3
-- creating a connection
connection=sqlite3.connect('data.db') 
-- starting a transaction
connection.execute()
-- a transaction needs to be closed (commited or rolled back) for the changes to actually take place in DB
connection.commit()
-- or use a context manager to handle automatically commiting at the end
    with connection:
            connection.execute('create table users (firstname text)')
```
### **New notions**
- Cursor
	- = structure that allows us to traverse a result set 
	- DB cursors allow the Db to only return results when requested
	- Usually a cursor only loads the desired number of rows, however the SQLite cursor loads all results
- SQL injection attack
	- When users can execute any SQL code they want without directly accessing your DB
	- Can happen when string formatting is used to pass the user input to the query 
		- In this case the user can input whatever info, even multiple queries separated by; and therefore getting info from DB or altering the DB
	- To avoid this use arguments for the query
```
connection.execute(f"insert into entries values ('{entry_content}','{entry_date}')") -- DO NOT USE THIS!!!
connection.execute('insert into entries values (?,?);',(entry_content, entry_date) -- USE THIS INSTEAD
```
