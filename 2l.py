[n, x1, d]=map(int, input().split())
if 1<=n<=10**9 and -1000<=x1<=1000 and -1000<=d<=1000 :
    avg= ((2 * x1 + d * (n-1))/2)
    avg=int(avg)
    print(avg)