from tkinter import *
import tkinter.messagebox
from tkinter.ttk import *
import sqlite3
con=sqlite3.connect('construction.db')
rootp=Tk()
rootp.geometry("900x700")
rootp.configure(background="green")
Label(rootp,text="CONSTRUCTION MANAGEMENT",font="helvetica 40",background="blue").pack()
def fun8():
    rootp.destroy()
    root2=Tk()
    root2.geometry("900x700")
    root2.configure(background="green")
    root2.title("FIRE")
    Label(root2,text="Enter your Id").grid(row=0,column=0)
    e1=Entry(root2)
    e1.grid(row=0,column=1)
    Label(root2,text="Projects").grid(row=1,column=0)
    w2=Combobox(root2,text="Projects",height=5,width=15,values=["House","Mall","School","Road","Hospital","Parks","METRO"])
    w2.grid(row=1,column=1)
    Label(root2,text="First name").grid(row=2,column=0)
    w3=Entry(root2)
    w3.grid(row=2,column=1)
    def fun2():
        d=e1.get()
        b=w2.get()
        c=w3.get()
        cur=con.cursor()
        x=str(d)
        con.commit()
        if d=='' or b=='' or c=='':
             tkinter.messagebox.showerror("Oops","You can't leave any field empty")
        else:     
             
                cur.execute("delete from employee where Id=(?) and First_Name=(?)",(d,c,))
                con.commit()
                cur.execute("select * from employee")
                tkinter.messagebox.showinfo("employee is fired",cur.fetchall())
            
        
                    
            
    Bc=Button(root2,text="fire",command=fun2).grid(row=4,column=0)
    root2.mainloop()
def fun9():
    rootp.destroy()
    root4=Tk()
    root4.geometry("900x700")
    root4.configure(background="green")
    root4.title("Welcome,Search Employee")
    root4.configure(background="pink")
    Label(root4,text="First name",background="blue").grid(row=0,column=0)
    w1=Entry(root4)
    w1.grid(row=0,column=1)
    Label(root4,text="Last name").grid(row=1,column=0)
    w2=Entry(root4)
    w2.grid(row=1,column=1)
    Label(root4,text="Projects").grid(row=2,column=0)
    w3=Combobox(root4,text="Projects",height=5,width=15,values=["House","Mall","School","Road","Hospital","Parks","METRO"])
    w3.grid(row=2,column=1)
    def fun10():
        a=w1.get()
        b=w2.get()
        c=w3.get()
        cur=con.cursor()
        if a=='' or b=='' or c=='':
            tkinter.messagebox.showerror("Error","Cant leave any field empty")
           
                
        else:
             if a!=b:
                 #cur.execute("create table eco(boarding char(20),destination char(20),day char(20),time number,class char(10),fare number)")
                 #cur.execute("insert into eco values('New York','Chicago','Sunday',1.00,'Economic',2500)")
                 #cur.execute("insert into eco values('New York','Dallas','Monday',1.00,'Common',4000)")
                 #cur.execute("insert into eco values('New York','San Francisco','Tuesday',1.00,'Economic',5500)")
                 #cur.execute("insert into eco values('Chicago','New York','Wensday',1.00,'Economic',3500)")
                 #cur.execute("insert into eco values('Chicago','New York','Wensday',7.00,'Common',2500)")
                 cur.execute("select * from employee where First_Name=? and Last_name=? and Projects=?",(a,b,c,))
                 con.commit()
                 e=cur.fetchall()
                 tkinter.messagebox.showinfo("Employee found",e)
             else:
                tkinter.messagebox.showerror("Oops","NO such employee")
        
    Bs=Button(root4,text="search",command=fun10).grid(row=3,column=0)
    root4.mainloop()
def fun5():
    rootp.destroy()
    root=Tk()
    root.geometry("900x700")
    root.configure(background="green")
    root.title('Registration')
    Label(root,text="First name").grid(row=1,column=0)
#e1=Entry(root,width=20,bd=4,justify="right")
#e1.grid(row=1,column=1)
    w=Entry(root) 
    w.grid(row=1,column=1)
    Label(root,text='Last name').grid(row=2,column=0)
#e2=Entry(root,width=20,justify='right')
#e2.grid(row=2,column=1)
    w1=Entry(root) 
    w1.grid(row=2,column=1)
#e3=Entry(root,width=20,justify='right')
#e3.grid(row=3,column=1)
    Label(root,text='Age').grid(row=3,column=0)
    e=Entry(root,width=20)
    e.grid(row=3,column=1)
    w2=Entry(root) 
    w2.grid(row=4,column=1)
    Label(root,text='Id').grid(row=4,column=0)
    Label(root,text="Projects").grid(row=5,column=0)
    w3=Combobox(root,text="Projects",height=5,width=15,values=["House","Mall","School","Road","Hospital","Parks","METRO"])
    w3.grid(row=5,column=1)
    Label(root,text="Wages").grid(row=6,column=0)
    w4=Entry(root) 
    w4.grid(row=6,column=1)
    def fun():
        a=w.get()
        b=w1.get()
        c=e.get()
        d=w2.get()
        f=w3.get()
        g=w4.get()
        x=(a,b,c,d,f,g)
        cur=con.cursor()
        
        if a=='' or b=='' or c=='' or d=='' or f=='' or g=='':
            tkinter.messagebox.showerror("OOPS","you can't leave any field empty")
        else :                
                if a!=b:
                    #cur.execute("create table economic2(boarding char(20),destination char(20),adno number,day char,time number)")
                    cur.execute("insert into employee values(?,?,?,?,?,?)",x)
                    tkinter.messagebox.showinfo("congrats","you are an employee now")
                    con.commit()
                    cur.execute("select * from employee where Id=(?)",(d,))
                    tkinter.messagebox.showinfo("records",cur.fetchall())
                else:
                    tkinter.messagebox.showerror("Error","you can't have same 1st and last name")
    Bi=Button(root,text="Insert",command=fun).grid(row=7,column=1)
#Bo=Button(root,text="See Flights",command=dis).grid(row=7,column=1)
#Bf=Button(root,text='Set fair range',command=fun1).grid(row=7,column=2)
    root.mainloop()

B3=Button(rootp,text="Employee",command=fun5).pack()
B2=Button(rootp,text="Employee list",command=fun9).pack()    
B1=Button(rootp,text="Fire employee",command=fun8).pack()


#B2=Button(rootp,text="Cancel Booking",height=4,width=35,font="Bold",bg="gray").pack()
#B3=Button(rootp,text="See flights",height=4,width=35,font="Bold",bg="gray").pack()


rootp.mainloop()
    
