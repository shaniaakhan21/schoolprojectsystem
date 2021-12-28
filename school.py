from tkinter import *
import tkinter.messagebox
import sqlite3

class Student:
    def __init__(self,window):

        def login_response():
            try:
                connection = sqlite3.connect("register.db")
                con = connection.cursor()
                for row in con.execute("Select * from teachers_data"):
                    username = row[2]
                    password = row[3]
            except Exception as ep:
                tkinter.messagebox.showerror('',ep)
            
            uname = username_textbox.get()
            userpassword = password_textbox.get()
            check_counter = 0
            if uname == "":
                warn = "Username can't be empty"
            else:
                check_counter += 1
            if userpassword == "":
                warn = "Passowrd can't be empty"
            else:
                check_counter +=1
            if check_counter == 2:
                if (uname == username and userpassword == password):
                    
                    tkinter.messagebox.showinfo('Login Successful', 'Logged in successfully!')

                else:
                    tkinter.messagebox.showerror('Login Status', 'invalid username or password')
            else:
                tkinter.messagebox.showerror('',warn)

        self.window = window #instance variable for a window
        self.window.title("School Management System.")
        self.window.geometry("1500x700+1+0")
        title = Label(self.window,text ="School Management System",font = ("times new roman",50,"bold"),bg="White",fg="Red")
        title.pack(side=TOP,fill = X) #x-axis if for horizontal direction and y-axis is for vertical direction. 

        Manage_frame = Frame(self.window, bd=4, relief=RIDGE, bg="gray")
        Manage_frame.place(x=450,y=160, width = 500, height= 400)

        username_label = Label(Manage_frame,text="Username", font=("times new roman",25, "bold"),bg="gray")
        username_label.grid(row=0, columnspan=2, pady=50)

        password_label = Label(Manage_frame, text="Password",font=("times new roman",25, "bold"),bg="gray")
        password_label.grid(row=1,column=0,pady=10)
        
        username = StringVar()
        username_textbox = Entry (textvariable=username, width="50")
        username_textbox.place(x = 620,y =220, width=300, height=30)

        password = StringVar()
        password_textbox = Entry(textvariable=password,width="50")
        password_textbox.place(x=620,y=320, width=300, height=30)
      
        Login_btn = Button(text="login",fg="black", bg="white" ,font=("times new roman",15,"italic"),command=login_response)
        Login_btn.place(x=620,y=400, width=100,height=50)

        def Register():
            newWindow = Toplevel(window)
            newWindow.title("Register Here")
            newWindow.geometry("700x500") 
            firstname_label = Label(newWindow, text="First Name",font=("times new roman",20,"bold"))
            lastname_label =  Label(newWindow, text="Last Name",font=("times new roman",20,"bold"))
            username_label = Label(newWindow,text="Username",font=("times new roman",20,"bold"))
            password_label = Label(newWindow,text="Password",font=("times new roman",20,"bold"))
            gender_label = Label(newWindow, text="Gender",font=("times new roman",20,"bold"))
            phonenumber_label = Label(newWindow, text="Phone Number",font=("times new roman",20,"bold"))
            email_label = Label(newWindow,text="Email",font=("times new roman",20,"bold"))
            firstname_label.place(x=100 , y=60)
            lastname_label.place(x=100 , y=90)
            username_label.place(x=100,y=120)
            password_label.place(x=100,y=150)
            gender_label.place( x=100, y=180)
            phonenumber_label.place(x=100 , y=210)
            email_label.place(x=100 , y=240)
       
            firstname = StringVar()
            Firstname_entry = Entry(newWindow,textvariable= firstname,width ="25")
            Firstname_entry.place(x=300,y=70)

            lastname = StringVar()
            Lastname_entry = Entry(newWindow,textvariable=lastname,width ="25")
            Lastname_entry.place(x=300,y=100)
             
            username = StringVar()
            Username_entry = Entry(newWindow,textvariable=username,width ="25")
            Username_entry.place(x=300,y=130)          
            
            password = StringVar()
            Password_entry = Entry(newWindow,show="*",textvariable=password,width ="25")
            Password_entry.place(x=300,y=160)
           
            gender = StringVar()
            Gender_entry = Entry(newWindow,textvariable=gender, width ="25" )
            Gender_entry.place(x=300,y=190)

            phonenumber = StringVar()
            Phonenumber_entry = Entry(newWindow,textvariable=phonenumber, width ="25" )
            Phonenumber_entry.place(x=300,y=220)

            email = StringVar()
            Email_entry = Entry(newWindow,textvariable=email, width ="25" )
            Email_entry.place(x=300,y=250)

            def oneclick():
                tkinter.messagebox.showinfo("Registered","Registered successfully, Please login .")
                firstname_info=firstname.get()
                lastname_info=lastname.get()
                username_info=username.get()
                password_info=password.get()
                gender_info=gender.get()
                phonenumber_info=phonenumber.get()
                email_info=email.get()
           
                connection=sqlite3.connect("register.db")
                connection.execute(" CREATE TABLE IF NOT EXISTS teachers_data (FirstName Text,LastName Text, Username Text, Password Text, Gender Text, PhoneNumber INT, Email Text)")
                connection.execute('INSERT INTO teachers_data (FirstName, LastName, Username, Password ,Gender, PhoneNumber, Email) VALUES(?,?,?,?,?,?,?)', (firstname_info, lastname_info, username_info, password_info,  gender_info, phonenumber_info, email_info))
                connection.commit()
            Registration_btn = Button(newWindow,text="Register",fg="black",bg="white",font=("times new roman", 15,"italic"),command=oneclick)
            Registration_btn.place(x=300,y=280,width=100,height=50)


        Register_btn = Button(text="Register",fg="black",bg="white",font=("times new roman", 15,"italic"),command=Register)  
        Register_btn.place(x=750,y=400,width=100,height=50)


window = Tk()
obj = Student(window)
window.mainloop()