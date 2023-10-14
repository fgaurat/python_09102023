import sys
import sqlite3
from UserDAO import UserDAO
from User import User
import configparser
import argparse
from tkinter import *
from tkinter import ttk

def main():
    dao = UserDAO("users_db.db")
    users = dao.findAll()

    ws = Tk()
    ws.title('TodoList')
    ws.geometry('800x600')
    ws['bg']='#fb0'

    tv = ttk.Treeview(ws,show="headings")
    tv['columns']=('Id', 'Name', 'Email')
    tv.column('Id',  anchor=CENTER,stretch=NO)
    tv.column('Name', anchor=CENTER, width=80)
    tv.column('Email', anchor=CENTER, width=80)

    tv.heading('Id', text='Id', anchor=CENTER)
    tv.heading('Name', text='Name', anchor=CENTER)
    tv.heading('Email', text='Email', anchor=CENTER)
    
    for user in users:
        tv.insert(parent='', index=user.id, iid=user.id, text='', values=(user.id,user.last_name,user.email))
    
    tv.pack(fill=BOTH,expand=True)


    ws.mainloop()

if __name__=='__main__':
    main()
