# ==========================================
# Codesaga Day 15
# elif Conditions
# ==========================================


# -------------------------
# Program 1 : Grade Checker
# -------------------------

marks = int(input("Enter Marks : "))

if marks > 100 or marks < 0:
    print("Invalid Marks")
elif marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")


# -------------------------
# Program 2 : Largest Number
# -------------------------

num1 = int(input("Enter First Number : "))
num2 = int(input("Enter Second Number : "))
num3 = int(input("Enter Third Number : "))

if num1 > num2 and num1 > num3:
    print("Largest :", num1)
elif num2 > num1 and num2 > num3:
    print("Largest :", num2)
else:
    print("Largest :", num3)


# -------------------------
# Program 3 : Smallest Number
# -------------------------

if num1 < num2 and num1 < num3:
    print("Smallest :", num1)
elif num2 < num1 and num2 < num3:
    print("Smallest :", num2)
else:
    print("Smallest :", num3)


# ---------------------------------
# Program 4 : Positive / Negative
# ---------------------------------

num = int(input("Enter Number : "))

if num == 0:
    print("Zero")
elif num > 0:
    print("Positive")
else:
    print("Negative")


# -------------------------
# Program 5 : Even / Odd
# -------------------------

num = int(input("Enter Number : "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")


# --------------------------------
# Program 6 : Big Even / Small Even
# --------------------------------

num = int(input("Enter Number : "))

if num > 50 and num % 2 == 0:
    print("Big Even")
elif num <= 50 and num % 2 == 0:
    print("Small Even")
else:
    print("Odd Number")


# ----------------------------------------
# Program 7 : Positive Even / Positive Odd
# ----------------------------------------

num = int(input("Enter Number : "))

if num == 0:
    print("Zero")
elif num < 0:
    print("Negative")
elif num % 2 == 0:
    print("Positive Even")
else:
    print("Positive Odd")