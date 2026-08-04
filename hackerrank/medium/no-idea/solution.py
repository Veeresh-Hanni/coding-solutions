# Enter your code here. Read input from STDIN. Print output to STDOUT
n, m = map(int, input().split())

arr = list(map(int, input().split()))

a = set(map(int, input().split()))

b = set(map(int, input().split()))

# print(n)
# print(m)
# print(arr)
# print(a)
# print(b)

# happiness = 0

# for num in arr:
#     if num in a:
#         happiness += 1
#     elif num in b:
#         happiness -= 1

# print(happiness)

print(sum((i in a) - (i in b) for i in arr))
