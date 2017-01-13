from __future__ import print_function

m = []
for i in range(5):
    m.append(raw_input().split(' '))
index = " "
for x in range(5):
    for y in range(5):
        if eval(m[x][y]) == 1:
            index = "{} {}".format(x, y)
index1 = eval(index.split(' ')[0])
index2 = eval(index.split(' ')[1])
print(abs(index1 - 2) + abs(index2 - 2))
