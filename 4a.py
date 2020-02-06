n = int(input())
if 3<=n<=360:
    a = list(map(int, input().split()))
    s=0
    b=0
    for i in range(n):
        if a[i] ==int(0):
            b=1
        s+=a[i]
    print(s)
    if b==1 or s>(180*(n-2)):
        print('NO')
    else: print('YES')

