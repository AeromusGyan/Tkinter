# import tkinter
from tkinter import *
import pymysql
import tkinter.messagebox as m

def resetAll():

        master.destroy()

        master = Tk()
        
# Creating a main window
r = Tk()

r.geometry("450x500")
r.title("My App")
r.configure(bg="Yellow")

# Database creation function 
def CreateConn():
    return pymysql.connect(host="localhost",database="test",user="sciakugyan",password="gyan",port=3306)


# Adding label in main window

rn = Label(r,text="Roll no")
rn.place(x=20,y=20)

fn = Label(r,text="First name")
fn.place(x=20,y=60)

ln = Label(r,text="Last name")
ln.place(x=20,y=100)

em = Label(r,text="Email")
em.place(x=20,y=130)

# Adding entry Box into Main Window

ern = Entry()
ern.place(x=100,y=20)

efn = Entry()
efn.place(x=100,y=60)

eln = Entry()
eln.place(x=100,y=100)

eem = Entry()
eem.place(x=100,y=130)

def InsertData():
    r = ern.get()
    f = efn.get()
    l = eln.get()
    e = eem.get()
    if (f=="" or l=="" or e==""):
        m.showinfo("Insert Status","All fields are mandatory")
    else:
        try:
            conn = CreateConn()
            cursor = conn.cursor()
            args = (f,l,e)
            query = "insert into students(fname,lname,email)values(%s,%s,%s)"
            cursor.execute(query,args)
            conn.commit()  #saving the data using commit
            m.showinfo("Insert Status","Data Inserted")
            conn.close()
        except Exception as e:
            print("Insert Exception :", e)

def ShowAllData():
    try:
        h = 0
        v = 0
        conn = CreateConn()
        cursor = conn.cursor()
        query = "select * from students"
        cursor.execute(query)
        result = cursor.fetchall()

        rn = Label(r,text="Roll no")
        rn.place(x=20,y=250)

        fn = Label(r,text="First name")
        fn.place(x=90,y=250)

        ln = Label(r,text="Last name")
        ln.place(x=170,y=250)

        em = Label(r,text="Email")
        em.place(x=250,y=250)
        for i in result:
            for j in i:
                label = Label(r, text= str(j))
                label.pack()
                label.place(x=40 + h,y=280 + v)
                h = h + 70
            h = 0
            v = v + 40
            # m.showinfo("Search Status",i)
        conn.close()
    except Exception as e:
        print("Search Exception :", e)

def ShowAllDataById():
    h = 0
    v = 0
    rs = ern.get()
    if (rs==""):
        m.showinfo("Search Status","Roll no is mandatory")
    else:
        try:
            conn = CreateConn()
            cursor = conn.cursor()
            args = (rs)
            query = "select * from students where rollno=%s"
            cursor.execute(query,args)
            result = cursor.fetchall()
            
            rn = Label(r,text="Roll no")
            rn.place(x=20,y=230)

            fn = Label(r,text="First name")
            fn.place(x=90,y=230)

            ln = Label(r,text="Last name")
            ln.place(x=170,y=230)

            em = Label(r,text="Email")
            em.place(x=250,y=230)

            for i in result:
                for j in i:
                    label1 = Label(r, text= str(j))
                    label1.pack()
                    label1.place(x=20 + h, y=260 + v)
                    h = h + 50
                h = 0
                v = v + 40
                m.showinfo("Search Status","Data Fetched",i)
            conn.close()
        except Exception as e:
            print("Search Exception :", e)
    
def UpdateData():
    r = ern.get()
    f = efn.get()
    l = eln.get()
    e = eem.get()
    if (f=="" or l=="" or e==""):
        m.showinfo("Update Status","All fields are mandatory")
    else:
        try:
            conn = CreateConn()
            cursor = conn.cursor()
            args = (f,l,e,r)
            query = "update students set fname=%s,lname=%s,email=%s where rollno=%s"
            cursor.execute(query,args)
            conn.commit()  #saving the data using commit
            m.showinfo("Update Status","Data Updated")
            conn.close()
        except Exception as e:
            m.showerror("Update Status",e)
            print("Update Exception :", e)
    ShowAllData()

def DeleteData():
    
    r = ern.get()
    if (r==""):
        m.showinfo("Delete Status","Roll no is mandatory")
    else:
        try:
            conn = CreateConn()
            cursor = conn.cursor()
            args = (r)
            query = "delete from students where rollno=%s"
            cursor.execute(query,args)
            conn.commit()
            m.showinfo("Delete Status","Data Deleted")
            conn.close()
        except Exception as e:
            print("Delete Exception :", e)
    ShowAllData()
# Adding Buttons

insert = Button(r,text="Insert",bg="White",command=InsertData)
insert.place(x=20,y=200)

search = Button(r,text="Search by Id",bg="Blue",command=ShowAllDataById)
search.place(x=80,y=200)

update = Button(r,text="Update",bg="Green",command=UpdateData)
update.place(x=180,y=200)

delete = Button(r,text="Delete",bg="Red",command=DeleteData)
delete.place(x=240,y=200)

showall = Button(r,text="Show All Data",bg="Green",command=ShowAllData)
showall.place(x=300,y=200)

reset = Button(r,text="Reset",bg="Red")
reset.place(x=390,y=200)
# mainloop method called
r.mainloop()