R = lambda: map(int, raw_input().split())
n, m = R()
a = sorted(R())
ans = (a[i+n-1]-a[i] for i in range(m-n+1))
print min(ans)