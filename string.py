college = "IIT Kanpur"

#Strings can store any sequence of characters enclosed in single or double quotes
print(college)
print(ord(college[0])) #ord() function returns the unicode code point for a given character
print(len(college[4])) #len() function returns the length of the string
indexing = college.index("K") #index() function returns the index of the first occurrence of a specified value
print(indexing)
print(college[0:3]) #slicing the string from index 0 to 2 [Start : Stop : Step]

#Type conversion 
a = 12
b = str(a) #converting int to str
print(type(b))

#bool convert values in false and true only 
#there are 2 vales 1> Falsy --> False, 0, None, [], {}, ""
#and rest of them is Truthy values

#Explicit type conversion = when we convert one data type to another data type using built-in functions like int(), str(), float(), etc.
#Implicit type conversion = when we convert one data type to another data type without using any built-in functions. This is done automatically by Python when we perform operations on different data types.
