n = int(input("Enter number of n: "))
i=0
for i in range(1, n + 1):
    for space in range(1, (n - i) + 1):
        print("",end="  ")

    for k in range(0,2*i-1):
        if i==n:
            print("a ", end="")
            k += 1
        elif i<=n and k==0:
            print("a ", end="")
            k+=1
        elif k%2==0 and i<=3 :
            print("a ",end="")
        elif k==3 and k==5 and i==4 and i==3:
            print("a ", end="")
        elif i==4 and k==6:
            print("a ", end="  ")
        elif i==3 and k==3:
            print(end="  ")
        else:
            print(end="  ")
    print()



