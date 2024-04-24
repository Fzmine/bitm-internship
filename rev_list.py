n=10
list_1=list(range(1,n+1)) #[1,2,3,4,5,6]
print(list_1)
rev_list=[]
for i in range(n):
    rev_list=rev_list+[list_1[n-1-i]]
print(rev_list)
list_1.reverse
rev_list[::-1]