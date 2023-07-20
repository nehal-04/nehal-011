#BINARY PART -2 
import pickle
import os
def create1():

    f=open ('xyz.dat','wb')

    while True:
        d={}
        y=eval(input("enter adno , name , mrk1 , mrk2 , mrk3"))
        d[y[0]]=(y[1],y[2],y[3],y[4])
        pickle.dump(d,f)
        ans=input("Want to continue? ")
        if ans in 'Nn':
            break

    f.close()

def display():
    f=open("xyz.dat","rb")
    try:
        while True:
            e=pickle.load(f)
            print(e)
    except EOFError:
        f.close()

def q3(num):
    f=open("xyz.dat","rb")
    try:
        while True:
            l=[]
            e=pickle.load(f)
            l=e.keys()
            for x in l:
                
                if x == num:
                    print('found')
                    print(e)
                    break

    except EOFError:
        pass
    f.close()
def q4():
    f=open("xyz.dat","rb")
    c=0
    try:
        while True:
            l=[]
            e=pickle.load(f)
            l=e.values()
            for x in l:
                
                if x[1]>=90:
                     c+=1
                     print(e)

    except EOFError:
        f.close()

def q5(mark1):
    f=open('xyz.dat','rb+')
    try:
        while True:
            a=[]
            d={}
            pos=f.tell()
            e=pickle.load(f)
            a=d[e]
            x=list(a)
            l=e.keys()
            s=str(l)
                   
            if x[1]==mark1:
                        
                    x[1]=x[1]+5
                    y=tuple(x)
                    f.seek(pos)
                    d[s]=y
                    pickle.dump(d,f)
                    flag = True
                    break
    except EOFError:
        f.close()
    if flag==False:
        print('rec not found')
    else:
        display()


