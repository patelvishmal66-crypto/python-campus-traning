#operators
#Arithmatic = +,-,*,/,//,**,%.

#write a program which will take degree celsius is input and covert it into fahrenheit

# c=int(input(" Enter the degree celcious value"))
# f=(9/5*c)+32
# print("corresponding f value is",f)


# write a program which will take radius as a input and print area of a circle



# r=int(input("Enter the radius of circle"))
# area = 3.14* r**2
# p=2*3.14*r
# print("the area and perimeter of the circle is ",area,"",p)

#write a program which will check if the user can vote or not
# number of all possible option 
# age=int(input("enter the Age"))
# if age>18:
#     print("user can vote")
# else:
#     print("user can not vote")    




# 4...write a program to determine grade based on marks,
# marks>=90: Grade: A
# marks>=80: Grade: B
# marks>=70: Grade: C
# marks>=60: Grade: D
# otherwise,
# Geade: E
# Test Case 1:
# input:50
# output: E

# marks=(int(input("enter the marks:")))
# if marks>=90: 
#     print("Grade: A")
# elif marks>=80:
#     print("Grade: B")
# elif marks>=70:
#     print("Grade: c")
# elif marks>=60:
#     print("Grade: D")
# else:
#       print("Grade:E")




# 7.....W.A.P... to find the  largeest of three number.
# input: enter 3 number:78,56,100
# output:greatest out of 3:1000

# number1=int(input("Enter the the number:"))
# number2=int(input("Enter the the number:"))
# number3=int(input("Enter the the number:"))

# if number1 > number2 and number2 > number3:
#     print("the largest number is",number1)
# elif number2 > number1 and number1 > number2:
#     print("the largest number is",number2)
# elif number3 > number1 and number1 > number3:
#     print("the largest number is",number3)
# else:
#     print("all number is equal.")





# 8....W.A.P...to deteremine if a triagale is equalateral, isosceles or scalene.

# side1=int(input("enter the first side of the triangle: "))
# side2=int(input("enter the first side of the triangle: "))
# side3=int(input("enter the first side of the triangle: "))

# if side1 == side2 and side2 == side3:
#     print("the triangle is equilateral.")
# elif side1 == side2 and side2 == side3 or side1 == side3:
#     print("the triangle is isosceles.")
# else:
#     print("the triangle is scalene.")


# 9......W.A.P to check if given year is leap  or not.
# year=int(input("Enter the year: "))
# if (year % 4 == 0 or  year % 400 == 0) and year % 100 !=0:
#     print(" the year is leap year:",year)
# else:
#     print("the year is not a leap year:",y)
#w
# 
# 
# write a program to input electricity unit charges and calculate total electricity bill
# according to the given sondition
# for first 50 units Rs. 0.50/unit
# for next 150 units Rs. 0.75/unit
# for next 250 units Rs. 1.20/unit 
# for unit abovs 450 Rs. 1.50/unit
# an additionel subcharge of 20% is added to the bill
# test case:
# input:100 units
# excepted output:
# rs.62.5
# with surchang: rs 75

unit=int(input("Enter number of units consumed: "))
if unit <=50:
   bill = unit* 0.50
elif unit <=200:
   bill = (50*0.50)+ (unit-50)*0.75
elif unit<= 450:
   bill = (50*0.50)+ (unit-50)*0.75+(unit-200)*1.20
else: 
   bill = (50*0.50)+ (unit-50)*0.75+(unit-200)*1.20+(unit-450)*1.50

final_bill = bill+bill*0.2

print("Final bill is:",final_bill)









#    W.A.P....a python  program which accept the 