m = list(raw_input().split(' '))
s = 0
for i in range(eval(m[2])):
    s += eval(m[0])*(i+1)
if eval(m[1])<s:
    print abs(eval(m[1])-s)
else:
    print "0"