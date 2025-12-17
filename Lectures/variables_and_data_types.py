greeting = "Hello"
name = "Marian"
age = 24

print(type(greeting))  # <class 'str'>
print(type(age))       # <class 'int'>

#Data type represent the type of value a variable holds.

#Python is a dynamically typed language, meaning you don't need to declare
#the data type of a variable explicitly. The interpreter infers the type
#based on the value assigned to the variable. So its more like the value has
#the type rather than the variable itself. But it also mean that you can
#reassign a variable to a value of a different type later in the code.

age = "2 years"

print(age)        # 2 years
print(type(age))  # <class 'str'>

age = 24 

#Python is strongly typed, meaning that it enforces type constraints.
#You cannot perform operations that are not supported between different
#data types without explicit conversion. For example, you cannot concatenate
#a string and an integer directly.
print(name + " is " + age + " years old.") # This will raise a TypeError
# TypeError: can only concatenate str (not "int") to str
