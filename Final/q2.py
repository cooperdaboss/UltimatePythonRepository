quarter = 25
dime = 10
nickle = 5
amount_due = 50
while True:
    print("amount due:", amount_due)
    coin = int(input("Insert coin:"))
    if coin == quarter:
        amount_due - quarter
    elif coin == dime:
        amount_due - dime
    elif coin == nickle:
        amount_due - nickle
    else:
        print("Error - this coin type not accepted")
    if amount_due == 0:
        break