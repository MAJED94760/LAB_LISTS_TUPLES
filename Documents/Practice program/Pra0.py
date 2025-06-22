student_grade = 90

if student_grade >= 95:
    print ("you are marke A+")
elif student_grade >= 90:
    print ("you are marke A")
elif student_grade >= 80:
     print ("you are marke B+")
elif student_grade >= 70:
    print ("you are marke B")
else :
    print ("You are failed")


print ("_"*20)

username = input("Enter username:")
pin = input("Enter you pin:")

if username == "Majed" and pin == "12":
    print("Welcome Majed")
    print ("showing menu for Manager")

elif username == "Khaled" and pin == "12":
     print("Welcome Khaleded")
     print ("showing menu for Student")
else:
    print ("not authorized")
