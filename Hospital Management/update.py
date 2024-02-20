# update the appointments 
from tkinter import *
import tkinter.messagebox
import sqlite3

conn = sqlite3.connect('database1.db')
c = conn.cursor()

class Application:
    def __init__(self, master):
        self.master = master
        # heading label
        self.heading = Label(master, text="Update Appointments", fg='steelblue', font=('arial 40 bold'))
        self.heading.place(x=150, y=0)

        #search criteria  --> name
        self.name = Label(master, text="Enter Patient's Name", font=('arial 18 bold'))
        self.name.place(x=0, y=60)

        #entry for the name
        self.namenet = Entry(master, width=30)
        self.namenet.place(x=280,y =62)

        #search button
        self.search = Button(master, text="Search", width=12, height=1, bg="steelblue", command=self.search_db)
        self.search.place(x=350, y=102)

    # funtcion to search
    def search_db(self):
        self.input = self.namenet.get()
        # execute sql 

        sql = "SELECT * FROM appointments WHERE name LIKE ?"
        self.res = c.execute(sql, (self.input,))
        for self.row in self.res:
            self.name1 = self.row[1]
            self.age = self.row[2]
            self.gender = self.row[3]
            self.location = self.row[4]
            self.phone = self.row[5]
            self.time1 = self.row[6]
        # creating the update form
        self.uname = Label(self.master, text="Patient's Name", font=('arial 18 bold'))
        self.uname.place(x=0, y=140)   

        self.uage = Label(self.master, text="Age", font=('arial 18 bold'))
        self.uage.place(x=0, y=180) 

        self.ugender = Label(self.master, text="Gender", font=('arial 18 bold'))
        self.ugender.place(x=0, y=220) 

        self.ulocation = Label(self.master, text="Location", font=('arial 18 bold'))
        self.ulocation.place(x=0, y=260) 

        self.uphone = Label(self.master, text="Phone No.", font=('arial 18 bold'))
        self.uphone.place(x=0, y=300) 

        self.utime1 = Label(self.master, text="Appointment's Time", font=('arial 18 bold'))
        self.utime1.place(x=0, y=340) 

        #entries for the labelszzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz
        #========================filling the search result in the entry box to update
        self.ent1 = Entry(self.master, width=30)
        self.ent1.place(x=300, y=140)
        self.ent1.insert(END, str(self.name1))  

        self.ent2 = Entry(self.master, width=30)
        self.ent2.place(x=300, y=180) 
        self.ent2.insert(END, str(self.age)) 

        self.ent3 = Entry(self.master, width=30)
        self.ent3.place(x=300, y=220) 
        self.ent3.insert(END, str(self.gender)) 

        self.ent4 = Entry(self.master, width=30)
        self.ent4.place(x=300, y=260) 
        self.ent4.insert(END, str(self.location)) 

        self.ent5 = Entry(self.master, width=30)
        self.ent5.place(x=300, y=300) 
        self.ent5.insert(END, str(self.phone)) 

        self.ent6 = Entry(self.master, width=30)
        self.ent6.place(x=300, y=340) 
        self.ent6.insert(END, str(self.time1)) 

        # button to execute the update page
        self.update = Button(self.master, text="Update", width=20, height=2, bg="lightblue")
        self.update.place(x=400, y=380)
# creating the object
root = Tk()
b = Application(root)
root.geometry("1200x720+0+0")
root.resizable(False, False)
root.mainloop()
