n = int(input("Enter number -> "))
for i in range(1, n):
    for j in range(n, 0, -1):
        if j > i:
            print(" ", end=' ')
        else:
            print(i%2, end=' ')

    print("")