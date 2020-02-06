[a1, a2, a3]=map(int, input().split())
a= [a1, a2, a3]
d=int(1)
for i in range(2):
     if a[i+1] == a[i]:
         d+=1
print(d)

