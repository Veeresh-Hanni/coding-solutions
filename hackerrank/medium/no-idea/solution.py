# Enter your code here. Read input from STDIN. Print output to STDOUT


n, m = map(int, input().split())

arr = list(map(int, input().split()))

a = set(map(int, input().split()))

b = set(map(int, input().split()))

a_happines = 0
b_happiness = 0

for n in arr:
    if n in a:
        a_happines += 1
    elif n in b:
        b_happiness += 1

print(a_happines - b_happiness)
# print(n)
# print(m)
# print(arr)
# print(a)
# print(b)
