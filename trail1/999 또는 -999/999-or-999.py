import sys

LIMIT = 999

arr = list(map(int, input().split()))

max_val = -sys.maxsize
min_val = sys.maxsize

for elem in arr:
    if elem == LIMIT or elem == -LIMIT:
        break

    if max_val < elem:
        max_val = elem
    
    if min_val > elem:
        min_val = elem

print(max_val, min_val)