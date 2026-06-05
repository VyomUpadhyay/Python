Number = int(input("Enter the limit to check the odd and even number till it => "))

for i in range(1, Number):
    if i%2==0:
        print(i, "is even")
    else:
        print(i, "is odd")
