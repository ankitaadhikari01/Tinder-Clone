from tkinter import*
from PIL import Image,ImageTk
from tkinter import messagebox


class GUI:
    def __init__(self,f,g):
        # create a login window
        self._root=Tk()

        self._root.minsize(400,800)
        self._root.maxsize(400,800)
        self._root.configure(background="#F5083A")

        self._label1=Label(self._root,text="Tinder")
        self._label1.configure(font=("Constantia",22,"bold"))
        self._label1.pack(pady=(30,30))

        self._label2=Label(self._root,text="Email : ")
        self._label2.configure(font=("Constantia",13))
        self._label2.pack(pady=(5,5))

        self._emailInput=Entry(self._root)
        self._emailInput.pack(pady=(0,20),ipady=7,ipadx=30)

        self._label3 = Label(self._root, text="Password : ")
        self._label3.configure(font=("Constantia", 13))
        self._label3.pack(pady=(5, 5))

        self._passwordInput = Entry(self._root)
        self._passwordInput.pack(pady=(0, 10), ipady=7, ipadx=30)

        self._loginBtn = Button(self._root, text="Login", width=30, height=2,command=lambda: f(self._emailInput.get(),self._passwordInput.get()))
        self._loginBtn.pack()

        self._label4 = Label(self._root, text="Not a Member? ")
        self._label4.configure(font=("Constantia", 13))
        self._label4.pack(pady=(10, 5))

        self._regBtn = Button(self._root, text="Click Here", width=10,command=lambda: self.regWindow(g))
        self._regBtn.pack()

        self._root.mainloop()

    def regWindow(self,g):
        self._root=Tk()

        self._root.minsize(400, 800)
        self._root.maxsize(400, 800)
        self._root.configure(background="#F5083A")

        self._label1 = Label(self._root, text="Tinder")
        self._label1.configure(font=("Constantia", 22, "bold"))
        self._label1.pack(pady=(30, 30))

        self._label2 = Label(self._root, text="Name : ")
        self._label2.configure(font=("Constantia", 13))
        self._label2.pack(pady=(5, 5))

        self._nameInput = Entry(self._root)
        self._nameInput.pack(pady=(0, 20), ipady=7, ipadx=30)

        self._label3 = Label(self._root, text="Email : ")
        self._label3.configure(font=("Constantia", 13))
        self._label3.pack(pady=(5, 5))

        self._emailInput = Entry(self._root)
        self._emailInput.pack(pady=(0, 20), ipady=7, ipadx=30)

        self._label4 = Label(self._root, text="Password : ")
        self._label4.configure(font=("Constantia", 13))
        self._label4.pack(pady=(5, 5))

        self._passwordInput = Entry(self._root)
        self._passwordInput.pack(pady=(0, 20), ipady=7, ipadx=30)


        self._ageInput = Entry(self._root)
        self._ageInput.pack(pady=(0, 20), ipady=7, ipadx=30)
        self._ageInput.insert(0, "Age")


        self._genderInput = Entry(self._root)
        self._genderInput.insert(0,"Gender")
        self._genderInput.pack(pady=(0, 20), ipady=7, ipadx=30)


        self._cityInput = Entry(self._root)
        self._cityInput.insert(0, "City")
        self._cityInput.pack(pady=(0, 20), ipady=7, ipadx=30)

        self._bioInput = Entry(self._root)
        self._bioInput.insert(0, "Bio")
        self._bioInput.pack(pady=(0, 20), ipady=7, ipadx=30)

        self._registerBtn = Button(self._root, text="Login", width=30, height=2,command=lambda: g(self._nameInput.get(),self._emailInput.get(),self._passwordInput.get(),self._ageInput.get(),self._genderInput.get(),self._cityInput.get(),self._bioInput.get()))
        self._registerBtn.pack()
        print(self._emailInput.fetchall())
        print(self._passwordInput.get())

        self._root.mainloop()

    def clearScreen(self):
        for i in self._root.pack_slaves():
            i.destroy()

    def clearScreen1(self):
        for i in self._root.grid_slaves():
            i.destroy()

    def headerMenu(self,other,data,a,b):
        menu = Menu(self._root)
        self._root.config(menu=menu)
        filemenu = Menu(menu)
        menu.add_cascade(label="Home", menu=filemenu)
        print(data)
        filemenu.add_command(label="My Profile", command=lambda: self.mainWindow(other,data,a,b,mode=0))
        filemenu.add_command(label="Edit Profile", command=lambda: self.viewWindow(other.viewHandler,data,a,b,mode=0))
        filemenu.add_command(label="View Profile", command=lambda: other.viewUsers(a,b,0))
        filemenu.add_command(label="LogOut", command=lambda: self.logoutWindow())

        helpmenu = Menu(menu)
        menu.add_cascade(label="Proposals", menu=helpmenu)
        helpmenu.add_command(label="My Proposals", command=lambda: self.clearScreen())
        helpmenu.add_command(label="My Requests", command=lambda: self.clearScreen())
        helpmenu.add_command(label="My Matches", command=lambda: self.clearScreen())


    def mainWindow(self,other,data,a,b,mode,num=0):#other=tinder object,self=GUI object
        self.clearScreen()
        self.headerMenu(other,data,a,b)

        imageUrl="image/2.jpg"
        load = Image.open(imageUrl)
        load = load.resize((200, 200), Image.ANTIALIAS)
        render = ImageTk.PhotoImage(load)

        img = Label(image=render)
        img.image = render
        img.pack()


        self.label1=Label(self._root,text="Name : ")
        self.label1.configure(font=("Constantia",18))
        self.label1.pack()

        name=data[0][1]
        self.label2 = Label(self._root, text=name)
        self.label2.configure(font=("Constantia", 18))
        self.label2.pack()

        self.label3 = Label(self._root, text="Age : ")
        self.label3.configure(font=("Constantia", 18))
        self.label3.pack()

        age=str(data[0][4])
        self.label4 = Label(self._root, text=age)
        self.label4.configure(font=("Constantia", 18))
        self.label4.pack()

        self.label5 = Label(self._root, text="Gender : ")
        self.label5.configure(font=("Constantia", 18))
        self.label5.pack()


        gender=data[0][5]
        self.label6 = Label(self._root, text=gender)
        self.label6.configure(font=("Constantia", 18))
        self.label6.pack()

        """self.label7 = Label(self._root, text="City : ")
        self.label7.configure(font=("Constantia", 18))
        self.label7.grid(row=4, column=0)

        city=data[0][7]
        self.label7 = Label(self._root, text=city)
        self.label7.configure(font=("Constantia", 18))
        self.label7.grid(row=4, column=1)
        
        self.label8=Label(self._root,text="Bio : ")
        self.label8.configure(font=("Constantia",18))
        self.label8.grid(row=5,column=0)
        
        
        bio=data[0][8]
        self.label8 = Label(self._root, text="Cool")
        self.label8.configure(font=("Constantia", 18))
        self.label8.grid(row=5,column=1)"""

        if mode==2:
            frame = Frame(self._root)
            frame.pack()
            btn1 = Button(frame, text="Previous", fg="#fff", bg="#fd5068",command=lambda: other.viewUsers(a,b,num-1))
            btn1.pack(side=LEFT)
            btn2 = Button(frame, text="Propose", fg="#fff", bg="#fd5068",command=lambda: other.propose(data[0][0]))
            btn2.pack(side=LEFT)
            btn3 = Button(frame, text="Next", fg="#fff", bg="#fd5068",command=lambda: other.viewUsers(a,b,num+1))
            btn3.pack(side=LEFT)


    def printMessage(self,title,message):
        messagebox.showerror(title,message)

    def printMessage1(self,title,message,messageboxImage):
        messagebox._show(title,message,messageboxImage)

    """def viewWindow(self):
        self.clearScreen1()


        self.label1 = Label(self._root, text="Name : ")
        self.label1.configure(font=("Constantia", 18))
        self.label1.grid(row=1, column=0)

        #name = data[0][1]
        self.label2 = Label(self._root, text="Hello")
        self.label2.configure(font=("Constantia", 18))
        self.label2.grid(row=1, column=1)

        self.label3 = Label(self._root, text="Age : ")
        self.label3.configure(font=("Constantia", 18))
        self.label3.grid(row=2, column=0)

        #age = str(data[0][4])
        self.label4 = Label(self._root, text="22")
        self.label4.configure(font=("Constantia", 18))
        self.label4.grid(row=2, column=1)

        self.label5 = Label(self._root, text="Gender : ")
        self.label5.configure(font=("Constantia", 18))
        self.label5.grid(row=3, column=0)

        #gender = data[0][5]
        self.label6 = Label(self._root, text="Female")
        self.label6.configure(font=("Constantia", 18))
        self.label6.grid(row=3, column=1)

        prevBtn=Button(self._root,text="Previous")
        prevBtn.grid(row=5,column=2,pady=(20,5))

        proposeBtn = Button(self._root, text="Propose")
        proposeBtn.grid(row=5, column=3,pady=(20,5))

        nextBtn = Button(self._root, text="Next")
        nextBtn.grid(row=5, column=4,pady=(20,5))"""

    def logoutWindow(self):
        self.clearScreen()
        self.clearScreen1()
        self.printMessage1("LogOut","You have Successfully Logged Out","info")
        self._root.destroy()
        self._root.mainloop()
        return self.__init__()

    def viewWindow(self, other, data,a,b,mode, num=0):
        self.clearScreen()
        self.headerMenu(other, data,a,b)

        imageUrl = "image/2.jpg"
        load = Image.open(imageUrl)
        load = load.resize((200, 200), Image.ANTIALIAS)
        render = ImageTk.PhotoImage(load)

        img = Label(image=render)
        img.image = render
        img.pack()

        self.label1 = Label(self._root, text="Name : ")
        self.label1.configure(font=("Constantia", 18))
        self.label1.pack()

        name = data[0][1]
        self.label2 = Label(self._root, text=name)
        self.label2.configure(font=("Constantia", 18))
        self.label2.pack()

        self.label3 = Label(self._root, text="Age : ")
        self.label3.configure(font=("Constantia", 18))
        self.label3.pack()

        age = str(data[0][4])
        self.label4 = Label(self._root, text=age)
        self.label4.configure(font=("Constantia", 18))
        self.label4.pack()

        self.label5 = Label(self._root, text="Gender : ")
        self.label5.configure(font=("Constantia", 18))
        self.label5.pack()

        gender = data[0][5]
        self.label6 = Label(self._root, text=gender)
        self.label6.configure(font=("Constantia", 18))
        self.label6.pack()

        """self.label7 = Label(self._root, text="City : ")
        self.label7.configure(font=("Constantia", 18))
        self.label7.grid(row=4, column=0)

        city=data[0][7]
        self.label7 = Label(self._root, text=city)
        self.label7.configure(font=("Constantia", 18))
        self.label7.grid(row=4, column=1)

        self.label8=Label(self._root,text="Bio : ")
        self.label8.configure(font=("Constantia",18))
        self.label8.grid(row=5,column=0)


        bio=data[0][8]
        self.label8 = Label(self._root, text="Cool")
        self.label8.configure(font=("Constantia", 18))
        self.label8.grid(row=5,column=1)

       if mode == 2:
           frame = Frame(self._root)
           frame.pack()
           btn1 = Button(frame, text="Want to Edit", fg="#fff", bg="#fd5068", command=lambda: other.viewUsers(num - 1))
           btn1.pack(side=LEFT)
           btn2 = Button(frame, text="Want to Save", fg="#fff", bg="#fd5068", command=lambda: other.propose(data[0][0]))
           btn2.pack(side=LEFT)"""
