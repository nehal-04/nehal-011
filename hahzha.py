#binary file
import pickle
import os
def create():
    f=open("abc.dat","wb")
    while True:
        e=eval(input("Enter Employno, Name, Salary, Deptt & Phoneno"))
        pickle.dump(e,f)
        ch=input("Wanna Continue?(Y/N)")
        if ch in 'Nn':
            break
    f.close()
        
#DISPLAY 
def display():
    f=open("abc.dat","rb")
    try:
        while True:
            l=pickle.load(f)
            print(l)
    except EOFError:
        f.close()

#SEARCH FOR AN EMPLOYEE USING HIS EMPLOYEE NO.
def q3():
    f=open("abc.dat","rb")
    flag=False
    num=int(input("Enter the employee no."))
    try:
        while True:
            e=pickle.load(f)
            if e[0]==num:
        
                print(e)
                break
    except EOFError:
        f.close()
        
        print("NOT FOUND")

#SEARCH FOR AN EMPLOYEE USING HIS NAME
def q4():
    f=open("abc.dat","rb")
    n=input('name?')
    try:
        while True:
            e=pickle.load(f)
            if e[1]==n:
                
                print(e)
                break
    except EOFError:
        f.close()
        print("NOT FOUND")

#DISPLAY EMPLOYEES OF A GIVEN DEPTT AND COUNT THEM
def q5():
    c=0
    f=open("abc.dat","rb")
    flag=False
    n=input("Name of the Department-")
    try:
        while True:
            emp=pickle.load(f)
            if emp[3]==n:
                flag=True
                print(emp)
                c+=1
                print("Total employees in the dept", ":",c)
    except EOFError:
        f.close()
        if flag==False:
            print("Dept. not found!")
            
#SEARCH FOR AN EMPLOYEE USING PHONE NO.
def search3():

    f=open("abc.dat","rb")
    num=int(input('enter phh no'))
    try:
        while True:
            emp=pickle.load(f)
            if emp[4]==num:
                print(emp)
                break
    except EOFError:
        f.close()
        print('phoen number not found')
        
#SEARCH FOR AN EMPLOYEE WITH HIGHEST SALARY
def search4():
    f=open("abc.dat","rb")
    hsal=0
    c=[]
    try:
        while True:
            emp=pickle.load(f)
            if emp[2]>hsal:
                hsal=emp[2]
                c=emp
    except EOFError:
        f.close()
        print("Details of employee having the highest salary,",c)
        
#DELETE AN EMPLOYEE USING EMPLOYEE NO.
def deleteemployee():
    f=open('abc.dat','rb')
    n=open('new.dat','wb')
    num=int(input('enter emply no for deletion'))
    try:
        
        while True:
            l=pickle.load(f)
            if l[0]!=num:
                pickle.dump(l,n)
            else:
                pass
    except EOFError:
        f.close()
        n.close()

    os.remove('abc.dat')
    os.rename('new.dat','abc.dat')


#DELETE EMPLOYEES WHOSE SALARY<50000  <<<=

def del2():
    f=open('abc.dat','rb')
    n=open('new.dat','wb')
    try:
        while True:
            l=pickle.load(f)
            if l[2]>=50000:
                pickle.dump(l,n)
            else:
                pass
    except EOFError:
        f.close()
        n.close()

    os.remove('abc.dat')
    os.rename('new.dat','abc.dat')




#APPEND A NEW EMPLOYEE
def append():
    f=open("abc.dat","ab")
    emp=input("Enter Employno, Name, Salary, Deptt & Phoneno")
    pickle.dump(emp,f)
    f.close()

def upd():
    f=open('abc.txt','wb')





#update

def upd(num):
    f = open('abc.dat', 'rb+')
    try:
        while True:
            pos = f.tell()
            l = pickle.load(f)
            if l[0] == num:
                l[2] = l[2] + 0.10 * l[2]
                f.seek(pos)
                pickle.dump(l, f)
                print(l)
                break
    except EOFError:
        print('rec not found')

    f.close()
        
    
          
