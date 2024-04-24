condition=True
#'Shashidhar Reddy H'
while condition:
  full_name=input("Enter your full name:")
  if full_name.isalpha():
    condition=False
last_name=full_name.split()[-1]
first_name=full_name.split()[0]
#Bitma123
condition=True
password="bitm@123"
special_count=0
digit_count=0
upper_count=0
lower_count=0
while condition:
  password=input("Enter your password:")
  if len(password)>=8 and password.isalnum():
    condition=False
  for i in password:
    if len(password)>=8 and password.isdigit():
      condition=False
    if len(password)>=8 and password.isupper():
        condition=False
    if len(password)>=8 and password.isspecial(): 
        condition=False 
if(len(password)>=8 and password==len(password)):
   print("You have succesfully got an access")
else:
    print("Re-Enter Password")
     