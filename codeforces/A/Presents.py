import operator
q = input()
n = map(int, raw_input().split(' '))
v = {}
for i, j in enumerate(n):
    v[i] = j
s = sorted(v.items(), key=operator.itemgetter(1))
r = []
for i in s:
    r.append(i[0]+1)
res =''
for i in r:
    res += str(i) + ' '
print res