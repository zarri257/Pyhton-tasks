uniquelist=[]#creating golobal list
mes="value is already present in the list so the result is"#just a message for proper output
mes1="values of list"#just a message for proper output
mes2="values of list after adding"#just a message for proper output
mes4="value is not present in the list so the result is"#just a message for proper output
def add(uniquelist):#function
    uniquelist=[1,2,3,4,5]#adding elements in the list
    return uniquelist#retur list
uniquelist=add(uniquelist)#calling function
print(mes1,uniquelist)#print list
def check(uniquelist):#again making a function check wheather the element present or not
    x=True
    f=1
    if(uniquelist[0]==f):#applying condition
        x=False
    return x#return value
def check1(uniquelist):#again making a function for a check
    x=True
    f=6
    if(uniquelist[4]==6):#apply if condition
        x=False
    return x#return result

helo1=check(uniquelist)#calling function
print(mes,'',helo1)#output
helo2=check1(uniquelist)#calling function
print(mes4,helo2)#print output
if(helo2==True):#addind value in list
    uniquelist.append(6)
print(mes2,uniquelist)#last output







