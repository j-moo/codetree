while True:
    width, height, s = input().split()
    
    width = int(width)
    height = int(height)
    area = width * height
    print(area)

    if s == 'C':
        break