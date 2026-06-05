total = int(input("Enter the total number of classes - "))
attended= int(input("Enter the number of classes attended - "))

percentage = attended/total*100

if percentage<=80:
    print("You are allowed to sit in the exam")
else:
    print("You will not be allowed to sit in the exam")