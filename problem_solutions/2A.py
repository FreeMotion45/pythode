t = int(input())

for _ in range(t):
    r, d, y, g = map(lambda n: int(n), input().strip().split(' '))
    if g < 3:
        print(-1)
        continue

    arr = sorted([r,d,y])
    ans = arr[0]
    if (g - 1) % 2 == 0:
        ans += (arr[-1] + arr[1]) * (g - 1) // 2
    else:
        ans += arr[-1] + (arr[-1] + arr[1]) * (g - 2) // 2
    print(ans)