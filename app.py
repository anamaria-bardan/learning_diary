# -*- coding: utf-8 -*-
"""
Created on Wed Dec 29 19:40:06 2021

@author: Anamaria
"""
#########imports
from database import add_entries,get_entries,create_table
import sqlite3

#########connect to DB
connection=sqlite3.connect('data.db')     


########variables
menu="""Please select one of the following options:
    1. Add a new entry for today
    2. view entries
    3. Exit
    
    Your selection: """
welcome='Welcome to the learning diary!'

create_table()
#########functions
def prompt_new_entry():
    entry_content=input('what have you learned today?')
    entry_date=input ('Input the date:')
    add_entries(entry_content,entry_date)    

def display_entries(entries):
    for e in entries:
        print(f"{e['date']} \n{e['content']} \n\n")  
 
   

##########main body       
print(welcome)
user_input=input(menu)
while user_input!='3':
    
    if user_input=='1':
        prompt_new_entry()
        
    elif user_input=='2':
        display_entries(get_entries())
            
    else:
        print('Invalid option, please choose only 1,2 or 3')
    user_input=input(menu)

    