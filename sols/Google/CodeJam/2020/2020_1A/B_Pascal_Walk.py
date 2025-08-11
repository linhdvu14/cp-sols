''' Pascal Walk
https://codingcompetitions.withgoogle.com/codejam/round/000000000019fd74/00000000002b1353
'''

def solve(n):
	if n <= 30: return [(i+1,1) for i in range(n)]

	target = n - 30 - (n%2)  # always odd
	rem = n - target 

	out = []
	lv = 1
	rev = False
	while target > 0:
		b = target & 1
		target >>= 1
		if b:
			row = [(lv,i+1) for i in range(lv)]
			if rev: row = row[::-1]
			rev = not rev
		else:
			row = [(lv,lv)] if rev else [(lv,1)] 
			rem -= 1
		out.extend(row)
		lv += 1

	for _ in range(rem):
		row = [(lv,lv)] if rev else [(lv,1)] 
		out.extend(row)
		lv += 1

	return out


def main():
	from sys import stdin
	
	T = int(stdin.readline().strip())

	for t in range(T):
		n = int(stdin.readline().strip())
		out = solve(n)
		print('Case #{}:'.format(t+1))
		for i,j in out:
			print('{} {}'.format(i,j))


if __name__ == '__main__':
	main()