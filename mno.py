num=int(input("Enter mobile number"))
li=[]
while int(num)>0:
    i=num%10
    li.append(int(i))
    num=num/10
digits=[7,8,9]
if len(li)==10:
    if  li[-1] in digits:
        print("valid")
else:
    print("invalid")