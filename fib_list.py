
def fib(n):
    f, f1 = 0, 1
    for i in range(n):
          if i <= 1:
            yield i
          else:  
            yield f + f1
            f, f1 = f1, f + f1

num = int(input())
for n in fib(num):
	print(n)

#map(lambda a : a * a * a, f)





