"""
#Simple way
name = "Ayush"
number = len(name)*9

#Ptinting Your name and lucky number 
print("Hello "+name+"Your lucky number is "+str(number))

"""

#Using a function

def lucky_number(name): 
    number = len(name)*9    
    print("Hello "+ name +". Your Lucky number is: "+ str(number))

lucky_number("Ayush")
lucky_number("Yush")