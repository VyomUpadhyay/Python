Maths = int(input("Enter the marks of Maths => "))
Science = int(input("Enter the marks of Science => "))
English = int(input("Enter the marks of English => "))

Total = Maths + Science + English

if Total>=100:
    print("A Grade")

else:
    if Total>=50:
        print("B Grade")
    
    else:
        print("C Grade")
