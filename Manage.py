import tkinter as tk
from tkinter import StringVar, ttk, messagebox
import sqlite3

admin = tk.Tk()
admin.title("Admin Panel")
admin.geometry("1920x1080")
connection = sqlite3.connect('SQLite3\manage.db')
cursor = connection.cursor()

TABLE_NAME = "student_table"
STUDENT_USN = "student_usn"
STUDENT_NAME = "student_name"
STUDENT_COLLEGE = "student_college"
STUDENT_ADDRESS = "student_address"
STUDENT_PHONE = "student_phone"
STUDENT_EMAIL = "student_email"


global usr,passw
usr = StringVar()
passw = StringVar()
topLabel = tk.Label(admin, text="Welcome to Student Management System", fg="#06a099", width=35)
topLabel.config(font=("Sylfaen", 30))
topLabel.grid(row=0, column=1,columnspan=7, padx=(10,10), pady=(30, 0))
usrLabel = tk.Label(admin, text="Enter your name: ", width=40, anchor='w',
        font=("Sylfaen", 12)).grid(row=3, column=2, padx=(10,0),pady=(30, 0))
passLabel = tk.Label(admin, text="Enter your password: ", width=40, anchor='w',
                        font=("Sylfaen", 12)).grid(row=4, column=2, padx=(10,0),pady=(30, 0))
usrEntry = tk.Entry(admin, width = 30,textvariable=usr)
usrEntry.grid(row=3, column=3, padx=(0,10), pady=(30, 20))
passEntry = tk.Entry(admin, width = 30,textvariable=passw,show="*")
passEntry.grid(row=4, column=3, padx=(0,10), pady=(30, 20))
usrEntry.delete(0,tk.END)
usrEntry.delete(0,tk.END)

subButton = tk.Button(admin, text="Submit", command=lambda: checkPass())
subButton.grid(row=9, column=3)

def mainPanel():
    admin.destroy()
    mainPage = tk.Tk()
    mainPage.title("Data Entry")
    mainPage.geometry("1920x1080")
    appLabel = tk.Label(mainPage, text="Student Management System", fg="#06a099", width=35)
    appLabel.config(font=("Sylfaen", 30))
    appLabel.grid(row=0, columnspan=2, padx=(10,10), pady=(30, 0))
    nameLabel = tk.Label(mainPage, text="Enter your name: ", width=40, anchor='w',
                        font=("Sylfaen", 12)).grid(row=1, column=0, padx=(10,0),
                                                    pady=(30, 0))
    collegeLabel = tk.Label(mainPage, text="Enter your college: ", width=40, anchor='w',
                            font=("Sylfaen", 12)).grid(row=2, column=0, padx=(10,0))
    phoneLabel = tk.Label(mainPage, text="Enter your phone number: ", width=40, anchor='w',
                        font=("Sylfaen", 12)).grid(row=3, column=0, padx=(10,0))
    addressLabel = tk.Label(mainPage, text="Enter your address: ", width=40, anchor='w',
                            font=("Sylfaen", 12)).grid(row=4, column=0, padx=(10,0))
    usnLabel = tk.Label(mainPage, text="Enter your usn: ", width=40, anchor='w',
                            font=("Sylfaen", 12)).grid(row=5, column=0, padx=(10,0))
    emailLabel = tk.Label(mainPage, text="Enter your email: ", width=40, anchor='w',
                            font=("Sylfaen", 12)).grid(row=6, column=0, padx=(10,0))

    nameEntry = tk.Entry(mainPage, width = 30)
    collegeEntry = tk.Entry(mainPage, width = 30)
    phoneEntry = tk.Entry(mainPage, width = 30)
    addressEntry = tk.Entry(mainPage, width = 30)
    usnEntry = tk.Entry(mainPage, width = 30)
    emailEntry = tk.Entry(mainPage, width = 30)

    nameEntry.grid(row=1, column=1, padx=(0,10), pady=(30, 20))
    collegeEntry.grid(row=2, column=1, padx=(0,10), pady = 20)
    phoneEntry.grid(row=3, column=1, padx=(0,10), pady = 20)
    addressEntry.grid(row=4, column=1, padx=(0,10), pady = 20)
    usnEntry.grid(row=5, column=1, padx=(0,10), pady = 20)
    emailEntry.grid(row=6, column=1, padx=(0,10), pady = 20)
    button = tk.Button(mainPage, text="Take input", command=lambda :takeNameInput(nameEntry,collegeEntry,addressEntry,phoneEntry,usnEntry,emailEntry))
    button.grid(row=9, column=0, pady=30)

    displayButton = tk.Button(mainPage, text="Display result", command=lambda : displayResultWindow())
    displayButton.grid(row=9, column=1)

    delButton = tk.Button(mainPage, text="Delete", command=lambda : delPage())
    delButton.grid(row=9, column=2)

    mainPage.mainloop()


