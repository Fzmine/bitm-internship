num=int(input())
count = 0
for i in range(2,num,):
     if(num%i ==0):
        count = count +1
if(count == 0):
    print("it is a prime number")
else:
    print("it is not a prime number")