n=int(input())
if n<0:
    print('ERROR')
k=int(n)
i=2	#индекс элемента
fib=[1,1]+[0]*k #ряд начинается с 1
while fib[i]<n:
    i += 1
    fib[i]=fib[i-1]+fib[i-2]

print(fib[i])