def checkPass():
    user = usr.get()
    passwrd = passw.get()
    if user == "admin" and passwrd == "admin123":
        mainPanel()
    else:
        messagebox.showinfo("Login Failed","Invalid username or password")


def takeNameInput(nameEntry,collegeEntry,addressEntry,phoneEntry,usnEntry,emailEntry):
    # global username, collegeName, phone, address
    global TABLE_NAME, STUDENT_NAME, STUDENT_COLLEGE, STUDENT_ADDRESS, STUDENT_PHONE,STUDENT_EMAIL,STUDENT_USN
    username = nameEntry.get()
    nameEntry.delete(0, tk.END)
    collegeName = collegeEntry.get()
    collegeEntry.delete(0, tk.END)
    phone = int(phoneEntry.get())
    phoneEntry.delete(0, tk.END)
    address = addressEntry.get()
    addressEntry.delete(0, tk.END)
    usn = usnEntry.get()
    usnEntry.delete(0,tk.END)
    email = emailEntry.get()
    emailEntry.delete(0,tk.END)
    cursor.execute("INSERT INTO " + TABLE_NAME + " ( " + STUDENT_USN + ", " + STUDENT_NAME + ", "
                       +STUDENT_COLLEGE + ", " + STUDENT_ADDRESS + ", " +
                       STUDENT_PHONE + ", "  + STUDENT_EMAIL+ " ) VALUES ( '" + usn + "', '"
                       + username + "', '" + collegeName + "', '" +
                       address + "', " + str(phone) + " , '" + email + "'); ")
    connection.commit()
    messagebox.showinfo("Success", "Data Saved Successfully.")

def deleteRecord(deletePage,usn_entry):
    del_usn = usn_entry.get()
    cursor.execute("DELETE FROM student_table WHERE student_usn='"+ del_usn +"';")
    connection.commit()
    deletePage.destroy()
    messagebox.showinfo("Success","Record deleted successfully.")

def delPage():
    deletePage = tk.Tk()
    deletePage.title("Delete record")
    deletePage.geometry("1920x1080")
    appLabel = tk.Label(deletePage, text="Delete Records",
                        fg="#06a099", width=40)
    appLabel.config(font=("Sylfaen", 30))
    appLabel.grid(row=0)
    
    delLabel = tk.Label(deletePage, text="Enter usn of record to be deleted: ",
                        fg="#06a099", width=40)
    delLabel.config(font=("Sylfaen", 30))
    delLabel.grid(row=5)

    usn = StringVar()
    usnEntry = tk.Entry(deletePage, textvariable=usn,width = 30)
    usnEntry.grid(row=5, column=4, padx=(0,10), pady=(30, 20))
    usnEntry.delete(0,tk.END)
    delButton = tk.Button(deletePage, text="Delete", command=lambda : deleteRecord(deletePage,usnEntry))
    delButton.grid(row=8, column=4)
    deletePage.mainloop()

def displayResultWindow():
    secondWindow = tk.Tk()

    secondWindow.title("Display results")
    secondWindow.geometry("1920x1080")
    appLabel = tk.Label(secondWindow, text="Student Management System",
                        fg="#06a099", width=40)
    appLabel.config(font=("Sylfaen", 30))
    appLabel.pack()

    tree = ttk.Treeview(secondWindow)
    tree["columns"] = ("one", "two", "three", "four" , "five" , "six")

    tree.heading("one", text="Student USN")
    tree.heading("two", text="Student Name")
    tree.heading("three", text="College Name")
    tree.heading("four", text="Address")
    tree.heading("five", text="Phone Number")
    tree.heading("six", text="Email")
    
    cursor = connection.execute("SELECT * FROM " + TABLE_NAME + " ;")
    i = 0

    for row in cursor:
        tree.insert('', i,text =str(i+1),
                            values=(row[0], row[1],
                            row[2], row[3],
                            row[4], row[5]))
        i = i + 1

    tree.pack()
    secondWindow.mainloop()

admin.mainloop()