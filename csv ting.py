import csv
def create():
    f=open('broheyy.csv','w',newline='')
    w=csv.writer(f)
    fields = ['name','age','qualification','experience(in yrs)']
    w.writerow(fields)
 
    while True:
        l=eval(input('name,age,qual,exp'))
        w.writerow(l)
        ans=input('more records')
        if ans in 'Nn':
            break
    f.close()

#display
def display():
    with open('broheyy.csv','r')as f:
        data=csv.reader(f)
        for rec in data:
            print(rec)

# search using given rollno-

def searchnum(num):
    with open('broheyy.csv','r')as f:
        data=csv.reader(f)
        c=0
        for x in data:
            if c==0:
                c+=1
            else:
                if int(x[1])==num:
                    print(x)
        
                
# append
def appnd():
    with open('broheyy.csv','a',newline='')as f:
        w=csv.writer(f)
        while True:
            l=eval(input('enter new records'))
            w.writerow(l)
            ch=input('wanna enter more records?')
            if ch in 'Nn':
                break

#display under 30
def dispunder30():
    with open ('broheyy.csv','r')as f:
        data=csv.reader(f)
        c=0
        for rec in data :
            if c==0:
                c+=1
            else:
                if int(rec[1])<30:
                    print(rec)
                else:
                    pass

# increase experinece by 1
'''def inc1():
    with open ('broheyy.csv','r') as f:
        d=list(csv.reader(f))
    with open('broheyy.csv','w',newline='') as f:
       w=csv.writer(f)
       r=0
       for rec in d:
           if r==0:
               r+=1
           else:
               rec[3]=str(int(rec[3]+1))
           print(rec)
           w.writerows(d)


def inc():
    with open("emp.csv","r") as f:
        data=list(csv.reader(f))
    with open("emp.csv","w",newline="") as f:
        c=0
        f=0
        for rec in data:
            if c==0:
                c+=1
            else:
                f=int(rec[3])+1
                rec[3]=f
                print(rec)'''


#delete
'''def delete():
    n=input('name?')
    a=input('age?')
    with open('broheyy.csv','r') as f:
        d=list(csv.reader(f))
    with open('broheyy.csv','w',newline='') as f:
        for i in range(1, len(d)):
            if d[i][0] == n and int(d[i][1]) == a:
                del d[i]
                print('rec deleted successfully')
                break
        else:
            print('record not found')
        w = csv.writer(f)
        w.writerows(d)
    display()

'''    
    
