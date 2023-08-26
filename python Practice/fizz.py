def fizbuzz(n):
    for i in n:
        if i % 3 == 0:
            print(i, "fizz")
        elif i % 5== 0:
            print(i, "buzz")
        if i%3==0 and i%5==0:
            print(i, "fizzbuzz")

n=range(1,100)
fizbuzz(n)