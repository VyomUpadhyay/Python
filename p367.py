n = int(input("Enter number of n: "))
k = 0
for i in range(1, n + 1):
    for space in range(1, (n - i) + 1):
        print("",end="  ")

    while k != (2 * i - 1):
        print(k,"", end="")
        k += 1

    k = 0
    print()

for i in range(n):
        if i == 0 or i == n - 1:
            print('* ' * ((n*2)-1))
        else:
            print('* ' + '  ' * (((n - 2) *2)+1) + '*')
