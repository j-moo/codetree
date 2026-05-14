a = input()
b = input()

while True:
    if b not in a:
        break
    
    index = a.find(b)
    
    a = a[:index] + a[index+len(b):]

print(a)