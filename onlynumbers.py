alpnum=input("enter an alphanumber: " )
numbers=[]
for char in alpnum:
    if char.isdigit():
        numbers.append(int(char))
number_sum=sum(numbers)
print("list of digits: ",numbers)
print("sum of digits: ",number_sum)