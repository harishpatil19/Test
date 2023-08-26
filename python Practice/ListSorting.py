n=[2,1,4,-1000000000, 0, -100, 3,9,-1]
temp=0
for i in range(0,len(n)):
    for j in range(i+1, len(n)):
        if (n[i] > n[j]):
            temp = n[i]
            n[i] = n[j]
            n[j] = temp
    print(n[i])