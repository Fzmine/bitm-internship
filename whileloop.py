n = 5  
i = 1  

while i <= n:
    print(" " * (n - i) + " ".join(str(j) for j in range(1, i+1)))
    i+=1