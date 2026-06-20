n = int(input("Enter number of rows: "))

for i in range(1, n + 1):
    for space in range(1, (n - i) + 1):
        print("  ", end="")  # Space for the left side

    for j in range(1, (2 * i)):
        # Print "a" at the border positions
        if j == 1 or j == (2 * i - 1) or i == n:
            print("a", end=" ")
        else:
            print(" ", end=" ")  # Inside of the triangle is empty
    print()
