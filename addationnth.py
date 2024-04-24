condition=True
sum=0
while (condition):
  num=int(input("Enter the number:"))
  if(num==0):
    condition=False
    print("the sum of number is :",sum)
  else:
    sum=sum+num