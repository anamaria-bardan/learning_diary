# -*- coding: utf-8 -*-
"""
Created on Thu Dec 30 14:04:25 2021

@author: Anamaria
"""


import sqlite3
connection=sqlite3.connect('data.db')
connection.row_factory=sqlite3.Row #cursor will return a dictionary instead of a tuple, a bit slower

def create_table():
    with connection:
        connection.execute('create table if not exists entries (content text, date text)')
    
def add_entries (entry_content,entry_date):
    with connection:
       #DO NOT USE - at risk of SQL injection attack
       # connection.execute(f"insert into entries values ('{entry_content}','{entry_date}')")
        connection.execute(
            'insert into entries values (?,?);',(entry_content, entry_date)
            )
def get_entries ():
    #context manager not needed - only getting entries, nothing to commit or roll back
    cursor=connection.execute('select * from entries;')
    #connection.execute() creates by default a cursor
    return cursor #each row returned will be a tuple
        

              
# add_entries()
# add_entries()

# view_entries()