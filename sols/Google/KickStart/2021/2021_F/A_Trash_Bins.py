''' Trash Bins
https://codingcompetitions.withgoogle.com/kickstart/round/0000000000435bae/0000000000887c32
'''

def solve(N,S):
	res = 0
	first = last = -1
	for i, c in enumerate(S):
		if c == '0': continue
		if last >= 0:
			d = i - last - 1
			res += d//2 * (d//2 + 1) + (d+1)//2 * (d%2)
		last = i
		if first < 0: first = i
	res += first * (first+1) // 2
	res += (N-last-1) * (N-last) // 2
	return res


def main():
	from sys import stdin
	
	T = int(stdin.readline().strip())

	for t in range(T):
		N = int(stdin.readline().strip())
		S = stdin.readline().strip()
		out = solve(N,S)
		print('Case #{}: {}'.format(t+1, out))


if __name__ == '__main__':
	main()
