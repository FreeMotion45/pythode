n, t = map(lambda n: int(n), input().strip().split(' '))

arr = []
for _ in range(n):
    a, c = map(lambda n: int(n), input().strip().split(' '))
    arr.append((a, c))

arr.sort(key=lambda p: p[1], reverse=True)
ans = 0
for a, c in arr:
    ans += min(a, t) * c
    t -= min(a, t)
print(ans)
