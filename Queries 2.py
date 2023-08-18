from tkinter import Tk, Label, Button
from matplotlib import pyplot as plt;plt.rcdefaults()
import mysql.connector
import numpy as np

#HOW WE CONNECT PYTHON TO SQL
'''
There are mainly seven steps in order to create a database connectivity.
STEPS
1.Start Python
2.Import the packages required for database programming
3.Open a connection to database
4.Create a cursor instance
5.Execute a query
6.Extract data from result set
7.Clean up the environment
'''

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="Akis.123",
  database="Application"
)

mycursor = mydb.cursor()

#A Class is like an object constructor, or a "blueprint" for creating objects
#self 
#The word 'self' is used to represent the instance of a class.
#By using the "self" keyword we access the attributes
#and methods of the class in python.

#__init__ method
#"__init__" is a reseved method in python classes.
#It is called as a constructor in object oriented terminology.
#This method is called when an object is created from a class
#and it allows the class to initialize the attributes of the class.

class App:
    def __init__(self, master):
        self.master = master
        master.title("Queries")

        self.label = Label(master, text="Select any one")
        self.label.pack()

        self.sat_button = Button(master, text="SAT toppers", command=self.sat)
        self.sat_button.pack()

        self.sats_button = Button(master, text="SAT Subject toppers", command=self.sats)
        self.sats_button.pack()

        self.overall_button = Button(master, text="High Overall scores", command=self.overall)
        self.overall_button.pack()

        self.nat_button = Button(master, text="Nationality", command=self.nat)
        self.nat_button.pack()

        self.extra_button = Button(master, text="Extracurricular", command=self.extra)
        self.extra_button.pack()

        self.age_button = Button(master, text="Age", command=self.age)
        self.age_button.pack()

    '''
    1. data=cursor.fetchall() returns all the records
    retrieved as per query in tuple form
    2. data=cursor.fetchone()returns one record
    retrieved from the resultset as per query as a tuple or a list.
    •First time it returns the first record.
    Next time it will fetch the next record and so on.
    •The method returns one record as  a tuple.
    •If there are no more records then it returns None
    '''

    def sat(self):
        mycursor.execute("SELECT Fullname, SAT FROM resumemain order by SAT desc")
        l=[]
        for i in range(5):
            myresult1 = mycursor.fetchone()
            a=list(myresult1)
            l.append(a)
            print (myresult1)
        print (l)
        l2=[]
        l3=[]
        for i in range(0,len(l)):
            l2.append(l[i][0])
        y=l2
        for i in range(0,len(l)):
            l3.append(l[i][1])
        z=l3
        plt.plot(y,z,label="SAT SCORE TOPPERS", color='red')
        plt.xlabel("NAMES")
        plt.ylabel("SAT SCORES")

        plt.legend()
        plt.show()
                       

    def sats(self):
        mycursor.execute("SELECT Fullname, SATSubject FROM resumemain order by SATSubject desc")
        l=[]
        for i in range(5):
            myresult1 = mycursor.fetchone()
            a=list(myresult1)
            l.append(a)
            print (myresult1)
        print (l)
                
        l2=[]
        l3=[]
        for i in range(0,len(l)):
            l2.append(l[i][0])
        y=l2
        for i in range(0,len(l)):
            l3.append(l[i][1])
        z=l3
        plt.plot(y,z,label="SAT SUBJECT SCORE TOPPERS", color='green')
        plt.xlabel("NAMES")
        plt.ylabel("SAT SUBJECT SCORES")
        
        
        plt.legend()
        plt.show()

        
    def nat(self):
        mycursor.execute("SELECT Fullname, Nationality FROM resumemain order by classrank asc")
        n=input("Which nationality do you prefer?")
        l=[]
        myresult1 = mycursor.fetchall()
        for i in myresult1:
            x=list(i)
            for j in x:
                if j==n:
                    l.append(i)
        print (l)

    '''
    NumPy arange() is one of the array creation routines
    based on numerical ranges. It creates an instance of ndarray
    with evenly spaced values and returns the reference to it.

    You can define the interval of the values contained
    in an array, space between them, and their type with
    four parameters of arange():

    numpy.arange([start, ]stop, [step, ], dtype=None)
    '''
    
    def overall(self):
        mycursor.execute("SELECT Fullname, Overall FROM resumemain order by Overall desc")
        l=[]
        for i in range(5):
            myresult1 = mycursor.fetchone()
            a=list(myresult1)
            l.append(a)
            print (myresult1)
        print (l)
        
        l2=[]
        
        l3=[]
        for i in range(len(l)):
            l2.append(l[i][0])
        y=l2

        for i in range(len(l)):
            l3.append(l[i][1])
        z=l3
        plt.bar(y,z,align='center',alpha=0.5,color="")
        plt.title("OVERALL TOPPERS")
        plt.xlabel("NAMES")
        plt.ylabel("OVERALL SCORES")
        plt.yticks(np.arange(0,100,2))
        plt.show()
     
    def extra(self):
        mycursor.execute("select count(Fullname) from resumemain")
        myre=mycursor.fetchone()
        print (myre)
        q=int(myre[0])
        print (q)
        mycursor.execute("select Fullname from resumemain")
        l2=[]
        c=input("Enter what criteria you want to select on:")
        for i in range(q):
            myresult=mycursor.fetchone()
            x=str(myresult[0])
            a=x.split()
            l2.append(a[0])

        print (l2)
        L=[]

        '''
        file.readlines( )
        readlines() returns the complete file as a list of strings
        each separated by \n
        '''
        
        for i in range(len(l2)):
            
            q=str(l2[i])+'.txt'
            print (q)
            f=open(q , "r")
            s1=f.readlines()
            for z in range(len(s1)):
                s=s1[z].split(" ")
                for k in range(len(s)):
                    a=s[k].strip()
                    if a.upper()==c.upper():
                        L.append(l2[i])

            
        print (c,':',L)

        for i in L:
            q=str(i)+'.txt'
            f=open(q , "r")
            f1=f.read()
            print (f1)
                    


                    
    def age(self):
        mycursor.execute("SELECT Fullname, DOB FROM resumemain order by DOB")
        l=[]
        for i in range(5):
            myresult1 = mycursor.fetchone()
            a=list(myresult1)
            l.append(a)
            print (myresult1)
        print (l)

        
        

root = Tk()
App(root)

