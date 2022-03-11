t = int(input())

for _ in range(t):
    r, d, y, g = map(lambda n: int(n), input().strip().split(' '))
    if g < 3:
        print(-1)
        continue

    arr = sorted([r,d,y])
    ans = arr[0]
    for i in range(1, g):
        if i % 2 == 1:
            ans += arr[-1]
        else:
            ans += arr[1]
    print(ans)