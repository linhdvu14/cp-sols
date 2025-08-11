''' F. Strange LCS
https://codeforces.com/contest/1589/problem/F
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

def atoi(c):
	if 'a' <= c <= 'z': return ord(c) - ord('a')
	return ord(c) - ord('A') + 26

def itoa(i):
	if i >= 26: return chr(i + ord('A') - 26)
	return chr(i + ord('a'))


# see also CF 463_D
# https://codeforces.com/contest/1588/submission/135825460

# find longest path in DAG where
# * node (c, mask) = V
#   * char c appears in all strs
#   * mask[i] = c appears in strs[i] as 1st/2nd occurrence
#   * V = Nd vector, V[i] = index (c, mask) in strs[i]
# * edge (c1, mask1)=V1 -> (c2, mask2)=V2
#   * if V[i] < V2[i], i.e. (c1, mask) appears before (c2, mask) in all strs

def solve(N, strs):
	# cnt[c] = num strs containing char c
	cnt = [0]*52

	# pos[c][i][b] = idx of b-th occurrence of char c in strs[i]
	pos = [[[-1]*2 for _ in range(N)] for _ in range(52)]

	for i, s in enumerate(strs):
		for j, c in enumerate(s):
			c = atoi(c)
			if pos[c][i][0] == -1:
				pos[c][i][0] = j
				cnt[c] += 1
			else:
				pos[c][i][1] = j

	# longest path from node (c, mask)
	def dfs(c, mask, memo):
		if (c, mask) in memo: return memo[c, mask]
		res = ''
		for nc in range(52):
			if cnt[nc] < N: continue
			nmask = 0     # min valid pos of nc
			valid = True  # whether can move to (nc, nmask)
			for i in range(N):
				# cur pos of c < 1st pos of nc -> use 1st pos
				if pos[c][i][(mask>>i) & 1] < pos[nc][i][0]: continue

				# cur pos of c < 2nd pos of nc -> use 2nd pos
				if pos[c][i][(mask>>i) & 1] < pos[nc][i][1]:
					nmask |= 1 << i
					continue

				# cur pos of c > 2nd pos of nc -> invalid
				valid = False
				break

			if valid: 
				cand = dfs(nc, nmask, memo)
				if len(res) < len(cand): res = cand
		
		memo[c, mask] = itoa(c) + res
		return memo[c, mask]

	# try starting path from each char, 1st occurrence (mask=0)
	res = ''
	memo = {}
	for c in range(52):
		if cnt[c] < N: continue
		cand = dfs(c, 0, memo)
		if len(res) < len(cand): res = cand

	return res


def main():
	T = int(input())
	for _ in range(T):
		N = int(input())
		strs = [input().decode().strip() for _ in range(N)]
		out = solve(N, strs)
		print(len(out))
		print(out)


if __name__ == '__main__':
	main()

