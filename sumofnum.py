str_1=input()
sum=0
ans_list=[]
for each_char in str_1:
    if (each_char.isdigit()):
        ans_list.append(int(each_char))
        sum=sum+int(each_char)
print(ans_list)
print(sum)