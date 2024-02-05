import tkinter as tk
from tkinter import messagebox
import bcrypt
from sqlite3 import DatabaseError,IntegrityError,InternalError,OperationalError

def saveNewUser(usernameEntry,passwordEntry,connection):
    userVal=usernameEntry.get()
    passVal=passwordEntry.get()
    hashPass=bcrypt.hashpw(passVal.encode(),bcrypt.gensalt())
    try:
        connection.execute("INSERT INTO users(username,password) VALUES(?,?);",(userVal,hashPass.decode('UTF-8')))
        connection.commit()
        messagebox.showinfo("Success", "User created successfully.")
    except IntegrityError or DatabaseError or OperationalError:
        messagebox.showinfo("Error", "The operation failed!! Please try again")

def delUser(uidEntry,connection):
    try:
        connection.execute(f"DELETE FROM users WHERE uid={uidEntry.get()};")
        connection.commit()
        messagebox.showinfo("Success", "User deleted successfully.")
    except DatabaseError or InternalError:
        messagebox.showinfo("Error", "The operation failed!! Please try again")

def deleteUser(connection):
    delUserPage = tk.Tk()
    delUserPage.title("User Management")
    delUserPage.geometry("1920x1080")
    appLabel= tk.Label(
        delUserPage, text="Delete a user", fg="#06a099", width=40
    )
    appLabel.config(font=("Sylfaen", 30))
    appLabel.grid(row=0)
    uidLabel = tk.Label(delUserPage, text="Enter the uid of user to be deleted:", fg="#06a099", width=40)
    uidLabel.config(font=("Sylfaen", 30))
    uidLabel.grid(row=5)
    uidEntry = tk.Entry(delUserPage, width=30)
    uidEntry.grid(row=5, column=4, padx=(0, 10), pady=(30, 20))
    uidEntry.delete(0, tk.END)
    delButton = tk.Button(
        delUserPage, text="Delete", command=lambda: delUser(uidEntry,connection)
    )
    delButton.grid(row=12, column=4)
    delUserPage.mainloop()


def addNewUser(connection):
    userPage = tk.Tk()
    userPage.title("User Management")
    userPage.geometry("1920x1080")
    appLabel = tk.Label(userPage, text="Enter the details of the new user", fg="#06a099", width=40)
    appLabel.config(font=("Sylfaen", 30))
    appLabel.grid(row=0)
    newNameLabel = tk.Label(
        userPage, text="Enter username of new user: ", fg="#06a099", width=40
    )
    newNameLabel.config(font=("Sylfaen", 30))
    newNameLabel.grid(row=5)
    usernameEntry = tk.Entry(userPage, width=30)
    usernameEntry.grid(row=5, column=4, padx=(0, 10), pady=(30, 20))
    passLabel = tk.Label(
        userPage, text="Enter password of new user: ", fg="#06a099", width=40
    )
    passLabel.config(font=("Sylfaen", 30))
    passLabel.grid(row=10)
    passwordEntry = tk.Entry(userPage, width=30)
    passwordEntry.grid(row=10, column=4, padx=(0, 10), pady=(30, 20))
    saveButton = tk.Button(
        userPage, text="Save", command=lambda: saveNewUser(usernameEntry,passwordEntry,connection)
    )
    saveButton.grid(row=12, column=4)
    userPage.mainloop()