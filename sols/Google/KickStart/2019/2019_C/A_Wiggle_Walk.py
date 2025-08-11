''' Wiggle Walk 
https://codingcompetitions.withgoogle.com/kickstart/round/0000000000050ff2/0000000000150aac
'''
def merge(e2s, s2e, x):
	if x-1 in e2s and x+1 in s2e:
		s = e2s[x-1]
		e = s2e[x+1]
		s2e[s] = e
		e2s[e] = s
		s2e.pop(x+1, None)
		e2s.pop(x-1, None)
	elif x-1 in e2s:
		s = e2s[x-1]
		e2s.pop(x-1, None)
		e2s[x] = s
		s2e[s] = x
	elif x+1 in s2e:
		e = s2e[x+1]
		s2e.pop(x+1, None)
		s2e[x] = e
		e2s[e] = x
	else:
		s2e[x] = x
		e2s[x] = x


def solve(nr, nc, sr, sc, cmds):
	row_e2s = [{} for _ in range(nr)]
	row_s2e = [{} for _ in range(nr)]
	col_e2s = [{} for _ in range(nc)]
	col_s2e = [{} for _ in range(nc)]

	r, c = sr, sc
	rr, cc = r, c

	for cmd in cmds:
		if cmd == 'N':
			rr, cc = r-1, c
			if rr in col_e2s[c]:
				rr = col_e2s[c][rr]-1
		elif cmd == 'S':
			rr, cc = r+1, c
			if rr in col_s2e[c]:
				rr = col_s2e[c][rr]+1
		elif cmd == 'W':
			rr, cc = r, c-1
			if cc in row_e2s[r]:
				cc = row_e2s[r][cc]-1
		elif cmd == 'E':
			rr, cc = r, c+1
			if cc in row_s2e[r]:
				cc = row_s2e[r][cc]+1			
		merge(col_e2s[c], col_s2e[c], r)
		merge(row_e2s[r], row_s2e[r], c)
		r, c = rr, cc

	return rr, cc


def main():
	from sys import stdin
	
	T = int(stdin.readline().strip())

	for t in range(T):
		n, nr, nc, sr, sc = list(map(int,stdin.readline().strip().split()))
		cmds = stdin.readline().strip()
		r, c = solve(nr, nc, sr-1, sc-1, cmds)
		print('Case #{}: {} {}'.format(t+1, r+1, c+1))


if __name__ == '__main__':
	main()