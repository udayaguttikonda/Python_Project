from Tkinter import *
import sqlite3
import json
from tkMessageBox import *
con=sqlite3.Connection('ram_db')
cur=con.cursor()
cur.execute("create table if not exists userid(username varchar(20) primary key,fname varchar(20),lname varchar(20),gender varchar(10),dob date,email varchar(40),password varchar(20),marital_status varchar(20),culture varchar(20),education varchar(20),complexion varchar(20),pob varchar(30),ft varchar(10),profession varchar(20),income varchar(15),height varchar(5),weight varchar(8),drink varchar(15))")
root=Tk()
root.geometry('1005x645')
root.title("Ram marriage bureau")
pi=PhotoImage(file="first.gif")
Label(root,image=pi).place(x=2,y=0)
Label(root, text="Welcome to Matrimonial spot", font=("algerian", 45), fg="white",bg="light blue" ,width=27).grid(row=0, column=0)
Label(root, text="The No.1 Matchmaking, Matrimony & Matrimonial Site \n Register today to find someone special", font=("algerian", 18), fg="blue", bg="green").grid(row=1, column=0)
def clo():
    que=askquestion('EXIT','Are you sure')
    if(que=='yes'):
        root.destroy()

#-------------------------------------------------------------------------------------------------------------------------------------
def now():
    root.destroy()
    root1=Tk()
    root1.title("LOGIN PAGE")
    root1.geometry('805x520')


#-----------------------++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++-----------------------------------+    
    def account():
        def ful():
            
                l = (username.get(), fname.get(), lname.get(), gender.get(), dob.get(), email.get(), password.get(),ms.get(), c.get(), ed.get(), cpl.get(), pob.get(), ft.get(), o.get(),i.get(),hei.get(),w.get(),d.get())
                cur.execute("insert into userid values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",l)
                showinfo('Congo!!',"You Are A User of matrimonial")
                con.commit()
                
                   
        user=username.get()
        cur.execute("select username from userid where username=(?)",(user,))
        a=cur.fetchall()
        if a != []:
            showerror('Error',"Username Already Exists")
        else:
            root11=Tk()    
            root11["bg"] = "black"
            
           
#---------------------------------------Select marital status ------------------------------------------------------------------------------------------
            Label(root11, text="Select marital status", font=("cooper black", 15),fg="black").grid(row=4, column=0)
            ms = StringVar(root11)
            ms.set("Select")
            OptionMenu(root11, ms, "Single","Divorced","Widowed","Seprated").grid(row=4,column=1)
            
#---------------------------------------Select Culture ------------------------------------------------------------------------------------------
            Label(root11, text="Select Culture", font=("cooper black", 15),fg="black").grid(row=5, column=0)
            c = StringVar(root11)
            c.set("Select")
            OptionMenu(root11, c, "Jainism", "Buddhism", "Sikhism","Hinduism").grid(row=5,column=1)

#---------------------------------------Select Education ------------------------------------------------------------------------------------------
            Label(root11, text="Select Education", font=("cooper black", 15),fg="black").grid(row=6, column=0)
            ed = StringVar(root11)
            ed.set("Select")
            OptionMenu(root11, ed, "No formal education","Primary education","Secondary education","Vocational qualification","Bachelor's degree","Master's degree","Doctorate","higher").grid(row=6,column=1)

#---------------------------------------Select complexion ------------------------------------------------------------------------------------------
            Label(root11, text="Select complexion", font=("cooper black", 15),fg="black").grid(row=7, column=0)
            cpl = StringVar(root11)
            cpl.set("Select")
            OptionMenu(root11, cpl, "Fair", "Medium", "Dark","Wheatish").grid(row=7,column=1)
            
#---------------------------------------Enter place of birth ------------------------------------------------------------------------------------------
            Label(root11, text="Enter place of birth", font=("cooper black", 15),fg="black").grid(row=8, column=0)
            pob = Entry(root11, width=30, font=("arial", 11), bg=('#ffcccc'))
            pob.grid(row=8, column=1)

#---------------------------------------Select Family type --------------------------------------------------------------------------------------------
            Label(root11, text="Select Family type", font=("cooper black", 15),fg="black").grid(row=9, column=0)
            ft = StringVar(root11)
            ft.set("Select")
            OptionMenu(root11, ft, " rich","upper middle class","middle class", "does not matter").grid(row=9,column=1)

