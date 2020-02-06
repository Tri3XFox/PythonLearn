import math
[x1, y1, x2, y2, x3, y3]=map(float, input().split())
S=0.5 * abs(( x2 - x1 ) * ( y3 - y1  ) - ( x3 - x1 ) * ( y2 - y1 ))
S=float('{:.5f}'.format(S))
A=math.sqrt((( x2 - x1 )**2) + (( y2 - y1 ))**2)
B=math.sqrt((( x3 - x2 )**2) + (( y3 - y2 ))**2)
C=math.sqrt((( x3 - x1 )**2) + (( y3 - y1 ))**2)
P=A+B+C
P=float('{:.5f}'.format(P))
print(P, S)