a = list(map(int, input().split()))
b=abs(a[0])
c=abs(a[1])
d=0
if -10000<a[0]<10000 or -10000<a[1]<10000:

    for i in range(c):
        d+=b
    if a[0]<0 and a[1]<0:
            print('(-', b,')', '*', '(-', c, ')', '=', d, sep=(''))
    elif a[0]<0 and a[1]==0:
        print('(-', b, ')', '*', c,  '=', d, sep=(''))
    elif a[0]<0:
        print('(-', b, ')', '*', c,  '=-', d, sep=(''))
    elif a[1] < 0 and a[0]==0:
        print(b, '*', '(-', c, ')', '=', d, sep=(''))
    elif a[1]<0:
        print(b, '*', '(-', c, ')', '=-', d, sep=(''))
    else:
        print(b, '*', c, '=', d, sep=(''))

