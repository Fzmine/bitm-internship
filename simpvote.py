age =int(input())
gender =input()
if(age<18):
    print("ur not eligible")
elif(age>=18 and gender == "male"):
   print ("your eligible to vote")
   print("go to right side")
else:
    print("your eligible to vote")
    print("go to left side")