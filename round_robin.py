n = int(input("Enter number of processes: "))
burst = []
for i in range(n):
    bt = int(input(f"Enter Burst Time for P{i}: "))
    burst.append(bt)

quantum = int(input("Enter Time Quantum: "))

remaining = burst[:]      # copy burst times
time = 0
waiting = [0]*n
done = False

print("\nGantt Chart:")
while not done:
    done = True
    for i in range(n):
        if remaining[i] > 0:
            done = False
            if remaining[i] > quantum:
                print(f"| P{i} ", end="")
                time += quantum
                remaining[i] -= quantum
            else:
                print(f"| P{i} ", end="")
                time += remaining[i]
                waiting[i] = time - burst[i]
                remaining[i] = 0
print("|\n")

turnaround = [burst[i] + waiting[i] for i in range(n)]

print("Process  BT  WT  TAT")
for i in range(n):
    print(f"P{i}\t {burst[i]}\t {waiting[i]}\t {turnaround[i]}")