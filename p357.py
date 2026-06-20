n = int(input("Enter number -> "))
k=10
for i in range(1, n):
    for j in range(n, 0, -1):
        if j > i:
            print(" ", end=' ')
        else:
            print(k, end=' ')

    print("")
    k-=1
