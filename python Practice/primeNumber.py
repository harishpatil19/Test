num=[3,5,2,8,6,5,9,7]
def prim(number):
    count=0
    mini =1
    while (number != mini):
        if number % 2 == 0:
            print("number", number, "is prime")
        else:
            print("number is not prime")
            count+=1
for i in num:
    prim(i)