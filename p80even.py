Number = int(input("Enter the limit to check the odd and even number till it => "))
c=0
s=0
for i in range(1, Number):
    if i%2==0:
        print(i, "is even")
        c+=1
        s=s+i

print("Sum = ",s," Count = ",c)