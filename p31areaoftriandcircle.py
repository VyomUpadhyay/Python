print("Press 1 to calculate the area of Triangle")
print("Press 2 to calculate the area of Circle")

option = int(input("Enter the option: "))

if option == 1:
    Base = int(input("Enter the Base of triangle: "))
    Height = int(input("Enter the height of the triangle: "))
    
    print("Area of Triangle = ", 0.5*Base*Height )
elif option == 2:
    Radius = int(input("Enter the Radius of Circle: "))
    print("Area of circle is: ", 3.1415*Radius*Radius)
else: 
    print("Enter the valid Option")