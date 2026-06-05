height=float("Enter the height in meters -> ")
weight = float("Enter the weight in kilograms -> ")

BMI = weight/height*height

if BMI<18.5:
    print("You are underweight")
elif BMI<25:
    print("You are normal weight")
elif BMI<30:
    print("You are slightly obese")
elif BMI<35:
    print("You are obese")
else:
    print("You are clinicaly obese")