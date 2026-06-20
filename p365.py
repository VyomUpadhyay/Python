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

i = 0
while i < (n*2)-1:
    j = 0
    while j < (n*2)-1:
        j = j + 1
        print('*', end = ' ')
    i = i + 1
    print('')