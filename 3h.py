import datetime
import time
[d, m]=map(str, input().split())
w=datetime.datetime.strptime(d + m + '2016', '%d%m%Y')
a=int(w.isoweekday())
if a==1:
   print('Monday')
if a==2:
   print('Tuesday')
if a==3:
   print('Wednesday')
if a==4:
   print('Thursday')
if a==5:
   print('Friday')
if a == 6:
    print('Saturday')
if a==7:
   print('Sunday')