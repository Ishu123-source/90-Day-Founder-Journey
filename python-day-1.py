# Task 1: introduction program                                                                        

name = "ishu"
age = 23

print("hello", name)
print("you are",age, "years old")

# Task 2: simple calculator

A = int(input("enter first number: "))
B = int(input("enter second number: "))
   
print("Addition =", A + B )
print("subtraction =", A - B ) 
print("Multiplication =", A * B )
print("Division =", A / B )  

# Task 3: area of rectangle

Length = int(input("enter length of rectangle: "))
width = int(input("enter width of rectangle: "))
Area = Length * width

print("area ", Area)

# Task 4: Temperature conversion

celsius = int(input("enter temprature in celcious: "))
farenheit = (celsius * 9/5) + 32
print("temprature in farenheit: ",farenheit)


# Task 5: personal bio generator

name = input("enter your name: ")
age = int(input("enter your age: "))
city = input("enter your city: ")

print("-----BIO-----")
print("Name: ", name)
print("Age: ", age)
print("City: ", city)
print("-------------")