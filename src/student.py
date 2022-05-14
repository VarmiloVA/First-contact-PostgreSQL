from pickle import LIST
from tkinter import Tk, Canvas, Label, Frame, Entry, Button, W, E, Listbox, END
#En el futuro será mejor usar from tkinter import *	
import psycopg2

root = Tk()
root.title("Python & PostgreSQL")

def save_new_user(name, email, age):
    conn = psycopg2.connect(dbname="postgres", user="postgres",
                            password="password", host="localhost", port="5433")
    cursor = conn.cursor()
    query = '''INSERT INTO users(name, email, age) VALUES (%s, %s, %s)'''
    cursor.execute(query, (name, email, int(age)))

    print("Data succesfully saved")
    #Refresh with new students
    display_users()

    conn.commit()
    conn.close()

def search_user(id):
    conn = psycopg2.connect(dbname="postgres", user="postgres",
                            password="password", host="localhost", port="5433")
    cursor = conn.cursor()
    query = '''SELECT * FROM users WHERE id=%s'''
    cursor.execute(query, (id))

    row = cursor.fetchone()
    display_search(row)

    conn.commit()
    conn.close()

def display_search(row):
    listbox = Listbox(frame, width=20, height=1)
    listbox.grid(row=31, columnspan=4, sticky=W+E)

    if len(row) > 0:
        listbox.insert(END, row)
    else:
        listbox.insert(END, "No results")

def display_users():
    conn = psycopg2.connect(dbname="postgres", user="postgres",
                            password="password", host="localhost", port="5433")
    cursor = conn.cursor()
    query = '''SELECT * FROM users'''
    cursor.execute(query)

    row = cursor.fetchall()

    listbox = Listbox(frame, width=20, height=10)
    listbox.grid(row=10, columnspan=4, sticky=W+E)

    for i in row:
        listbox.insert(END, i)

    conn.commit()
    conn.close()

#Canva
canvas = Canvas(root, height=500, width=500).pack()

frame = Frame()
frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

label = Label(frame, text="Add a user")
label.grid(row=0, column=1)

#Name Input
label = Label(frame, text="Name:")
label.grid(row=1, column=1)

entry_name = Entry(frame)
entry_name.grid(row=1, column=2)

#Age Input
label = Label(frame, text="Age:")
label.grid(row=2, column=1)

entry_age = Entry(frame)
entry_age.grid(row=2, column=2)

#Email Input
label = Label(frame, text="Email:")
label.grid(row=3, column=1)

entry_email = Entry(frame)
entry_email.grid(row=3, column=2)

#Add button
button = Button(frame, text="Add", command=lambda:save_new_user(
    entry_name.get(), 
    entry_email.get(), 
    entry_age.get()
    ))
button.grid(row=4, column=2, sticky=W+E)

#Search
label = Label(frame, text="Search data")
label.grid(row=5, column=1)

label = Label(frame, text="Search by id:")
label.grid(row=6, column=0)

id_search = Entry(frame)
id_search.grid(row=6, column=1)

button = Button(frame, text="Search", command=lambda:search_user(id_search.get()))
button.grid(row=6, column=2, sticky=W+E)


display_users()
root.mainloop()