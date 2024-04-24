n=10
list_1=list(range(1,n+1))
print(list_1)
rev_list=[]
for i in range(n):
    rev_list=rev_list+[list_1[n-1-i]]
    print(rev_list)
    print(list_1.reverse())
    print(list_1)
    print(list_1[::-1])