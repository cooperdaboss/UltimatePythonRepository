# ========== 3.3.1 ==========
# word = input("Please trpe in a word:")
#         0123456
# word = "example"

# letters = 1
# lastposition = len(word) + 1
# while True:
#     print(word[:letters])
#     letters += 1
#     if letters == lastposition:
#         break

# ========== 3.3.2 ==========
# word = input("Please type in a string:")
# letters = len(word) - 1
# lastposition = len(word) 
# while True:
#     print(word[letters:])
#     letters -= 1
#     if letters == -1:
#         break

# ========== 3.3.3 ==========
# string = input("Please enter a string:")


# a_pos = string.find("a")
# e_pos = string.find("e")
# o_pos = string.find("o")
# if a_pos > -1:
#     print("a found")
# else:
#     print("a not found")
# if e_pos > -1:
#     print("e found")
# else: 
#     print("e not found")
# if o_pos > -1:
#     print("o found")
# else:
#     print(" o not found")

# ========== 3.3.4 ==========
# word = input("Please type in a word:")
# letter = input("Please type in a character:")
# let_pos = word.find(letter)
# if len(word) - let_pos >= 3:
#     print(word[let_pos:let_pos+3])
# else:
#     print()

# ========== 3.3.5 ==========
# skip this one

# ========== 3.3.6 ==========
# word = input("please enter a string:")
# sub_string = input("Please type in a sub string:")
# sub_pos = word.find(sub_string)
# part = word[ sub_pos + 1: ]
# first = sub_pos
# second = part.find(sub_string) + first + 1
# if second >= 0:
#     print("the second occurence of the sub string is at indext", second)
# if second <= -1:
#     print("the sub string does not occur twice in the string")

# if sub_string # if it's in the word
