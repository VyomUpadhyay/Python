Character = str(input("Enter a letter to check wheateher the letter uppercase or not => "))

if Character.isupper():
    print(Character.lower())
elif Character.islower():
    print(Character.upper())
else:
    print(Character)
    
