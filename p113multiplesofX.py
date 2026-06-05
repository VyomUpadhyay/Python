number = int(input("Enter the limit = "))
multipleof = int(input("Enter the number you want to check the multiples = "))
count=0
sum=0
for i in range(1,number):
    if i%multipleof == 0:
        print(i)
    count += 1
    sum = sum + i
    
