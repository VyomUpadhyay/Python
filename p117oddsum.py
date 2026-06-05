Number = int(input("Enter the limit to check the odd and even number till it => "))
s=0
for i in range(1, Number):
    if i%2==1:
        print(i)
        s=s+i

print("Sum = ",s)