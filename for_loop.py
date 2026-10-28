# #Here are looooops guysssssssss 
# #loops in python allow us to execute a block of code multiple times without rewriting it 
# #There are 2 types of loop 
#for loop --> work based on ranges
#range(start,stop,step)
a = range(5)
for i in a:   #Here i is a itrator which itrate over range 
    print(i,"Hii") 

for i in range(16,0,-1):
    print(i)

for i in range(20,51):
    print(i)

for i in range(-5,-16,-1):
    print(i)

table =int(input("kiski table chaiye ? \n "))
for a in range(1,11,1):
    print(f"{table} * {a} = {table * a}")

a = "Ankit is a good boy "

for i in range(len(a)):
    print(a[i])

for t in a:
    print(t)

#Break and Continue 
for i in range(1, 21):
    if i == 15:
        continue  
    print(i)

for i in range(1, 21):
    if i == 15:
         break
    print(i)

for i in range(1, 21):
     if i == 12:
           print("Break statement is executed")
           break
     print(i)
else:
      print("Break statement is not executed")

#quizz for loop
num = int(input("give me an Integer ? \n"))
for i in range(num):
    print("Hello world")
print("---x---")
for i in range(1,num+1):
    print(i)
print("---x---")
for t in range(num,0,-1):
    print(t)
print("---x---")   
for i in range(1,11,1):
    print(f"{num} * {i} = {num * i}")
print("---x---")
sum = 0 
for r in range(1,num+1):
    sum += r 
print(f"Sum of {num} is = {sum}")
print("---x---")
facto = 1 
for i in range(1,num+1):
    facto *= i
print("Factorial of",num,"numbers is = ", facto)
print("---x---")
even_sum = 0
odd_sum = 0
num1 = int(input("give me an Integer ? \n"))
for x in range(1,num1+1):
    if x%2 == 0:
        even_sum += x
    else:
        odd_sum += x
print(f"Sum of all even no. = {even_sum} \n Sum of all odd no. = {odd_sum}")
print("---x---")
num2 = int(input("give me a number ? \n"))
for i in range(1, num2+1):
    if num2%i == 0:
        print(i)
print("---x---")
fact = 0
num3 = int(input("check your number is perfect or not = "))
for i in range(1,num3):
    if num3%i==0:
        fact += i
        print(fact)
if fact == num3:
    print(f"Yes the number {num3} is a perfect number")
else:
    print("It is not a perfect number")

print("---x---")
name = input("Enter a string value = ")
for g in range(len(name)-1,-1,-1):
    print(name[g])
print("---x---")
#Checking Plindrom
word = input("Enter a word = ")
chk = ""
for g in range(len(word)-1,-1,-1):
    chk += word[g]
if  word == chk:
    print(f"The word {word} is a Plindrom")
else:
    print(f"The word {word} is not Plindrom")
print("---x---")
combi = input("Enter your password = ")
char = 0
digit = 0
symbol = 0
for i in combi:
    if i.isdigit() == True :
        digit += 1
    elif i.isalpha() == True:
        char += 1
    else:
        symbol += 1
print("Charactors = ",char)
print("Digits = ",digit)
print("Symbols = ",symbol)