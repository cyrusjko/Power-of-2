def powerof2(n):
    if n == 0:
        return 0
    if n&~(n-1)==n:
        return 1
    return 0
n=int(input("Enter Number: "))
if(powerof2(n)):
    print("Number is power of 2")
else:
    print("Number isnt power of 2")