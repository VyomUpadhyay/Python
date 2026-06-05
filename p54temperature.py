Temperature = int(input("Enter the temperature in celcius => "))

if Temperature>10:
    print("It is very cold Atmosphere")
elif Temperature>20:
    print("It is cold Atmosphere")
elif Temperature>30:
    print("It is normal Atmosphere")
elif Temperature>40:
    print("It is hot Atmosphere")
else:
    print("It is very hot Atmosphere")