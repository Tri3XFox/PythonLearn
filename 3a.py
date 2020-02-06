[a1, a2, a3]=map(int, input().split())
a=[a1, a2, a3]
max=int(0)
for i in range(3):
    if a[i] > max:
        max=a[i]
print(max)
