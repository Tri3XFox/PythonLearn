N=int(input(''))
a=0
i=1
while a>=N:
    a=i**2
    i+=1
    if a % 10== i:
        print(i)