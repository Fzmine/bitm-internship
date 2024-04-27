n=input("enter the bracket: ")
stack=[]
for each_bracket in (n):
    if (each_bracket == "[" or "{" or "("):
        stack.append(each_bracket)
    else:
        top =stack[-1]
        if(top == "[" and each_bracket=="]"):
            stack.pop()
        elif(top == "(" and each_bracket==")"):
            stack.pop()
        elif(top == "{" and each_bracket=="}"):
            stack.pop()
        else:
            stack.append(each_bracket)

else:
    if not stack:
        print("Stack is balanced")
    else:
        print("Stack is unbalanced")
            


    