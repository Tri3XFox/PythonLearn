import math

n1, n2 = map(int, input().split())
lst=[]
for i in range(n1, n2+1):
    if (i > 10):
        if (i%2==0) or (i%10==5):
            continue
    for j in lst:
        if j > int((math.sqrt(i)) + 1):
            lst.append(i)
            break
        if (i % j == 0):
            break
    else:
        lst.append(i)
print (*lst, sep=(' '))