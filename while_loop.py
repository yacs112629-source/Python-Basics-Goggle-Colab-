#while loop --> it repeats a block of code as long as conditions is True 
'''while condition:
     code to execute'''
a = 1
while a <= 10:
    print(a,"Hii")
    a += 1
#While loop quetions 
a = int(input("Tell your number = "))
while a > 0:
    print(a%10)
    a //= 10
print("----x----")
a = int(input("Tell your number = "))
rev = 0
while a > 0:
    rev = rev*10+a%10
    a //= 10
print(rev)
print("----x----")
a = int(input("Tell your number = "))
copy = a
rev = 0
while a > 0:
    rev = rev*10+a%10
    a //= 10
if copy == rev:
        print(f"Yes the number {copy} is a plindrom")
else:
        print(f"No the number {copy} is not plindrom")