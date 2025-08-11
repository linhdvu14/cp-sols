''' Problem A1: Weak Typing - Chapter 1
https://www.facebook.com/codingcompetitions/hacker-cup/2021/round-1/problems/A1
'''

def solve(s):
	res = 0
	key = ''
	for c in s:
		if c == 'F': continue
		if c != key and key != '':
			res += 1
		key = c
	return res


def main():
	from sys import stdin
	
	T = int(stdin.readline().strip())
	for t in range(T):
		_ = int(stdin.readline().strip())
		s = stdin.readline().strip()
		out = solve(s)
		print('Case #{}: {}'.format(t+1, out))


def gen():
	import random
	random.seed(12)

	chars = 'FXO'

	T = 1000
	print(T)
	for _ in range(T):
		N = random.randint(1,800000)
		s = [random.randint(0,len(chars)-1) for _ in range(N)]
		s = ''.join(chars[i] for i in s)
		print(s)


if __name__ == '__main__':
	# gen()
	main()
