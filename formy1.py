from tkinter import *
from tkinter import filedialog
root = Tk()
root.geometry('1000x1500')
root.title("Registration Form")

import os
import subprocess as sp

import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',passwd='Akis.123',database="Application")
mycursor=mydb.cursor()


#To specify what kind of variable is going to be used
fn=StringVar()
ln=StringVar()
dob=StringVar()
engi=StringVar()
st=IntVar()
ge= IntVar()
phy=IntVar()
chem=IntVar()
math=IntVar()
sn=StringVar()
cr=IntVar()

eg=StringVar()
ep=DoubleVar()
mg=StringVar()
mp=DoubleVar()
og=StringVar()
op=DoubleVar()
cg=StringVar()
cp=DoubleVar()
pg=StringVar()
pp=DoubleVar()



#function to exit the form
def exitt():
    exit()


#to store values inputed in form into variables and print them  
def printt():
    first=fn.get()
    sec=ln.get()
    var1=var.get()
    date1=d.get()
    month1=m.get()
    year1=y.get()
    dept=engi.get()
    stc=st.get()
    ma=math.get()
    c=chem.get()
    p=phy.get()
    sstc=int(ma)+int(c)+int(p)
    gen=ge.get()

    school=sn.get()
    rank=cr.get()

    ep1=ep.get()
    mp1=mp.get()
    op1=op.get()
    cp1=cp.get()
    pp1=pp.get()
    overall=(ep1+mp1+op1+cp1+pp1)/5
    if gen==2:
        gen="female"
    elif gen==1:
        gen="male"
    details=[first+' '+sec, date1+"/"+month1+"/"+year1,var1,school,dept,int(stc),int(sstc),gen,overall,rank]
    details=tuple(details)
    path="C:\\Users\\500490\\Desktop\\cs project"
    cn1=os.path.join(path,'Detailsfile.txt' )
    dfile=open(cn1,"w")
    dfile.write(str(details))
    print (details)
    mycursor.execute('insert resumemain values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',details)
    mydb.commit()
    mycursor.execute("select * from Resumemain")
    for i in mycursor:
        print (i)


        
#important  widgets and uses 
'''
The Entry widget is used to display a single-line text field for accepting values from a user.
'''

'''
The Label widget is used to provide a single-line caption for other widgets. It can also contain images.
'''

'''
The Menu widget is used to provide various commands to a user. These commands are contained inside Menubutton.
'''

'''
The Radiobutton widget is used to display a number of options as radio buttons. The user can select only one option at a time.
'''

'''
The place() Method − This geometry manager organizes widgets by placing them in a specific position in the parent widget.
'''

label_0=Label(root,text="Registration Form", relief="solid",width=20)
label_0.place(x=175,y=10)

#for First Name of person

label_1=Label(root,text="FirstName :",width=20,font=("bold",10))
label_1.place(x=80,y=40)

entry_1=Entry(root,textvar=fn)
entry_1.place(x=240,y=42)

#for last name of person

label_2=Label(root,text="LastName :",width=20,font=("bold",10))
label_2.place(x=80,y=80)

entry_2=Entry(root,textvar=ln)
entry_2.place(x=240,y=82)

#For date of birth of person

dob=Label(root, text="DOB :",width=20,font=("bold", 10))
dob.place(x=65,y=120)

#drop down menu for Date of birth

l=[]
for i in range(1,32):
    l.append(str(i))
day=l;
d=StringVar()
dropd=OptionMenu(root,d, *day)
dropd.config(width=4)
d.set("Date")
dropd.place(x=240,y=125)

#drop down menu for Month of birth

month = ['January','February','March','April','May','June','July','August','September','October','November','December'];
m=StringVar()
dropm=OptionMenu(root,m, *month)
dropm.config(width=10)
m.set("Month")
dropm.place(x=300,y=125)

#drop down menu for Year of birth

year=['1999','2000','2001','2002','2003','2004','2005','2006','2007'];
y=StringVar()
dropy=OptionMenu(root,y, *year)
dropy.config(width=5)
y.set("Year")
dropy.place(x=400,y=125)

#for Nationality

label_4=Label(root,text="Nationality :",width=20,font=("bold",10))
label_4.place(x=75,y=170)

var=StringVar()
l=['Indian','British','American','Canadian','Qatari']
droplist=OptionMenu(root,var,*l)
var.set('Select Nationality')
droplist.config(width=15)
droplist.place(x=230,y=170)

#Program of Application

label_5=Label(root,text="I am applying for :",width=20,font=("bold",10))
label_5.place(x=75,y=220)
l1=["Chemical Engineering"," Civil Engineering","Mechanical Engineering","IT","Computer Science","Electronics and Communication","Mathematics"]
droplist=OptionMenu(root,engi,*l1)
engi.set('Select Department')
droplist.config(width=20)
droplist.place(x=230,y=225)

#SAT scores

label_6=Label(root,text="SAT Scores :",width=20,font=("bold",10))
label_6.place(x=75,y=270)
entry_6=Entry(root,textvar=st)
entry_6.place(x=240,y=275)

#SAT subject scores which will be later added together

