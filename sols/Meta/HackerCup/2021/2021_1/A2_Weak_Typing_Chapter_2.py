''' Problem A2: Weak Typing - Chapter 2
https://www.facebook.com/codingcompetitions/hacker-cup/2021/round-1/problems/A2
'''

MOD = 10**9 + 7

def solve(s, n):
	res = 0
	key, i = '', -1
	for j, c in enumerate(s):
		if c == 'F': continue
		if c != key and key != '':
			res += (i+1)*(n-j)
			res = res % MOD
		key = c
		i = j
	return res


def main():
	from sys import stdin
	
	T = int(stdin.readline().strip())
	for t in range(T):
		n = int(stdin.readline().strip())
		s = stdin.readline().strip()
		out = solve(s, n)
		print('Case #{}: {}'.format(t+1, out))


if __name__ == '__main__':
	# gen()
	main()
