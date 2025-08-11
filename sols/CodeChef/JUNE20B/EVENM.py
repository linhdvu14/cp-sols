''' Even Matrix
https://www.codechef.com/JUNE20B/problems/EVENM
'''

def solve(N):
	res = [[i+1 for i in range(N)]]
	for _ in range(N-1):
		res.append([n+N for n in res[-1]][::-1])
	return res


def main():
	from sys import stdin
	
	T = int(stdin.readline().strip())
	for _ in range(T):
		N = int(stdin.readline().strip())
		mat = solve(N)
		for row in mat: print(' '.join(map(str,row)))


if __name__ == '__main__':
	main()

