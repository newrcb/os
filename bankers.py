p = int(input("Enter number of processes: "))
r = int(input("Enter number of resources: "))

alloc = []
print("Enter Allocation Matrix:")
for i in range(p):
    row = list(map(int, input().split()))
    alloc.append(row)

maxm = []
print("Enter Max Matrix:")
for i in range(p):
    row = list(map(int, input().split()))
    maxm.append(row)

avail = list(map(int, input("Enter Available Resources: ").split()))

need = [[maxm[i][j] - alloc[i][j] for j in range(r)] for i in range(p)]
finish = [False]*p
safe_seq = []

while len(safe_seq) < p:
    allocated = False
    for i in range(p):
        if not finish[i] and all(need[i][j] <= avail[j] for j in range(r)):
            safe_seq.append(i)
            finish[i] = True
            for j in range(r):
                avail[j] += alloc[i][j]
            allocated = True
    if not allocated:
        print("\nSystem is NOT in Safe State!")
        exit()

print("\nSystem is in Safe State.")
print("Safe Sequence:", " -> ".join("P"+str(i) for i in safe_seq))