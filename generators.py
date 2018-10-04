def count_func(n):
	x = 0

	while x < n:
		yield x 
		x += 1


x = count_func(10)

for i in range(10):
	x.next()	
	print("count_func yields:", x)
