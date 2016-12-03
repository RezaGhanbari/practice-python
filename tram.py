n=input()
a=[]
for i in range(n):
  a.append(raw_input().split(' '))
x,y=[],[]

for i in a:
  x.append(int(i[0]))
  y.append(int(i[1]))

s=[]

for i in range(len(y)):
  if i==(len(y)-1):
    break;
  s.append(y[i]+y[i+1])
t=[]
x.remove(x[0])
for j in range(len(s)):
  t.append(s[j]-x[j])
print t
print max(t)
