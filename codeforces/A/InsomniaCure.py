from __future__ import print_function
x=[]
for j in range(5):
    x.append(input())
count = 0
for i in range(1, x[4]+1):
    if i % x[0] == 0 or i % x[1] == 0 or i % x[2] == 0 or i % x[3] == 0:
        count += 1
print(count)
