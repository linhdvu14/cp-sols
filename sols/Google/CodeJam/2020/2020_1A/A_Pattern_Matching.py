''' Pattern Matching
https://codingcompetitions.withgoogle.com/codejam/round/000000000019fd74/00000000002b3034
'''

def select(prefices):
	if not prefices: return ''
	prefices.sort(key=lambda x: len(x))
	cand = prefices[-1]
	for p in prefices:
		if not cand.startswith(p): return '*'
	return cand



def solve(pats):
	prefices, suffices = set(), set()
	mid = ''
	for pat in pats:
		toks = pat.split('*')
		if toks[0]: prefices.add(toks[0])
		if toks[-1]: suffices.add(toks[-1][::-1])
		mid += ''.join(toks[1:-1])

	p = select(list(prefices))
	s = select(list(suffices))[::-1]
	return '*' if p == '*' or s == '*' else p + mid + s




def main():
	from sys import stdin
	
	T = int(stdin.readline().strip())

	for t in range(T):
		N = int(stdin.readline().strip())
		pats = [stdin.readline().strip() for _ in range(N)]
		out = solve(pats)
		print('Case #{}: {}'.format(t+1, out))


if __name__ == '__main__':
	main()