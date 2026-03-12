# integer type variables and also multiple values below 


x , y , z = 2 , 3 , 6

print (x , y , z, end = "\n")

# float ones
  
e , d = 7.9 , 3.6
print (e, d)

#string type variables 

f ,c = "lal ", 'kun '
print(f, c)

#Case-Sensitive 

a = 8 
A = "Kun"
print(a)
print(A)

#variable names 

MyName = "Iskandar"
my_name = "Iskan"

print(MyName)
print(my_name)

#List type

fruit = ["apple ", "banana " , "cherry"]

#after declaring again same things like x it will change no latest one 
 
print(fruit)

#global variables 

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

# Tuple

coordinates = (10, 20)
print("Tuple:", coordinates)