label_7=Label(root,text="SAT Subject Scores :",width=20,font=("bold",10))
label_7.place(x=75,y=320)
label_7a=Label(root,text="Physics:",width=10,font=("bold",10))
label_7a.place(x=150,y=350)
label_7b=Label(root,text="Chemistry:",width=10,font=("bold",10))
label_7b.place(x=150,y=380)
label_7c=Label(root,text="Maths:",width=10,font=("bold",10))
label_7c.place(x=150,y=410)
entry_7c=Entry(root,textvar=math)
entry_7c.place(x=270,y=415)
entry_7b=Entry(root,textvar=chem)
entry_7b.place(x=270,y=385)
entry_7a=Entry(root,textvar=phy)
entry_7a.place(x=270,y=355)


#Gender of applicant

label_8= Label(root, text="Gender",width=20,font=("bold", 10))
label_8.place(x=75,y=450)
Radiobutton(root, text="Male",padx = 5, variable=ge, value=1).place(x=240,y=450)
Radiobutton(root, text="Female",padx = 20, variable=ge, value=2).place(x=300,y=450)

#School Name

label_9=Label(root,text="School Name :",width=20,font=("bold",10))
label_9.place(x=600,y=40)
entry_9=Entry(root,textvar=sn)
entry_9.place(x=750,y=42)

#Class Rank

label_10=Label(root,text="Class Rank:",width=20,font=("bold",10))
label_10.place(x=594,y=80)
entry_10=Entry(root,textvar=cr)
entry_10.place(x=750,y=82)

#grades and percentage

label_11=Label(root,text="GRADES AND PERCENTAGE:",width=40,font=("bold",10))
label_11.place(x=600,y=120)

#English
label_11a=Label(root,text="English:",width=40,font=("bold",10))
label_11a.place(x=600,y=160)
label_11aa=Label(root,text="Grade:",width=20,font=("bold",10))
label_11aa.place(x=600,y=190)
label_11ab=Label(root,text="%:",width=20,font=("bold",10))
label_11ab.place(x=600,y=220)

entry_11aa=Entry(root,textvar=eg)
entry_11aa.place(x=730,y=190)
entry_11ab=Entry(root,textvar=ep)
entry_11ab.place(x=730,y=220)

#Maths
label_11b=Label(root,text="Maths:",width=40,font=("bold",10))
label_11b.place(x=600,y=260)
label_11ba=Label(root,text="Grade:",width=20,font=("bold",10))
label_11ba.place(x=600,y=290)
label_11bb=Label(root,text="%:",width=20,font=("bold",10))
label_11bb.place(x=600,y=320)

entry_11ba=Entry(root,textvar=mg)
entry_11ba.place(x=730,y=290)
entry_11bb=Entry(root,textvar=mp)
entry_11bb.place(x=730,y=320)

#Optionals
label_11c=Label(root,text="Optional Subject:",width=40,font=("bold",10))
label_11c.place(x=600,y=360)
label_11ca=Label(root,text="Grade:",width=20,font=("bold",10))
label_11ca.place(x=600,y=390)
label_11cb=Label(root,text="%:",width=20,font=("bold",10))
label_11cb.place(x=600,y=420)

entry_11ca=Entry(root,textvar=og)
entry_11ca.place(x=730,y=390)
entry_11cb=Entry(root,textvar=op)
entry_11cb.place(x=730,y=420)

#Chemistry
label_11d=Label(root,text="Chemistry:",width=40,font=("bold",10))
label_11d.place(x=600,y=460)
label_11da=Label(root,text="Grade:",width=20,font=("bold",10))
label_11da.place(x=600,y=490)
label_11db=Label(root,text="%:",width=20,font=("bold",10))
label_11db.place(x=600,y=520)

entry_11da=Entry(root,textvar=cg)
entry_11da.place(x=730,y=490)
entry_11db=Entry(root,textvar=cp)
entry_11db.place(x=730,y=520)

#Physics
label_11e=Label(root,text="Physics:",width=40,font=("bold",10))
label_11e.place(x=600,y=560)
label_11ea=Label(root,text="Grade:",width=20,font=("bold",10))
label_11ea.place(x=600,y=590)
label_11eb=Label(root,text="%:",width=20,font=("bold",10))
label_11eb.place(x=760,y=620)

entry_11ea=Entry(root,textvar=pg)
entry_11ea.place(x=730,y=590)
entry_11eb=Entry(root,textvar=pp)
entry_11eb.place(x=730,y=620)




#To upload files from any folder and save the file name as the name of the person
def upload():
    root.filename =  filedialog.asksaveasfilename(initialdir = "/",title = "Select file",filetypes = (("txt files","*.txt"),("all files","*.*")))
    print (root.filename)
    f=open(root.filename,'r')
    frd=f.read()
    first=fn.get()
    #to save the filename as the name of the applicant
    a=str(first)+'.txt'
    #path=r"C:\\Users\\500490\\Desktop\\cs project"
    #cn=os.path.join(path,r'{first}.txt')
    file=open(a,"w")
    #file=open(f'{first}.txt','w')
    file.write(frd)
    file.close()

'''
The Button widget is used to display buttons in your application.
'''

but_u=Button(root,text="Upload File on Extracurriculars(.txt)",width=35,bg="brown",fg="White",command=upload).place(x=200,y=520)

but_signup=Button(root,text="Submit",width=20,bg="brown",fg="White",command=printt).place(x=150,y=600)
but_quit=Button(root,text="Quit",width=20,bg='brown',fg='white',command=exitt).place(x=350,y=600)
root.mainloop()


