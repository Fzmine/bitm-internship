password='yeshwanth'
attempts=3
for i in range(attempts):
        attempt=int(i+1)
        passwords=input("enter password\n")
        if (passwords==password):
            print("excatly right password")
            break

        else:
            if attempt<attempts:
                print("youve entered incorrect password")
            else:
                print("incorrect password,youve overcame 3 attempts")