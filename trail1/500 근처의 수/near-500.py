import sys

arr = list(map(int, input().split()))

max_val = -sys.maxsize
min_val = sys.maxsize

for elem in arr:
    if elem < 500 and max_val < elem:
        max_val = elem
    
    if elem > 500 and min_val > elem:
        min_val = elem

print(max_val, min_val)