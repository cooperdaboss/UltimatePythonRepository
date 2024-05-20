first_name = input("please enter your first name:")
last_name = input("please enter your last name:")
gpa = float(input("please enter your GPA:"))

if gpa >= 3.86:
    print("Hello, ", first_name, "you should report to school on Tuesday and Friday. you are eligible for a scholarship of 16,000")
if gpa <= 3.85 and gpa >= 3.7:
    print("Hello, ", first_name, "you should report to school on Tuesday and Friday. you are eligible for a scholarship of 12,000")
if gpa <= 3.69 and gpa >= 3.5:
    print("Hello, ", first_name, "you should report to school on Tuesday and Friday. you are eligible for a scholarship of 8,000")
if gpa <= 3.49 and gpa >= 3.25:
    print("Hello, ", first_name, "you should report to school on Tuesday and Friday. you are eligible for a scholarship of 4,000")
if gpa < 3.25:
    print("Hello, ", first_name, "you should report to school on Monay and Thursday. you are eligible for a scholarship of 0")


