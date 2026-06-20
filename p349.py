n = int(input("Enter the number -> "))
k=9
for i in range (1,n+1):
    for j in range(1, i+1):
        print(" ", end="")
    for j in range(n, i-1 , -1 ):
        print(i, end="")
    print("")
