import os
f_name=input('Enter file_name plz: ')
def write(f_name):
    f=False
    c=input('Enter ur text u want to enter in the file :')
    file=open(f_name,"w")
    file.write(c)
    file.close()
    #file.write(close)
    f=True
    return f
def check_(f_name):
    x=False
    if os.path.isfile(f_name):
        x=True
    return x
def choice_():
    print("choose 1")
    print('\n')
    print("press 1 for read")
    print("press 2 for delete")
    print("press 3 for append")
    x=int(input())
    return x
def read_file(f_name):
    file=open(f_name,"r")
    z=file.read()
    file.close()
    print(z)
    #return z
def append_file(f_name):
    x=input("Enter the text u want to enter in the file :")
    file=open(f_name,"a")
    file.write(x)
    file.close()
def del_(f_name):
    file=open(f_name,"w")
    file.write('\0')
    file.close()
a=check_(f_name)
if(a==False):
    c=write(f_name)
    #print(c)
    if(c==True):
        print("Data enter sucessfully")
else:
   f=choice_();
   if(f==1):
       read_file(f_name)
   elif (f==3):
       append_file(f_name)
   elif(f==2):
       del_(f_name)
       print("The data of the file is deleted")
   else:
       
        print("You selected a wrong choice")

      
    

    

    