#---------------------------------------Select Occupation --------------------------------------------------------------------------------------------
            Label(root11, text="Select Occupation", font=("cooper black", 15),fg="black").grid(row=10, column=0)
            o = StringVar(root11)
            o.set("Select")
            OptionMenu(root11, o, " Actor","Business Owner","Entrepreneur","Engineer","Comedian","Entertainer","Lawyer","Musician","Publisher").grid(row=10,column=1)

#---------------------------------------Select Income ------------------------------------------------------------------------------------------------
            Label(root11, text="Select Income", font=("cooper black", 15),fg="black").grid(row=11, column=0)
            i = StringVar(root11)
            i.set("Select")
            OptionMenu(root11, i, "<20000","20k~30k","20k~30k","30k~50k","50k~1 lakh",">1 lakh").grid(row=11,column=1)

#---------------------------------------Enter Height -------------------------------------------------------------------------------------------------
            Label(root11, text="Enter Height <cm>", font=("cooper black", 15),fg="black").grid(row=12, column=0)
            hei= Entry(root11, width=30, font=("arial", 11), bg=('#ffcccc'))
            hei.grid(row=12, column=1)

#---------------------------------------Enter Weight ------------------------------------------------------------------------------------------------
            Label(root11, text="Enter Weight<kg>", font=("cooper black", 15),fg="black").grid(row=13, column=0)
            w = Entry(root11, width=30, font=("arial", 11), bg=('#ffcccc'))
            w.grid(row=13, column=1)
            
#---------------------------------------Drink or not ------------------------------------------------------------------------------------------------
            Label(root11, text="Drink", font=("cooper black", 15),fg="black").grid(row=14, column=0)
            d= StringVar(root11)
            d.set("Select")
            OptionMenu(root11, d,"Never","Regularly","In parties/occasion").grid(row=14,column=1)
            Button(root11, text="Submit", compound='center', font=("arial", 10), bg='green', fg='white', width=10, command=lambda: ful()).grid(row=15, columnspan=1)
            root11.mainloop()

