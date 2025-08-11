''' Reversort Engineering 
https://codingcompetitions.withgoogle.com/codejam/round/000000000043580a/00000000006d12d7
'''

def solve(N,C):
	if not N-1<=C<=N*(N+1)//2-1: return 'IMPOSSIBLE'

	def build(i,C):
		if C > N-1-i: return list(reversed(build(i+1,C-(N-1-i)))) + [i+1]  # flip i..N-1
		return [i+1 for i in range(i+C,i-1,-1)] + [i+1 for i in range(i+C+1,N)]  # flip i,i+1,..,i+C

	nums = build(0,C-(N-1))
	return ' '.join(map(str,nums))


def main():
	from sys import stdin
	
	T = int(stdin.readline().strip())

	for t in range(T):
		N,C = list(map(int,stdin.readline().strip().split()))
		out = solve(N,C)
		print('Case #{}: {}'.format(t+1, out))


if __name__ == '__main__':
	main()

