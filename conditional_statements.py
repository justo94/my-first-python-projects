# this is an if statement
age = int(input("Enter your age\n"))
if age < 20:
    print("Sorry, you can't attend this party")
else:
    print("Welcome to the party")
age = 20
if age < 20:
    print("Sorry, you can't attend this party")
else:
    print("Welcome to the party")
    # simple interest calculator
principle = float(input("Enter your principle\n"))
rate = float(input("Enter your rate\n"))
time = float(input("Enter your repayment period\n"))
simpleInterest =(principle * rate * time) / 100
if simpleInterest <= 1000:
    print("The loan is affordable")
elif simpleInterest <= 2000:
    print("The loan is expensive")
else:
    print("This is a scam")
    # grading system
marks = int(input("Enter your marks\n"))
if marks >= 80:
    print("Your grade is A\n Distinction")
elif marks >= 70 < 80:
    print("Your grade is B\n First Class Upper")
elif marks >= 60 < 70:
    print("Your grade is C\n Second Class Lower")
elif marks >= 50 < 60:
    print("Your grade is D\n Credit")
elif marks >= 40 < 50:
    print("Your grade is E\n Ordinary Pass")
else:
    print("Your grade is F\n Fail")



