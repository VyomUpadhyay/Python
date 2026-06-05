speed = int(input("Enter the fuel speed in (km/h) -> "))
if speed<=5:
    print("LOW")
elif speed<=20:
    print("AVERAGE")
elif speed>50:
    print("HIGH")
