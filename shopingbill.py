bill_amount=int(input())

if(bill_amount<10000):
    print("no discount")
elif(bill_amount>=10000 and bill_amount < 20000):
   print ("10% discount")
   discount_price = 0.1*bill_amount
   final_bill_amt = bill_amount - discount_price
   print(final_bill_amt)
elif(bill_amount>=20000 and bill_amount < 50000):
    print("30% discount")
    discount_price = 0.3*bill_amount
    final_bill_amt = bill_amount - discount_price
    print(final_bill_amt)
else:
    print("50% discount")
    discount_price = 0.5*bill_amount
    final_bill_amt = bill_amount - discount_price
    print(final_bill_amt)
    