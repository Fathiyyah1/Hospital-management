#import  modules
import re
from tkinter import *
import sqlite3
import tkinter.messagebox

# connect to the database 
conn = sqlite3.connect('database1.db')
#cursor to move around the database 
c = conn.cursor()

# empty list to later append the ids from the database
ids = []

# tkinter window
class application:
    def __init__(self, master):
        self.master = master

        #creating the frames in the master
        self.left = Frame(master, width=800, height=720, bg = 'lightgreen')
        self.left.pack(side=LEFT)

        self.right = Frame(master, width= 400, height= 720, bg='steelblue')
        self.right.pack(side=RIGHT)

        # Labels for the window
        self.heading = Label(self.left, text = "AL-Hamdan Hospital Appointments", font=('arial 40 bold'), fg = 'black', bg='lightgreen')
        self.heading.place(x = 0, y = 0)
        #patient name
        self.name = Label(self.left, text= "Patient's Name", font=('arial 18 bold'), fg = 'black', bg = 'lightgreen')
        self.name.place(x=0, y=100)
        #patient age
        self.age = Label(self.left, text= "Age", font=('arial 18 bold'), fg = 'black', bg = 'lightgreen')
        self.age.place(x=0, y=140)
        #patient gender
        self.gender = Label(self.left, text= "Gender", font=('arial 18 bold'), fg = 'black', bg = 'lightgreen')
        self.gender.place(x=0, y=180)
        #patient location
        self.location = Label(self.left, text= "Location", font=('arial 18 bold'), fg = 'black', bg = 'lightgreen')
        self.location.place(x=0, y=220)
        #appiontment time
        self.time = Label(self.left, text= "Appiontment's Time", font=('arial 18 bold'), fg = 'black', bg = 'lightgreen')
        self.time.place(x=0, y=260)

        #phone number
        self.phone = Label(self.left, text= "Phone Number", font=('arial 18 bold'), fg = 'black', bg = 'lightgreen')
        self.phone.place(x=0, y=300)


        #Entries  or textfields for all labelszzzzzzzzzzzzzzzzzzzzzzzzzzzz
        self.name_ent = Entry(self.left, width=30)
        self.name_ent.place(x=250,y=100)

        self.age_ent = Entry(self.left, width=30)
        self.age_ent.place(x=250,y=140)

        self.gender_ent = Entry(self.left, width=30)
        self.gender_ent.place(x=250,y=180)

        self.location_ent = Entry(self.left, width=30)
        self.location_ent.place(x=250,y=220)

        self.time_ent = Entry(self.left, width=30)
        self.time_ent.place(x=250,y=260)

        self.phone_ent = Entry(self.left, width = 30)
        self.phone_ent.place(x=250, y=300)

        #button for perform and command 
        self.submit= Button(self.left, text="Add Appointment", width=20, height=2, bg='steelblue', command=self.add_appointment)
        self.submit.place(x=300, y=340)

        #getting the number of appointments fixed to view in th log
        sql2 = "SELECT ID FROM appointments "
        self.result = c.execute(sql2)
        for self.row in self.result:
            self.id = self.row[0]
            ids.append(self.id)

            # ordering the ids 
        self.new = sorted(ids)
        self.final_id = self.new[len(ids)-1]   

        # displaying the logs in our right frame
        self.logs = Label(self.right, text="Logs", font=('arial 28 bold'), fg ='white', bg='steelblue')
        self.logs.place(x=0, y=0)

        self.box = Text(self.right, width=50, height=40)
        self.box.place(x=20, y=60)
        self.box.insert(END, "Total Appointments till now:  "+ str(self.final_id))
    # funtion to call when the submit button is clicked
    def add_appointment(self):
        # getting the user inputs 
        self.val1 = self.name_ent.get()
        self.val2 = self.age_ent.get()
        self.val3 = self.gender_ent.get()
        self.val4 = self.location_ent.get()
        self.val5 = self.phone_ent.get()
        self.val6 = self.time_ent.get()
        

 # testig the user inputs#print(self.val1) 
        # checkinbg if the user input is empty
        if self.val1 == '' or self.val2 == '' or self.val3 == '' or self.val4 == '' or self.val5 == '' or self.val6 == '':
            tkinter.messagebox.showinfo("Warning", "please, fill up all the boxes")      
        else:
            # now we add to the database
            sql = "INSERT INTO 'appointments' (name, age, gender, location, phone, scheduled) VALUES(?, ?, ?, ?, ?, ?)"
            c.execute(sql, (self.val1, self.val2, self.val3, self.val4, self.val5, self.val6))
            conn.commit()
            tkinter.messagebox.showinfo("Success", " An Appointment for " +str(self.val1) + " has been created.")
               
            self.box.insert(END, '\n An Appointment fixed for '+ str(self.val1) + ' at ' + str(self.val6))

# create the object 
root = Tk()
b = application(root)

# resolution of the window 
root.geometry("1200x720+0+0")

# preventing the resize feature
root.resizable(False, False)

# end the loop
root.mainloop()

