print("Namaste Sarthak")

a=None
print("type of a none type variable : ",type(a))
print("Not False ka o/p: ",not False)
print("Not True ka o/p: ",not True)

# Implicit type conversion
var1=100
var2=2.366
print(var1+var2)

# type casting (explicit)
var3="2000"
varT=int(var3)
var4=1000
print(varT+var4)


# Input in python (taking input from user)
# Result of input is always a string By Default
name=input("Enter your Name: ")
print("Namaste,",name)

# If we expect a integer input then we need to mention while declaring input
age=int(input("Enter your Age: "))
print("You are",age,"years old")