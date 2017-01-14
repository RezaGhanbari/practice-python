n=input()
res = []
for i in range(n):
    res.append(raw_input().split(' '))
f = []
s0,s1,s2 = 0, 0 , 0
for j in res:
    s0 += eval(j[0])
for j in res:
    s1 += eval(j[1])
for j in res:
    s2 += eval(j[2])

if s0==0 and s1==0 and s2==0:
    print "YES"
else:
    print "NO"