#----------------------------------------------------------------------------------------------------------------------------------------------------            
    def account1():
        usr = user.get()
        pasw = pas.get()
        cur.execute("select * from userid where username=(?) and password=(?)", (usr, pasw,))
        a = cur.fetchall()
        if a==[]:
            showerror('Log In Failed', "Invalid Username or Password")
        else:
            root1.destroy()
            root4 = Tk()
            root4.title("searching")
            root4.geometry('930x645')
            o=PhotoImage(file="first.gif")
            Label(root4,image=o).place(x=0,y=0)
            #Label(root4,image=o).grid(row=0, column=0)
            Label(root4, text="Ram marriage bureau", font=("algerian", 22), fg="black", bg="red", width=52).place(x=0,y=40)
            Label(root4, text="Please choose your priority in searching ", font=("cooper black", 21),fg="red").place(x=0,y=100)
            
            Label(root4, text="On the basis of Cultural", font=("cooper black", 15),fg=('Blue')).place(x=30,y=180)
            c1 = StringVar(root4)
            c1.set("Select")
            OptionMenu(root4, c1, "Jainism", "Buddhism", "Sikhism","Hinduism").place(x=570,y=180)
            Label(root4, text="On the basis of Family", font=("cooper black", 15),fg=('Blue')).place(x=30,y=260)
            ft1 = StringVar(root4)
            ft1.set("Select")
            OptionMenu(root4, ft1, " rich","upper middle class","middle class", "does not matter").place(x=570,y=260)
            Label(root4, text="On the basis of Education", font=("cooper black", 15),fg=('Blue')).place(x=30,y=340)
            ed1 = StringVar(root4)
            ed1.set("Select")
            OptionMenu(root4, ed1, "No formal education","Primary education","Secondary education","Vocational qualification","Bachelor's degree","Master's degree","Doctorate","higher").place(x=570,y=340)
            Label(root4, text="On the basis of Marital Status", font=("cooper black", 15),fg="blue").place(x=30,y=420)
            ms1 = StringVar(root4)
            ms1.set("Select")
            OptionMenu(root4, ms1, "Single","Divorced","Widowed","Seprated").place(x=570,y=420)
            def funf():
                root4.destroy()
                root10=Tk()
                imgs = PhotoImage(file="third.gif")
                Label(root10,image=imgs).place(x=2,y=0)
                root10.geometry('750x545')
                root10.title("Ram marriage bureau")
                cur.execute("select gender from userid where username=(?)", (usr))
                x=cur.fetchall()
                print x
                for row in x :
                    if(row[0]=='male'):
                            #cur.execute("select count(*) from userid where gender!='male' and marital_status=(?) and culture=(?) and education=(?) and ft=(?)",(ms1.get(),c1.get(),ed1.get(),ft1.get(),))
                            #kl=cur.fetchall()
                            #print kl
                            cur.execute("select * from userid where gender!='male' and marital_status=(?) and culture=(?) and education=(?) and ft=(?)",(ms1.get(),c1.get(),ed1.get(),ft1.get(),))
                            r=cur.fetchall()
                            Label(root10, text="Firstname: ", font=("cooper black", 15),fg=('Black')).place(x=100,y=30)
                            Label(root10, text=r[0][1], font=("cooper black", 15),fg=('Black')).place(x=450,y=30)
                            Label(root10, text="Lastname: ", font=("cooper black", 15),fg=('Black')).place(x=100,y=60)
                            Label(root10, text=r[0][2], font=("cooper black", 15),fg=('Black')).place(x=450,y=60)
                            Label(root10, text="GENDER: ", font=("cooper black", 15),fg=('Black')).place(x=100,y=90)
                            Label(root10, text=r[0][3], font=("cooper black", 15),fg=('Black')).place(x=450,y=90)
                            Label(root10, text="DOB", font=("cooper black", 15),fg=('Black')).place(x=100,y=120)
                            Label(root10, text=r[0][4], font=("cooper black", 15),fg=('Black')).place(x=450,y=120)
                            Label(root10, text="E-Mail ", font=("cooper black", 15),fg=('Black')).place(x=100,y=150)
                            Label(root10, text=r[0][5], font=("cooper black", 15),fg=('Black')).place(x=450,y=150)
                            Label(root10, text="Marital Status", font=("cooper black", 15),fg="Black").place(x=100,y=180)
                            Label(root10, text=r[0][7], font=("cooper black", 15),fg=('Black')).place(x=450,y=180)
                            Label(root10, text="Culture", font=("cooper black", 15),fg="Black").place(x=100,y=210)
                            Label(root10, text=r[0][8], font=("cooper black", 15),fg=('Black')).place(x=450,y=210)
                        
                            Label(root10, text="Education", font=("cooper black", 15),fg="Black").place(x=100,y=240)
                            Label(root10, text=r[0][9], font=("cooper black", 15),fg=('Black')).place(x=450,y=240)
                            Label(root10, text="Complexion", font=("cooper black", 15),fg="Black").place(x=100,y=270)
                            Label(root10, text=r[0][10], font=("cooper black", 15),fg=('Black')).place(x=450,y=270)
                            Label(root10, text="Place of Birth", font=("cooper black", 15),fg="Black").place(x=100,y=300)
                            Label(root10, text=r[0][11], font=("cooper black", 15),fg=('Black')).place(x=450,y=300)
                            Label(root10, text="Family Type", font=("cooper black", 15),fg="Black").place(x=100,y=330)
                            Label(root10, text=r[0][12], font=("cooper black", 15),fg=('Black')).place(x=450,y=330)
                            Label(root10, text="Occupation", font=("cooper black", 15),fg="Black").place(x=100,y=360)
                            Label(root10, text=r[0][13], font=("cooper black", 15),fg=('Black')).place(x=450,y=360)
                            Label(root10, text="Income", font=("cooper black", 15),fg="Black").place(x=100,y=390)
                            Label(root10, text=r[0][14], font=("cooper black", 15),fg=('Black')).place(x=450,y=390)
                            Label(root10, text="Height <cm>", font=("cooper black", 15),fg="Black").place(x=100,y=410)
                            Label(root10, text=r[0][15], font=("cooper black", 15),fg=('Black')).place(x=450,y=410)
                            Label(root10, text="Weight<kg>", font=("cooper black", 15),fg="Black").place(x=100,y=440)
                            Label(root10, text=r[0][16], font=("cooper black", 15),fg=('Black')).place(x=450,y=440)
                            Label(root10, text="Drink", font=("cooper black", 15),fg="Black").place(x=100,y=470)
                            Label(root10, text=r[0][17], font=("cooper black", 15),fg="Black").place(x=450,y=470)
                            root10.mainloop()
                    else:
                        cur.execute("select count(*) from userid where gender!='female' and marital_status=(?) and culture=(?) and education=(?) and ft=(?)",(ms1.get(),c1.get(),ed1.get(),ft1.get(),))
                        kl=cur.fetchall()
                        sd=kl[0][0]
                        cur.execute("select * from userid where gender!='female' and marital_status=(?) and culture=(?) and education=(?) and ft=(?)",(ms1.get(),c1.get(),ed1.get(),ft1.get(),))

                        while(kl[0][0]>0):
                            r=cur.fetchall()
                            Label(root10, text="Firstname: ", font=("cooper black", 15),fg=('Black')).place(x=100,y=30)
                            Label(root10, text=r[0][1], font=("cooper black", 15),fg=('Black')).place(x=450,y=30)
                            Label(root10, text="Lastname: ", font=("cooper black", 15),fg=('Black')).place(x=100,y=60)
                            Label(root10, text=r[0][2], font=("cooper black", 15),fg=('Black')).place(x=450,y=60)
                            Label(root10, text="GENDER: ", font=("cooper black", 15),fg=('Black')).place(x=100,y=90)
                            Label(root10, text=r[0][3], font=("cooper black", 15),fg=('Black')).place(x=450,y=90)
                            Label(root10, text="DOB", font=("cooper black", 15),fg=('Black')).place(x=100,y=120)
                            Label(root10, text=r[0][4], font=("cooper black", 15),fg=('Black')).place(x=450,y=120)
                            Label(root10, text="E-Mail ", font=("cooper black", 15),fg=('Black')).place(x=100,y=150)
                            Label(root10, text=r[0][5], font=("cooper black", 15),fg=('Black')).place(x=450,y=150)
                            Label(root10, text="Marital Status", font=("cooper black", 15),fg="Black").place(x=100,y=180)
                            Label(root10, text=r[0][7], font=("cooper black", 15),fg=('Black')).place(x=450,y=180)
                            Label(root10, text="Culture", font=("cooper black", 15),fg="Black").place(x=100,y=210)
                            Label(root10, text=r[0][8], font=("cooper black", 15),fg=('Black')).place(x=450,y=210)
                        
                            Label(root10, text="Education", font=("cooper black", 15),fg="Black").place(x=100,y=240)
                            Label(root10, text=r[0][9], font=("cooper black", 15),fg=('Black')).place(x=450,y=240)
                            Label(root10, text="Complexion", font=("cooper black", 15),fg="Black").place(x=100,y=270)
                            Label(root10, text=r[0][10], font=("cooper black", 15),fg=('Black')).place(x=450,y=270)
                            Label(root10, text="Place of Birth", font=("cooper black", 15),fg="Black").place(x=100,y=300)
                            Label(root10, text=r[0][11], font=("cooper black", 15),fg=('Black')).place(x=450,y=300)
                            Label(root10, text="Family Type", font=("cooper black", 15),fg="Black").place(x=100,y=330)
                            Label(root10, text=r[0][12], font=("cooper black", 15),fg=('Black')).place(x=450,y=330)
                            Label(root10, text="Occupation", font=("cooper black", 15),fg="Black").place(x=100,y=360)
                            Label(root10, text=r[0][13], font=("cooper black", 15),fg=('Black')).place(x=450,y=360)
                            Label(root10, text="Income", font=("cooper black", 15),fg="Black").place(x=100,y=390)
                            Label(root10, text=r[0][14], font=("cooper black", 15),fg=('Black')).place(x=450,y=390)
                            Label(root10, text="Height <cm>", font=("cooper black", 15),fg="Black").place(x=100,y=410)
                            Label(root10, text=r[0][15], font=("cooper black", 15),fg=('Black')).place(x=450,y=410)
                            Label(root10, text="Weight<kg>", font=("cooper black", 15),fg="Black").place(x=100,y=440)
                            Label(root10, text=r[0][16], font=("cooper black", 15),fg=('Black')).place(x=450,y=440)
                            Label(root10, text="Drink", font=("cooper black", 15),fg="Black").place(x=100,y=470)
                            Label(root10, text=r[0][17], font=("cooper black", 15),fg="Black").place(x=450,y=470)
                            sd=sd-1
                            
                            root10.mainloop()

            Button(root4, text="search", compound='center', font=("arial", 10), bg='Blue', fg='white', width=10, command=lambda:funf()).place(x=350,y=550)
           # Button(root4, text="dek", compound='center', font=("arial", 10), bg='Blue', fg='white', width=10, command=lambda:show()).place(x=200,y=185)
            
            root4.mainloop()
    
    img = PhotoImage(file="second.gif")
    Label(root1,image=img).place(x=2,y=0)
    Label(root1, text="Ram marriage bureau", font=("algerian", 22), fg="blue", bg="green", width=52).grid(row=0, column=0, columnspan=4)
    Label(root1, text="Already a User ? Log In", font=("arial", 18), fg="black", bg="white", width=20).place(x=20,y=50)
    Label(root1, text="Dont have an account ? Register", font=("arial", 18), fg="black", bg="White", width=25).place(x=435,y=50)

