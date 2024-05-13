# ========== 3.4.1 ==========
# def seven_dwarves():         
#     print("bashful")
#     print("Doc")
#     print("Dopey")           
#     print("Grumpy")    
#     print("Happy")
#     print("Sleepy")
#     print("Sneezy")                                          
# seven_dwarves()
# # ========== 3.4.2 ==========
# def first_character(word):
#     print(word[0])
# first_character('python')
# first_character('yellow')
# first_character('tomorrow')
# first_character('heliotrope')
# first_character('open')
# first_character('night')




# ========== 3.4.3 ==========


# def mean(num1, num2, num3): 
#     print((num1 + num2 + num3) / 3)
    
# mean(5, 3, 1)

#========== 3.4.4 ==========   
# def print_many_times(text, times):
#     counter = 1
#     while True:
#         print(text)
#         counter = counter + 1
#         if counter == times +1:
#             break

# text = "hi"
# times = 5
# print_many_times(text, times)
#========== 3.4.5 ==========
# def hash_square(length):
#     counter = 1 

#     while True:
#         print("#" * length)
#         counter = counter + 1
#         if counter == length +1:
#             break

# hash_square(3)

        
#========== 3.4.6 ==========
def chessboard(length):
    counter = 1
    while True:
        print("10" * length)
        counter = counter + 1
        if counter == length:
            break
chessboard(3)