n, d = input().split()
print(n[:-1] + d if n[-1] < d else str(int(n) + 10)[:-1] + d )