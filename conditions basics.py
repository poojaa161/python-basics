#if statement
age = 18
if age>=18:
    print("eligible to vote")

#if else statement
num = 56
if num %2 == 0:
    print("even")
else:
    print("odd")

#if elif else statement
marks = 75

if marks >= 90:
    print("Grade A")
elif marks >= 70:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")

#Nested if else 
username = "poojaa"
password = "1234"

if username == "poojaa":
    if password == "1234":
        print("Login successful")
    else:
        print("Wrong password")
else:
    print("Wrong username")
