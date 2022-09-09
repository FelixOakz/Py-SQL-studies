# importing essential GUI, database and popup message tools
from tkinter import *
from tkinter import messagebox
import mysql.connector


# WHOLE LOGIC AND FUNCTIONING BACKEND:

# INSERT METHOD: read data provided by user
def insertData():
    id = enterId.get()
    name = enterName.get()
    dept = enterDept.get()

# data validation for a warning message If empty data is provided by user
    if(id =="" or name =="" or dept ==""):
# different type of message box: showwarning
        messagebox.showwarning("Cannot Insert", "All the fields required!")
    else:
# accessing database
        myDB = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="timemachine",
            database="employee")
# inserting data in the empDetails table
        myCur = myDB.cursor()
        myCur.execute("insert into empDetails values('"+ id +"','"+ name +"','"+ dept +"') ")
        myDB.commit()
# once inserted we clear the data from entry field using delete() method
        enterId.delete(0, "end")
        enterName.delete(0, "end")
        enterDept.delete(0, "end",)
        show()
# different type of message box: showinfo
        messagebox.showinfo("Insert Status:", "Data Inserted Sucesfully!")
        myDB.close()


# UPDATE METHOD: read data provided by user





# WHOLE GUI CODE:

#creating parent window at the required size with the right label
window = Tk()
window.geometry("700x400")
window.title("Employee CRUD App")

# creating all labels
empId = Label(window, text="Employee ID", font=("Serif", 12))
empId.place(x=20, y=30)

empName = Label(window, text="Employee Name", font=("Serif", 12))
empName.place(x=20, y=60)

empDept = Label(window, text="Employee Dept", font=("Serif", 12))
empDept.place(x=20, y=90)

#creating entry fields to respective labels
enterId = Entry(window)
enterId.place(x=170, y=30)

enterName = Entry(window)
enterName.place(x=170, y=60)

enterDept = Entry(window)
enterDept.place(x=170, y=90)

#adding buttons to perform CRUD operations and a reset button

#Using the command option we specify the method that will be called when clicked
insertBtn = Button(window, text="Insert", font=(
    "Sans", 11), bg="white", command=insertData) # will interact with specific method
insertBtn.place(x=20, y=160)

updateBtn = Button(window, text="Update", font=(
    "Sans", 11), bg="white", command=updateData) # will interact with specific method
updateBtn.place(x=80, y=160)

getBtn = Button(window, text="Fetch", font=(
    "Sans", 11), bg="white", command=getData) # will interact with specific method
getBtn.place(x=150, y=160)

deleteBtn = Button(window, text="Delete", font=(
    "Sans", 11), bg="white", command=deleteData) # will interact with specific method
deleteBtn.place(x=210, y=160)

resetBtn = Button(window, text="Reset", font=(
    "Sans", 11), bg="white", command=resetFields) # will interact with specific method
resetBtn.place(x=20, y=210)

# final listbox widget, it will show the database table
showData = Listbox(window)
showData.place(x=330, y=30)
show()

#loop till and event
window.mainloop()

