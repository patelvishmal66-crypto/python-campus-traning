print("Hello Global")
print("Hello Global")

x=5
y=7
z=5
print(id(x),id(y),id(z))
y=9
print(id(x),id(y),id(z))

name=input("Enter your name ")
print(name)
age= int(input("Enter your age"))
height = float(input("Enter your height"))
print("My name is  ",name," and my age is ",age,\
    " and height ",height)
#sdfjasd
#My name is   sdfjasd  and my age is  34  and height  34.0
l=int(input("Enter the length"))
w=int(input("ENter the width"))
a=l*w
print("Area of rectangle is ",a)
#Area of rectangle is  200