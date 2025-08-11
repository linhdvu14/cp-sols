''' Wandering Robot 
https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ffc8/00000000002d8565
'''

from math import log2

# shared global var between test cases
# prob going (1,1) -> (r,c): C(r+c-2,r-1) / 2^(r+c-2) = (r+c-2)! / (r-1)! / (c-1)! / 2^(r+c-2)
# = 2 ^ [ log (r+c-2)! - log (r-1)! - log(c-1)! - (r+c-2) ]
logs = [0,0]  # log2(n!)
if len(logs) == 2:
	for i in range(2,2*(10**5)+1):
		logs.append(logs[-1] + log2(i))

def prob(r,c): return 2**(logs[r+c-2] - logs[r-1] - logs[c-1] - (r+c-2))


def solveSmall(nr,nc,r1,c1,r2,c2):
	def tour(r,c,memo):
		if r > nr or c > nc: return 0
		if (r,c) in memo: return memo[(r,c)]  # prob pass if start from this cell
		if r==nr and c==nc:  #  pass
			memo[(r,c)] = 1
		elif r1<=r<=r2 and c1<=c<=c2:  # fail
			memo[(r,c)] = 0
		else:
			right,down = tour(r+1,c,memo), tour(r,c+1,memo)
			if r+1 <= nr and c+1 <= nc:
				memo[(r,c)] = right/2 + down/2
			elif r+1 <= nr:
				memo[(r,c)] = right
			elif c+1 <= nc:
				memo[(r,c)] = down
		return memo[(r,c)]

	return tour(1,1,{})


def solveBig(nr,nc,r1,c1,r2,c2):
	res = 0.

	r,c = r2+1,c1-1
	while r < nr and c >= 1:
		res += prob(r,c)
		r += 1
		c -= 1
	while r == nr and c >= 1: 
		res += prob(r-1,c) / 2
		c -= 1

	r,c = r1-1,c2+1
	while r >= 1 and c < nc:
		res += prob(r,c)
		r -= 1
		c += 1
	while c == nc and r >= 1: 
		res += prob(c-1,r) / 2
		r -= 1

	return res

 

solve = solveBig


def main():
	from sys import stdin
	
	T = int(stdin.readline().strip())

	for t in range(T):
		W,H,L,U,R,D = list(map(int,stdin.readline().strip().split()))
		out = solve(W,H,L,U,R,D)
		print('Case #{}: {}'.format(t+1, out))


if __name__ == '__main__':
	main()