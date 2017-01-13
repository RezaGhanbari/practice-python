n = input()
m = []
c=0
for i in range(n):
    m.append(raw_input().split(' '))
for i in m:
    if abs(eval(i[1])-eval(i[0])) >= 2:
        c+=1
print c