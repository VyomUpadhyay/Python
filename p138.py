#printdata(name,age,gender)
def information(name,age,gender):
    print("Name -> ",name)
    print("Age -> ",age)
    print("Gender-> ",gender)
    
    
information("Vyom",16,"male")
information(age=22,gender="male",name="Rahil")


def square(a):
    return a*a
    
    
c=square(5)
square(c)