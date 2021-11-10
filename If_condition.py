mes1="The temperature is not too high so u need to be ur pajamas"# this is for proper output message
mes2="The temperature is high so u need to be ur pajamas"# this is for proper output message
def heo():#function
    temperature=30
    pajam ="off"
    time =False
    if temperature>30 and time ==False:#applying if condition with and operator
        #temperature=40
        pajam="on"
    return pajam
def heol():
    temperature=31#local variable
    pajam ="off"#local variable
    time =False#local variable
    if temperature>30 and time ==False:#again applying if condition with and operator but this time value ubdates
        #temperature=40
        pajam="on"
    return pajam#returning value
p=heo()#calling function
f=heol()#calling function
print(mes1,p)#output
print(mes2,f)#output




