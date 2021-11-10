mes1="Genre of this song is"#use this for showing proper output
mes4="And the artist of this song is"#use this for showing proper output
mes="And this song is released in"
def genre():#making function
    mes2="folk"#declaring local variable
    return mes2#returing value
def artist():#making function
     mes2="El professor"#local varaible
     return mes2
def year():#function
    mes2=2012#local variable
    return mes2
mes3=genre()#calling function
mes5=artist()#calling function
mes6=year()#calling function
print(mes1,mes3)
print(mes4,mes5)
print(mes,mes6)
