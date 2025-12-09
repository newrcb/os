requests = list(map(int, input("Enter disk requests: ").split()))
head = int(input("Enter initial head position: "))
direction = input("Enter direction (left/right): ")

requests.sort()
movement = 0
pos = head

print("\nOrder of servicing:")

if direction == "right":
    # Serve right side first
    for r in requests:
        if r >= head:
            print(r, end=" ")
            movement += abs(r - pos)
            pos = r

    # then reverse and serve left side
    for r in reversed(requests):
        if r < head:
            print(r, end=" ")
            movement += abs(pos - r)
            pos = r

else:
    # Serve left first
    for r in reversed(requests):
        if r <= head:
            print(r, end=" ")
            movement += abs(pos - r)
            pos = r

    # then serve right
    for r in requests:
        if r > head:
            print(r, end=" ")
            movement += abs(r - pos)
            pos = r

print("\nTotal Head Movement:", movement)