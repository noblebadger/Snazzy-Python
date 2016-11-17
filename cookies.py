
def more_cookies(m, n, base):
	if n > m:
		return n-m

	return more_cookies(m, n + base, base)

n,m = raw_input().split(' ')
n,m = int(n),int(m)

if n < 1 or n == m:
	print(0)
else:
	print(more_cookies(m, n, n))