#logical operator with conditional statement
#and(Check Whether Given All Conditions Are True)
#or(Check Whether Atleat one Condition is True)
#not(oppsite to give condition)
print("Example for Logical Operator "and"")
print("Example 1 Check Whether give Number Is Positive or Negative")
x=int(input("Enter any Number of x value:"))
y=int(input("Enter any Number of y value:"))
if x>0 and y>0:
    print(f"{x} and {y} are positive number")
else:
    print(f"not both {x} and {y} are positive number")

print("Example 2 Check age and income Eligible for loan")
age=int(input("Enter Candidate's age:"))
income=int(input("Enter Candidate income:"))

if age>18 and income>30000:
    print(f"Congratulation youe age {age} and income {income} is Eligible for loan")
else:
    print(f"Your age {age} and income {income} is not Eligible for loan")

print("Example 3 Check Whether Given Temperature and Humidity is Comfortable")    
temperature=float(input("Enter Temerature :"))
humidity=int(input("Enter Humidity"))
if temperature>20 and humidity<70:
    print(f"The Weather is comfortable at Temperature {temperature} degrees and Humidity {humidity}")
else:
    print(f"The Weather isn't comfortable at Temperature {temperature} degrees and Humidity {humidity}  ")

print("Example 4 Check Whether the given Weight and height is prefered")    
height=float(input("Enter Your Height :"))
weight=float(input("Enter Your Weight :"))
if height>170 and weight<=80:
    print(f"Congratulation You've Prefered Range at {height} cm and {weight} kgs")
else:
    print(f"Sorry You haven't Prefered range, you have {height}cms and {weight} kgs")




print("Example for or logical statement")
print("Example 1 Check Whether Atleast one give number is positive")
x=int(input("Enter any Number of x value:"))
y=int(input("Enter any Number of y value:"))
if x>0 or y>0:
    print(f"Either {x} or {y} is positive number")
else:
    print(f"Both given Numbers or Negative")    

print("Example 2 Check whether age eligible or having permission ")    
age=int(input("Enter Candidate's age:"))
permission=int(input("Enter Candidate having Permission:"))
if age>18 or permission==Yes:
    print("Access Granted")
else:
    print("Access Not Granted")    

print("Example 3 Check Whether Temperature and weather condition are allow to go outside by using or ")    
temperature-float(input("Enter Temperature:"))
weather=input("Enter Weather Condition:")
if temperature>30 or weather==rainy:
    print("Stay indoor due to bad weather....:) ")
else:
    print("You can go OUt There is a good Weather Today..:)")    

print("Example 4 Check Whether the shop is open or close by or operator")
print("Shop Name was MCA Department")
time=int(input("Enter Shop Timings:"))
if time<9 or time>22:
    print("Shop is closed")
else:
    print("Welcome...! Shop is open")    

print("Example1 Cheack Weather condition by using not")    
is_raining=input("Is it raining:")
if is_raining==True:
    if not is_raining:
        print("No need to carry umbrella")
else:
    print("Please carry Umbrella.") 
    

