list_1=[5,4,67,7,68,300,98,99]
max_num=list_1[0]
for i in range(1,len(list_1)):
    if(list_1[i]>max_num):
        max_num=list_1[i]
print(max_num)