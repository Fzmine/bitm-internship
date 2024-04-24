condition=True
#'yeshwanth kumar'
while condition:
  full_name=input("Enter your full name:")
  if full_name.isalpha():
    condition=False
last_name=full_name.split()[-1]
first_name=full_name.split()[0]
#Bitma123
condition=True
digit_count=0
upper_count=0
lower_count=0
while condition:
  password=input("Enter your password:")
  if len(password)>=8 and password.isalnum():
    condition=False
  for i in password:
    if len(password)>=8 and password.indigit():
      condition=False
    if len(password)>=8 and password.isupper():
      condition=False