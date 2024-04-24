n=int(input())
i=1
def table(n ,i):
    if(i<=10):
       print(n,' x  ',i,' = ',n*i)
    else:
        return
    table(n,i+1)
table(n,i)