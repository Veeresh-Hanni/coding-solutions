n = int(input())
A = set(map(int, input().split()))

N = int(input())

for _ in range(N):
    cmd, _ = input().split()

    other = set(map(int, input().split()))

    if cmd == "intersection_update":
        A.intersection_update(other)

    elif cmd == "update":
        A.update(other)

    elif cmd == "symmetric_difference_update":
        A.symmetric_difference_update(other)

    elif cmd == "difference_update":
        A.difference_update(other)

print(sum(A))
