print("########## 1.4.1 ##########")
digit = int (input("please type a number:"))
print(digit, "*", "5", "=", digit*5)
print("########## 1.4.2 ##########")
name = input("What is your name?")
year = int(input("Which year were you born?"))
age = 2024-year
print("Hi", name, "you will be", age, "years old at the end of 2024.")


print("########## 1.4.3 ##########")
days = int(input("how many days?"))
print ("secomds in that many days:", days*86400)

print("########## 1.4.4 ##########")
# Fix the code
number1 = int(input("Please type in the first number: "))
number2 = int(input("Please type in the second number: "))
number3 = int(input("Please type in the third number: "))

product = number1 * number2 * number3

print("The product is", product)

print("########## 1.4.5 ##########")
number4 = int(input("please type in number:"))
number5 = int(input("please type in number:"))
sum = number4 + number5
product = number4 * number5
print("the sum is, ", sum)
print("the product is:", product)
print("########## 1.4.6 ##########")
number1 = int(input("please type in first number:"))
number2 = int(input("please type in second number:"))
number3 = int(input("please type in third number:"))
number4 = int(input("please type in fourth number:"))
sum = number1 + number2 + number3 + number4
mean = (number1 + number2 + number3 + number4) / 4
print("the sum of the numbers is ", sum, "and the mean is ", mean)
print("########## 1.4.7 ##########")
times_eaten = float(input("How many times a week do you eat at the student cafeteria?"))
price_of_food = float(input("What is the price of a typical student lunch?"))
groceries = float(input("How much do you spend on groceries in a week?"))
daily = (times_eaten * price_of_food + groceries) / 7
weekly = times_eaten * price_of_food + groceries
print("Average food expenditure:")
print("Daily:", daily)
print("Weekly:", weekly)
print("########## 1.4.8 ##########")
number_in_course = int(input("How many students on the course?"))
number_in_group = int(input("desired group size?"))
print("Number of groups formed", number_in_course // number_in_group)
