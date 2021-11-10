for i  in range (1,101):#for proper output i made more than one loops
    print (i,end=" ");#just showing numbers on screen
print(" ");#print space
print("Multiples of 3 are");#a proper message for output  
print(" ");#space
for f in range(1,101):#loop for a multiple of 3
    if(f%3==0):#check
        print(f," ","Fizz");#output
print(" ");#print space
print("Multiples of 5 are");#a proper message for output  
print(" ");#space
for z in range(1,101):
    if(z%5==0):
        print(z," ","Buzz");
print(" ");#print space
print("Multiples of3 and 5 are");#a proper message for output  
print(" ");#space
for z in range(1,101):
    if(z%3==0and z%5==0):
        print(z," ","Fizz"," ","Buzz");

