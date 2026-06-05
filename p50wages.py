gender = input("Enter the Gender (male/female) - ").strip().lower()
age = int(input("Enter the age - "))

if 18 < age < 30:
    if gender == 'male':
        print("The wages you will get is 700 per day")
    else:
        print("The wages you will get is 750 per day")
elif 30 <= age <= 40:
    if gender == 'male':
        print("The wages you will get is 800 per day")
    else:
        print("The wages you will get is 850 per day")
else:
    print("Enter a valid age")
