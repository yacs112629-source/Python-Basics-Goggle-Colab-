#if-else 
#program
a = int(input("Enter no: "))
if a > 10:
    print("I will do Task A")   #Indentation is spacing in a block of code 
else:
    print("I will do Task B")    

#program 
money = float(input("Enter how much money ?\n "))
if money == 10:
    print("I will have a crispello")
else:
    print("I will have crispello and O'yes")

#if-elif-else
#program
light = input("Colour of trafic light ?\n ")
if light == "red":
    print("Stop")
elif light == "yellow":
    print("Get-Redy")
elif light == "green":
    print("Goooo")  
else:
    print("Invalid colour !!")       

#quizz
num_1 = int(input("number 1 = "))
num_2 = int(input("number 2 = "))
if num_1 > num_2:
    print(f"{num_1} is grater than {num_2} ")
elif num_2 > num_1:
    print(f"{num_2} is grator than {num_1}")    
else:
    print("Both numbers are equal")    

print("Choose your gender\n 1> Male  2> Female")
choose = int(input("chosse 1 or 2 ?\n "))
if choose == 1:
    print("Good Morning Sir")
else:
    print("Good Morning Mam")    

integer = int(input("Enter a number = "))
if integer%2 == 0:
    print(f"{integer} is a even number ")
else:
       print(f"{integer} is odd number")  

age = int(input("Enter you age ? \n "))
if age < 18:
      print("No you can't vote")
else:
      print("Yes you can vote")   

# Take integer input from the user
year = int(input("Enter a year: "))

# Check the leap year conditions
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

#if-elif-else Ladder 
t = int(input('pls tell the temprature = '))
if t < 0:
    print("Frezzing cold !!")
elif t >= 0 and t < 10:
    print("Very cold")
elif t >= 10 and t < 20:   
    print("Cold")
elif t >= 20 and t < 30: 
    print("Plesent")   
elif t >= 30 and t < 40:
    print("Hot")    
else:
    print("Very hot")