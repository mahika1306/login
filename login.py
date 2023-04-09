from tkinter import *
from tkinter import messagebox

def login():
    username=entry1.get()
    password=entry2.get()

    if(username=='Admin'and password=="test123"):
        messagebox.showinfo("","Login successful")
    elif(username==''and password==''):
        messagebox.showwarning("Warning","Field is empty!")
    else:
        messagebox.showerror("Error","Invalid username or password")
    



window=Tk()
window.title("Login Form")
window.geometry("350x200")
global entry1
global entry2
'''label=Label(window,text="Login",font=("Times New Roman",20))
label.pack(side="top")'''
userlabel=Label(window,text="Username",font=("Times New Roman",15)).place(x=20,y=40)
passlabel=Label(window,text="Password",font=("Times New Roman",15)).place(x=20,y=100)
entry1=Entry(window,bd=3)
entry1.place(x=140,y=40)

entry2=Entry(window,bd=3,show='*')
entry2.place(x=140,y=100)

button=Button(text="Submit",font=('times',10),bd=3,command=login)
button.place(x=130,y=159)
frame=Frame(window)
frame.pack()

window.mainloop()

