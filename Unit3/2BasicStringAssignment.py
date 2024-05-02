# ========== 3.2.1 ==========
# string = input("Please type in a string:")
# amount = int(input("Please type in amount:"))
# print(string * amount)

# ========== 3.2.2 ==========
# string1 = input("Please type in string 1:")
# string2 = input("please type in string 2:")
# len(string1)
# len(string2)
# if string1 > string2:
#     print(string1, "is longer")
# else:
#     print(string2, "is longer")

# ========== 3.2.3 ==========
# string = input("please enter a string:")
# position = len(string) - 1

# while True:
#     print(string[position])
#     position = position - 1
#     if position == -1:
#         break

# ========== 3.2.4 ==========
# string = input("Please enter a string:")
# print(string[1])
# letter1 = (string[1])
# print(string[len(string)-2])
# letter2 = (string[len(string)-2])
# if letter1 == letter2:
#     print("the second letter and the second to last letter are ", letter1)
# else:
#     print("the second letter and the second to last letter are different")

# ========== 3.2.5 ==========
# number = int(input("Width:"))
# letter = ("#")
# print(number * letter)

# ========== 3.2.6 ==========
# number = int(input("Width"))
# letter = ("#")
# hight = int(input(""))
# count = 0
# while True:
#     print(number * letter)
#     count = count + 1
#     if count == hight:
#         break


# ========== 3.2.7 ==========
# string = input("Please enter string:")
# print(string)
# print("-"*len(string))

# ========== 3.2.8 ==========
# string = input("Please type in a string:")
# number_of_stars = 20 - len(string)
# print(number_of_stars * "*" + string)


# ========== 3.2.9 ==========
word = input("Word:")

stars = "*" * 30
print(stars)

### this!
number_of_spaces = 30 -2 - len(word)
numberofleftspaces = number_of_spaces // 2
leftspaces = " " * numberofleftspaces
numberofrightspaces = number_of_spaces // 2

print("*" + leftspaces + word + leftspaces +"*")
###

print(stars)

