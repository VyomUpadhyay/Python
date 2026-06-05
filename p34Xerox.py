print("Press 1 to print")
print("Press 2 to give typing job")

option = int(input("Enter the option: "))

if option==1:
    Pages = int(input("Enter the pages to be printed: "))
    if Pages > 50:
        print("The price of printing will be 5 rs per page. The total rs will be = ", Pages*5)
    else: 
        print("The price of printing will be 7 rs per page. The total rs will be = ", Pages*7)


elif option==2:
    Pages = int(input("Enter the pages to be Typed: "))
    if Pages > 50:
        print("The price of typing per page will be 15 rs. The total rs will be = ", Pages*15)
    else:
        print("The price of typing per page will be 20 rs. The total rs will be = ", Pages*20)
else:
    print("Eneter the valid option")