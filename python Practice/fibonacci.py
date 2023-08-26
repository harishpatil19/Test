
def fib(n):
    n1 = 0
    n2 = 1
    count = 0
    if num==0:
        print("number is 0")
    elif num==1:
        print("fib of 1 is", num)
    while count < num:
        sum = n1 +n2
        n1=n2
        n2= sum
        count+=1
        print(n2)

num=int(input("enter number"))
fib(num)



