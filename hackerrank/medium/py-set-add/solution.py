# Enter your code here. Read input from STDIN. Print output to STDOUT

N = int(input())

stamps = set()

for _ in range(N):
    stamps.add(input())

print(len(stamps))
