[a, b, v]=map(int, input().split())

if a > b and a > v :
    print('Anton')
if b > a and b > v:
    print('Boris')
if v > a and  v > b:
    print('Victor')
if a == b and a > v:
    print('Victor')
if a == v and a > b:
    print('Boris')
if b == v and b > a:
    print('Anton')
if a == b and a == v:
    print('Same age')

