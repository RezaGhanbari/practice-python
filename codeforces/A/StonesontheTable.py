i = input()
raw = raw_input()
print(sum(p == n for p, n in zip(raw[1:], raw)))
