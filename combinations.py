from itertools import combinations

def get_comb(y, x):
    if x == 0:
        yield ()
    else:
        yield get_comb(x, y)
        x -= 1

x, y = raw_input().split(' ')
y = int(y)


z = combinations(x, y)

for i in z:
    print(str(i))