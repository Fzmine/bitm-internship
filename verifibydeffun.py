def verify_person(name="Unknown", age=None):
    if age is not None:
        print("Verifying".format(name))
        if age >= 18:
            print("Verification successful eligible.".format(name))
        else:
            print("not eligible due to age.".format(name))
    else:
        print("Age is required for verification.")
        


name = input("Enter your name: ")
age = int(input("Enter your age: "))


verify_person(name, age)