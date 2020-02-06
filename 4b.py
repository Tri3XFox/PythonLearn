a = list(map(int, input().split()))
i=a[0]
while i<=a[1]:
    print(i, '*', i, '=', i*i, sep=('') )
    i+=1