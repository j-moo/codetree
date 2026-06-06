text = input()
pattern = input()

def solve():
    idx = -1
    for i in range(len(text) - len(pattern) + 1):
        if text[i] == pattern[0]:
            idx = i
            for j in range(len(pattern)):
                if text[i + j] != pattern[j]:
                    idx = -1
                    break
            else:
                return i
    return idx

print(solve())