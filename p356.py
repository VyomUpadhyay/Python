n = int(input("Enter number -> "))
k=10
for i in range(1, n):
    for j in range(n, 0, -1):
        if j > i:
            print(" ", end=' ')
        else:
            k-=1
            print(k, end=' ')

    print("")