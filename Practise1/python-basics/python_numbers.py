x = 1 #int type 
y = 1j #complex 
z = 1.59348 #float 

#if we want to know which type of variable we are working with

print(type(x)) #result int 
print(type(y)) #result complex 
print(type(z)) #result float 
#and also we can convert variable to different one \

a = float(x)
print(a) # result 1.0

#and we want to take random number from some interval we can use func import 
import random 
print(random.randrange(10)) # it will show us random int from 0 to 9 
