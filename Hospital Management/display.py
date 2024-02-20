from tkinter import *
import sqlite3
import pyttsx3

# connection to database 
conn = sqlite3.connect('database1.db')
c = conn.cursor()

#empty list to apply later
number = []
patients = []

sql = "SELECT * FROM appointments"
res = c.execute(sql)
for r in res:
    ids = r[0]
    name = r[1]
    number.append(ids)
    patients.append(name)

#window 
class Application:
    def __init__(self, master):
        self.master = master

        self.x = 0
        #heading
        self.heading = Label(master, text="Appointments", font=('arial 100 bold'))
        self.heading.place(x=350, y=0)

        #button to change patients
        self.change = Button(master, text="Next Patient", width=25, height=2, bg='green', command= self.func)
        self.change.place(x=530, y=600)

        #empty text label to later config
        self.n = Label(master, text=str(number[self.x]), fg='black', bg='white' ,font=('arial 200 bold'))
        self.n.place(x=540, y=100)

        self.pname = Label(master, text=str(patients[self.x]),fg='black', bg='white', font=('arial 80 bold'))
        self.pname.place(x=380, y=400)

    #function to speak the text and update the text
    def func(self):
        self.n.config(text=str(number[self.x]))
        self.pname.config(text=str(patients[self.x]))
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        rate = engine.getProperty('rate')
        engine.setProperty('rate', rate-50)
        engine.say('Patient number ' + str(number[self.x]) + str(patients[self.x]))
        engine.runAndWait()
        self.x += 1

root = Tk()
b = Application(root)
root.geometry("1366x768+0+0")
root.resizable(False, False)
root.mainloop()


