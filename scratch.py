import random

print("before loop")
num = random.randint(1, 2)
counter = 10
while True:
    counter = counter - 1
    print("inside loop")
    if counter == 3:
        break

print("after loop")

if num == 1:
    print("num = 1")

if num == 2:
    print("num = 2")

print("num is", num)