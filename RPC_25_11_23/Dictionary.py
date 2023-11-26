from bisect import bisect_left, bisect_right
ent = list(map(int,input().split()))
x = []
for i in range(ent[0]):
    x.append(input())
x.sort()
for i in range(ent[1]):
    rang = input().split()
    j = bisect_left(x, rang[0])
    y = bisect_right(x, rang[1])
    print(y-j)