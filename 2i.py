[a, b, n]=map(int, input().split())
if 1<=a<=1000 and a<=b<=1000:
    c=b-a
    an=a + (n - 1) * c
    print(an)