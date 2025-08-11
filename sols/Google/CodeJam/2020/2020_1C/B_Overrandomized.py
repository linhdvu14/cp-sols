''' Overrandomized
https://codingcompetitions.withgoogle.com/codejam/round/000000000019fef4/00000000003179a1
'''


def solve(counts,letters):
	zero = [c for c in letters if c not in counts]
	return zero[0] + ''.join(sorted(counts, key=counts.get, reverse=True))


def main():
	from sys import stdin
	
	T = int(stdin.readline().strip())

	for t in range(T):
		U = int(stdin.readline().strip())
		counts = {}
		letters = set()
		for _ in range(10**4):
			_, r = stdin.readline().strip().split()
			if r[0] not in counts: counts[r[0]] = 0
			counts[r[0]] += 1
			for c in r: letters.add(c)

		out = solve(counts,letters)
		print('Case #{}: {}'.format(t+1, out))


if __name__ == '__main__':
	main()