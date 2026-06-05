Number = int(input("Enter limit =>"))
s=0
for i in range(1, Number+1):
    if i==Number:
        print(i,end=" " )
    else:
        print(i,end=" + " )
    s=s+i
print("\nSum = ",s)