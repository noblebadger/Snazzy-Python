

def findall(s, sub):
    if s.find(sub) == -1:
        return 0
    else:
        start = s.find(sub) + 1
        return 1 + findall(s[start:], sub)

s = raw_input()
sub = raw_input()

print(findall(s, sub))