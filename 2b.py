import math

[a1, a2]=map(float, input().split())
[b1, b2]=map(float, input().split())
c=math.sqrt((( a1- b1 )**2) + (( a2-b2 ))**2)
c=float('{:.3f}'.format(c))
print(c)


