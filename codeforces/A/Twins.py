from __future__ import print_function

n = input()
# noinspection PyCompatibility
a = sorted(map(int, raw_input().split(" ")))
c, s = 0, 0
while sum(a) >= s:
    s += a.pop()
    c += 1
print(c)
