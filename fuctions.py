#Here Functions In Pythion 
#some functions are already defined for programmers those are known as ---Built-in Function---
print(len("Hello World"))
print(ord("B")) #etc.
#some functions are inside the module so whenerve we import modules then those ---inside-module Function--- can be used 
import math as m
f = m.floor(567.2312)
print("Floor Value = ",f)
#and then in the end there some functions made by programmer for there own use
def hi():  #Function Header 
    print("Hii") #Function Body
    return     #return satement also ending of function line 
print("main Body")
hi()  #Function call satement 
#fuction for sum of 2 numbers
def s(a=1,b=1):  #(a,b) = parameters
    sum=a+b
    print(sum)
    return
s(b=2,a=3) #(2,3) = arguments
s(12,12)
s(11,11)
#Now Types Of Arguments
#positional
#defualt 
#keywords
#functions of plindrom
