# ========== 2.3.1 ==========
# while True: 
#     answer = input("Shall we continue?")
#     if answer == "no":
#         print("Okay then")
#         break
# # ========== 2.3.2 ==========
# while True:
#     from math import sqrt
#     number = int(input("Please type in a number:"))
#     if number < 0:
#         print("invalid number")
#     else:
#         print(sqrt(number))

#     if number == 0:
#         break
    

# ========== 2.3.3 ==========
# number = 5
# print("Countdown!")
# while True:
#   print(number)
#   number = number - 1
#   if number == 0:
#     break

# print("Now!")

# ========== 2.3.4 ==========
# password1 = input("Password:")
# while True:
#     password2 = input("repeat password:")
#     if password1 == password2:
#         break

# ========== 2.3.5 ==========

# attempts = 0 
# while True:
#     pin = input("PIN:")
#     attempts += 1
#     if pin != "4321":
#         print("wrong")
#     if pin == "4321":
#         break
# if attempts > 1:
#     print("correct! you had", attempts, "attempts")
# if attempts == 1:
#     print("correct! it only took you a single attempt!")

# ========== 2.3.6 ==========
# year = int(input("Year:"))


# ========== 2.3.7 ==========
# word = 0
# allwords = ""
# while True:
#    word = input("Please type in a word:")
#    if word == "end":
#       break
#    else:
#       allwords += word


# print(allwords)

# ========== 2.3.8 ==========
# word = 0
# previous_word = "nothing, yet"
# allwords = ""
# while True:
#    word = input("Please type in a word:")
#    if word == "end" or word == previous_word:
#       break
#    else:
#       allwords += word

#    previous_word = word

# print(allwords)

# ========== 2.3.9 ==========
allnumbers = 0
sumofnums = 0
meanofnum = 0
negative =0
positive = 0
while True:
   number = int(input("please type in integer numbers"))
   if number == 0:
      break
   else:
      allnumbers += 1
      sumofnums += number
      meanofnum = sumofnums / allnumbers
      if number > 0:
         positive += 1
      if number < 0:
         negative += 1
print("numbers typed in:", allnumbers)
print("the sum of numbers:", sumofnums)
print("the mean of numbers:", meanofnum)
if number > 0:
         positive += 1
print("positive numbers:", positive)
if number < 0:
         negative += 1
print("negative numbers:", negative)
