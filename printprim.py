start_num = int(input())
end_num = int(input())
for i in range(start_num, end_num+1 ):
    count = 0
for j in range(5,i):
     if(i%j ==0):
        count = count +1
if(count == 0):
    print(i)