#---------------------------------------Entry account1 ------------------------------------------------------------------------------------------
    Label(root1, text="Username: ", font=("cooper black", 15),fg=('black')).place(x=20,y=90)
    user = Entry(width=20, font=("arial", 11), bg=('#ffcccc'))
    user.place(x=140,y=95)

    Label(root1, text="Password: ", font=("cooper black", 15),fg=('black')).place(x=20,y=135)
    pas = Entry(width=20, font=("arial", 11), bg=('#ffcccc'))
    pas.place(x=140,y=140)

    Button(root1, text="Log In", compound='center', font=("arial", 10), bg='Blue', fg='white', width=10, command=lambda: account1()).place(x=130,y=185)

#---------------------------------------Entry account ------------------------------------------------------------------------------------------
    Label(root1, text="Username: ", font=("cooper black", 15),fg=('black')).place(x=490,y=100)
    username = Entry(root1, width=18, font=("arial", 11), bg=('#ffcccc') )
    username.place(x=630,y=100)

    Label(root1, text="Firstname: ", font=("cooper black", 15),fg=('black')).place(x=490,y=150)
    fname = Entry(root1, width=18, font=("arial", 11), bg=('#ffcccc'))
    fname.place(x=630,y=150)

    Label(root1, text="Lastname: ", font=("cooper black", 15),fg=('black')).place(x=490,y=200)
    lname = Entry(root1, width=18, font=("arial", 11), bg=('#ffcccc'))
    lname.place(x=630,y=200)

    Label(root1, text="GENDER: ", font=("cooper black", 15),fg=('black')).place(x=490,y=250)
    gender = StringVar(root1)
    gender.set("Choose")
    OptionMenu(root1, gender,"Male","Female","Transgender").place(x=630,y=250)
    #gender = Entry(root1, width=18, font=("arial", 11), bg=('#ffcccc'))
    #gender.place(x=630,y=250)

    Label(root1, text="DOB", font=("cooper black", 15),fg=('black')).place(x=490,y=300)
    dob = Entry(root1, width=18, font=("arial", 11), bg=('#ffcccc'))
    dob.place(x=630,y=300)

    Label(root1, text="E-Mail ", font=("cooper black", 15),fg=('black')).place(x=490,y=350)
    email = Entry(root1, width=18, font=("arial", 11), bg=('#ffcccc'))
    email.place(x=630,y=350)

    Label(root1, text="Password: ", font=("cooper black", 15),fg=('black')).place(x=490,y=400)
    password = Entry(root1, width=18, font=("arial", 11), bg=('#ffcccc'))
    password.place(x=630,y=400)

    Button(root1, text="Sign Up", compound='center', font=("arial", 10), bg='Blue', fg='white', width=10, command=lambda: account()).place(x=660,y=470)
    root1.mainloop()

Label(root, text="Happiness is Just a Click Away!", font=("algerian", 18), fg="blue", bg="green").place(x=60,y=500)
Button(root, text="Click here to continue", font=("Comic Sans MS", 12), bg='blue', fg='white', width=20, command=lambda: now()).place(x=100,y=550)
Button(root, text="EXIT", font=("Comic Sans MS", 12), bg='blue', fg='white', width=10, command=lambda: clo()).place(x=825,y=550)
root.mainloop()
