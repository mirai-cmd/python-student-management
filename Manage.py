from tkinter import StringVar, ttk, messagebox
from util.helpers import addNewUser,deleteUser
import tkinter as tk
import sqlite3
import bcrypt

main = tk.Tk()
main.title("Admin Panel")
main.geometry("1920x1080")
connection = sqlite3.connect("sqlite-tools-win32-x86-3430100\manage.db")
cursor = connection.cursor()


TABLE_NAME = "student_table"
STUDENT_USN = "student_usn"
STUDENT_NAME = "student_name"
STUDENT_COLLEGE = "student_college"
STUDENT_ADDRESS = "student_address"
STUDENT_PHONE = "student_phone"
STUDENT_EMAIL = "student_email"


global usr, passw
usr = StringVar()
passw = StringVar()
topLabel = tk.Label(
    main, text="Welcome to Student Management System", fg="#06a099", width=35
)
topLabel.config(font=("Sylfaen", 30))
topLabel.grid(row=0, column=1, columnspan=7, padx=(10, 10), pady=(30, 0))
usrLabel = tk.Label(
    main, text="Enter your username: ", width=40, anchor="w", font=("Sylfaen", 12)
).grid(row=3, column=2, padx=(10, 0), pady=(30, 0))
passLabel = tk.Label(
    main, text="Enter your password: ", width=40, anchor="w", font=("Sylfaen", 12)
).grid(row=4, column=2, padx=(10, 0), pady=(30, 0))
usrEntry = tk.Entry(main, width=30, textvariable=usr)
usrEntry.grid(row=3, column=3, padx=(0, 10), pady=(30, 20))
passEntry = tk.Entry(main, width=30, textvariable=passw, show="*")
passEntry.grid(row=4, column=3, padx=(0, 10), pady=(30, 20))
usrEntry.delete(0, tk.END)
usrEntry.delete(0, tk.END)

subButton = tk.Button(main, text="Submit", command=lambda: checkPass())
subButton.grid(row=9, column=3)
adminToggleButton = tk.Button(
    main, text="Admin Options", command=lambda: toggleAdminControlPanel()
)
adminToggleButton.grid(row=9, column=4)


def mainPanel():
    main.destroy()
    inputPanel = tk.Tk()
    inputPanel.title("Data Entry")
    inputPanel.geometry("1920x1080")
    appLabel = tk.Label(
        inputPanel, text="Student Management System", fg="#06a099", width=35
    )
    appLabel.config(font=("Sylfaen", 30))
    appLabel.grid(row=0, columnspan=2, padx=(10, 10), pady=(30, 0))
    nameLabel = tk.Label(
        inputPanel, text="Enter your name: ", width=40, anchor="w", font=("Sylfaen", 12)
    ).grid(row=1, column=0, padx=(10, 0), pady=(30, 0))
    collegeLabel = tk.Label(
        inputPanel,
        text="Enter your college: ",
        width=40,
        anchor="w",
        font=("Sylfaen", 12),
    ).grid(row=2, column=0, padx=(10, 0))
    phoneLabel = tk.Label(
        inputPanel,
        text="Enter your phone number: ",
        width=40,
        anchor="w",
        font=("Sylfaen", 12),
    ).grid(row=3, column=0, padx=(10, 0))
    addressLabel = tk.Label(
        inputPanel,
        text="Enter your address: ",
        width=40,
        anchor="w",
        font=("Sylfaen", 12),
    ).grid(row=4, column=0, padx=(10, 0))
    usnLabel = tk.Label(
        inputPanel, text="Enter your usn: ", width=40, anchor="w", font=("Sylfaen", 12)
    ).grid(row=5, column=0, padx=(10, 0))
    emailLabel = tk.Label(
        inputPanel,
        text="Enter your email: ",
        width=40,
        anchor="w",
        font=("Sylfaen", 12),
    ).grid(row=6, column=0, padx=(10, 0))

    nameEntry = tk.Entry(inputPanel, width=30)
    collegeEntry = tk.Entry(inputPanel, width=30)
    phoneEntry = tk.Entry(inputPanel, width=30)
    addressEntry = tk.Entry(inputPanel, width=30)
    usnEntry = tk.Entry(inputPanel, width=30)
    emailEntry = tk.Entry(inputPanel, width=30)

    nameEntry.grid(row=1, column=1, padx=(0, 10), pady=(30, 20))
    collegeEntry.grid(row=2, column=1, padx=(0, 10), pady=20)
    phoneEntry.grid(row=3, column=1, padx=(0, 10), pady=20)
    addressEntry.grid(row=4, column=1, padx=(0, 10), pady=20)
    usnEntry.grid(row=5, column=1, padx=(0, 10), pady=20)
    emailEntry.grid(row=6, column=1, padx=(0, 10), pady=20)
    button = tk.Button(
        inputPanel,
        text="Save Details",
        command=lambda: saveInputDetails(
            nameEntry, collegeEntry, addressEntry, phoneEntry, usnEntry, emailEntry
        ),
    )
    button.grid(row=9, column=0, pady=30)

    displayButton = tk.Button(
        inputPanel, text="Display result", command=lambda: displayResultWindow()
    )
    displayButton.grid(row=9, column=1)

    delButton = tk.Button(inputPanel, text="Delete", command=lambda: delPage())
    delButton.grid(row=9, column=2)

    inputPanel.mainloop()

