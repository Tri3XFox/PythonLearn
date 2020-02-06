[a, b, c]=map(int, input().split())
if 0!=a<=b+c and 0!=b<=a+c and 0!=c<=b+a :
    print('YES')
else: print('NO')