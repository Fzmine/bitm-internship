list_1=[5,9,8,7,98,87,86,90]
max_num=list_1[0]
for i in range (1,len(list_1)):
    if (list_1[i]>max_num):
        max_num=list_1[i]
print(max_num)