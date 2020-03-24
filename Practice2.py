#nested if
n=int(input("Enter number of your choice:",))
print(n)
if(n%2==0)in range(2,6)or n>20:
    print("not weird")
    if(n%2==0) in range(6,20):
        print("weird")
else:
    print("weird")
