def motto():
    print("Hello this is our motto")
motto()

def addition():
    answer = 10 + 20
    print("Your answer is", answer)
addition()

def sum(x, y, z):
    answer = x + y+ z
    print("Hello your answer is", answer)
sum(323232, 7558878, 876758)
sum(32, 54, 87)

def avg(x, y, z):
    average = (x + y + z) / 3
    return average

myValue = avg(323, 545, 7676)
print(myValue)

# Create a function to calculate the BMI of any person.
# Use formula BMI = weight divide by height squared.
# Check and ascertain that if:
# BMI < 24 ........ Underweight
# BMI< 29 ......... Normal weight
# BMI < 34 ....... Overweight
# else ........ Obese

def BMI(weight, height):
    bmi = weight / pow(height,2)
    bmi = round(bmi,4)
    if bmi < 24:
        print(bmi, "You are Underweight")
    elif bmi < 29 > 23:
        print(bmi, "Your weight is Normal")
    elif bmi < 34 > 28:
        print(bmi, "You are Overweight")
    else:
        print(bmi, "You are Obese")
BMI(80, 1.8)
