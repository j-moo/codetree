string = input()
length = len(string)

for _ in range(length+1):
    print(string)
    answer = string[-1] + string[0:length-1]
    string = answer