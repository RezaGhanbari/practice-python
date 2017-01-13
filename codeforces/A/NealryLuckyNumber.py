from __future__ import print_function


def lucky(n):
    return True if any(set("47") >= set(str(i)) and n % i == 0 for i in range(1, n + 1))else False


def get_number(n):
    c = []
    for i in n:
        if eval(i)==7 or eval(i)==4:
            c.append(1)
    return sum(c)

n = raw_input()
print("YES" if lucky(get_number(n)) else "NO")
