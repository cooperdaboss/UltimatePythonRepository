
# print("########## 1.5.1 ##########")
# number = int(input("please type number:"))
# if number == 1984:
#     print("orwell")
# print("########## 1.5.2 ##########")
# number = int(input("please type in a number:"))
# if number < 0:
#     print("the absolute value of that number is", number * -1)
# print("########## 1.5.3 ##########")
# name = input("what is your name?")
# if name != ("jerry"):
#     portions = int(input("How many portions?"))
#     print("The total cost is:", portions * 5.90)
# print("Next please!")

# print("########## 1.5.4 ##########")
# number = int(input("please type in number:"))
# if number < 1000:
#     print("this number is smaller than 1000")
# if number < 100:
#     print("this number is smaller than 100")
# if number < 10:
#     print("this number is smaller than 10")
# # print("########## 1.5.5 ##########")
# number1 = int(input("number 1:"))
# number2 = int(input("number 2:"))
# operation = (input("operation:"))
# if operation == ("add"):
#     print(number1, "+", number2, "=", number1+number2)
# if operation == ("multiply"):
#     print(number1, "*", number2, "=", number1*number2)
# if operation == ("subtract"):
#     print(number1, "-", number2, "=", number1-number2)
# print("########## 1.5.6 ##########")
# tempF = int(input("type in a tempurature (F):"))
# tempC = (tempF - 32) * 5/9
# print(tempF, "degrees fahrenheit equals", tempC, "degrees celcius")
# print("########## 1.5.7 ##########")
# hourlywage = float(input("hourly wage:"))
# hoursworked = float(input("hours worked:"))
# dailywages = hourlywage * hoursworked 
# dailysunday = dailywages * 2
# if day == ("Sunday"):
#     print("daily wages:", dailysunday)
# if day != ("Sunday"):
#     print("daily wages:", dailywages)
print("########## 1.5.8 ##########")
# Fix the program
points = int(input("How many points are on your card? "))
if points < 100:
    points *= 1.1
    print("Your bonus is 10 %")

if points >= 100:
    points *= 1.15
    print("Your bonus is 15 %")

print("You now have", points, "points")

# print("########## 1.5.9 ##########")