def saveInputDetails(
    nameEntry, collegeEntry, addressEntry, phoneEntry, usnEntry, emailEntry
):
    # global username, collegeName, phone, address
    global TABLE_NAME, STUDENT_NAME, STUDENT_COLLEGE, STUDENT_ADDRESS, STUDENT_PHONE, STUDENT_EMAIL, STUDENT_USN
    username = nameEntry.get()
    nameEntry.delete(0, tk.END)
    collegeName = collegeEntry.get()
    collegeEntry.delete(0, tk.END)
    phone = int(phoneEntry.get())
    phoneEntry.delete(0, tk.END)
    address = addressEntry.get()
    addressEntry.delete(0, tk.END)
    usn = usnEntry.get()
    usnEntry.delete(0, tk.END)
    email = emailEntry.get()
    emailEntry.delete(0, tk.END)
    cursor.execute(
        "INSERT INTO "
        + TABLE_NAME
        + " ( "
        + STUDENT_USN
        + ", "
        + STUDENT_NAME
        + ", "
        + STUDENT_COLLEGE
        + ", "
        + STUDENT_ADDRESS
        + ", "
        + STUDENT_PHONE
        + ", "
        + STUDENT_EMAIL
        + " ) VALUES ( '"
        + usn
        + "', '"
        + username
        + "', '"
        + collegeName
        + "', '"
        + address
        + "', "
        + str(phone)
        + " , '"
        + email
        + "'); "
    )
    connection.commit()
    messagebox.showinfo("Success", "Data Saved Successfully.")


def deleteRecord(editPage, usn_entry):
    del_usn = usn_entry.get()
    cursor.execute("DELETE FROM student_table WHERE student_usn='" + del_usn + "';")
    connection.commit()
    editPage.destroy()
    messagebox.showinfo("Success", "Record deleted successfully.")


def delPage():
    editPage = tk.Tk()
    editPage.title("Delete record")
    editPage.geometry("1920x1080")
    appLabel = tk.Label(editPage, text="Delete Records", fg="#06a099", width=40)
    appLabel.config(font=("Sylfaen", 30))
    appLabel.grid(row=0)

    delLabel = tk.Label(
        editPage, text="Enter usn of record to be deleted: ", fg="#06a099", width=40
    )
    delLabel.config(font=("Sylfaen", 30))
    delLabel.grid(row=5)

    usn = StringVar()
    usnEntry = tk.Entry(editPage, textvariable=usn, width=30)
    usnEntry.grid(row=5, column=4, padx=(0, 10), pady=(30, 20))
    usnEntry.delete(0, tk.END)
    delButton = tk.Button(
        editPage, text="Delete", command=lambda: deleteRecord(editPage, usnEntry)
    )
    delButton.grid(row=8, column=4)
    editPage.mainloop()


def displayResultWindow():
    resultPanel = tk.Tk()

    resultPanel.title("Display results")
    resultPanel.geometry("1920x1080")
    appLabel = tk.Label(
        resultPanel, text="Student Management System", fg="#06a099", width=40
    )
    appLabel.config(font=("Sylfaen", 30))
    appLabel.pack()

    tree = ttk.Treeview(resultPanel)
    tree["columns"] = ("one", "two", "three", "four", "five", "six")

    tree.heading("one", text="Student USN")
    tree.heading("two", text="Student Name")
    tree.heading("three", text="College Name")
    tree.heading("four", text="Address")
    tree.heading("five", text="Phone Number")
    tree.heading("six", text="Email")

    cursor = connection.execute("SELECT * FROM " + TABLE_NAME + " ;")
    i = 0
    for row in cursor:
        tree.insert(
            "",
            i,
            text=str(i + 1),
            values=(row[0], row[1], row[2], row[3], row[4], row[5]),
        )
        i = i + 1

    tree.pack()
    resultPanel.mainloop()

def displayUsers(admin):
    # Treeview to display records
    tree = ttk.Treeview(admin)
    # To suppress default empty first column from view
    tree["show"] = "headings"
    tree["columns"] = ("one", "two")
    tree.heading("one", text="Uid")
    tree.heading("two", text="Username")
    cursor = connection.execute(f"SELECT uid,username FROM users;")
    i = 0
    for row in cursor:
        tree.insert("", i, values=(row[0], row[1]))
        i += 1
    tree.grid(row=15,column=1)

def checkPass():
    user = usr.get()
    passwrd = passw.get()
    cursor = connection.execute(
        f"SELECT username,password FROM users WHERE username='{user}';"
    )
    userData = cursor.fetchone()
    if user == userData[0] and bcrypt.checkpw(passwrd.encode(),userData[1].encode()):
        mainPanel()
    else:
        messagebox.showinfo("Login Failed", "Invalid username or password")

def toggleAdminControlPanel():
    admin = tk.Tk()
    admin.title("Admin Control")
    admin.geometry("1200x800")
    panelLabel = tk.Label(admin, text="Admin Panel", fg="#06a099", width=35)
    panelLabel.config(font=("Sylfaen", 30))
    panelLabel.grid(row=0, columnspan=2, padx=(10, 10), pady=(30, 0))
    displayUsers(admin)
    refreshButton = tk.Button(admin, text="Refresh Records", command=lambda: displayUsers(admin))
    refreshButton.grid(row=14, column=6)
    newUserButton = tk.Button(admin, text="Add a new User", command=lambda: addNewUser(connection))
    newUserButton.grid(row=15, column=6)
    delUserButton = tk.Button(admin, text="Delete a User", command=lambda: deleteUser(connection))
    delUserButton.grid(row=16, column=6)
    admin.mainloop()

main.mainloop()
#testing branch protection
