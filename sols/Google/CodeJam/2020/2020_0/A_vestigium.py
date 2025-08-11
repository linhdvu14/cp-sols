''' Vestigium 
https://codingcompetitions.withgoogle.com/codejam/round/000000000019fd27
'''

def solve(mat,N):
	def check(arr):
		seen = set()
		for a in arr:
			if a in seen: return True
			seen.add(a)
		return False

	k = sum(mat[i][i] for i in range(N))
	r = c = 0
	for i in range(N):
		if check(mat[i]):
			r += 1
		if check(mat[j][i] for j in range(N)):
			c += 1
	return k,r,c



def main():
	from sys import stdin
	
	T = int(stdin.readline().strip())

	for t in range(T):
		N = int(stdin.readline().strip())
		mat = []
		for _ in range(N):
			row = list(map(int,stdin.readline().strip().split()))
			mat.append(row)
		k,r,c = solve(mat,N)
		print('Case #{}: {} {} {}'.format(t+1, k,r,c))


if __name__ == '__main__':
	main()