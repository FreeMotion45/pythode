t = int(input())

for _ in range(t):
    _, roads, bridges = int(input()), 0, 0
    blocks = input()

    ans = 0
    if blocks[0] == '1':
        roads += 1
        ans += 1
    else:
        bridges += 1
    
    for i in range(1, len(blocks)):
        block = blocks[i]
        if block == '1':
            if roads < bridges:
                # We dont gain WIDEness score as long as we havent passed the same amount
                # of road blocks as the last bridge.
                roads += 1
            else:
                # We have already passed the same amount of road blocks as the last bridge,
                # so we can gain WIDEness score.
                ans += 1
        else:
            roads = 0
            if blocks[i-1] == '1':
                # If the previous block was a road, then we are starting to count bridge sequence
                bridges = 1
            else:
                # The previous is a bridge, we are continuing the sequence
                bridges += 1
    print(ans)
