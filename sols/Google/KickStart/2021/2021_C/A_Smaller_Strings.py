''' Smaller Strings 
https://codingcompetitions.withgoogle.com/kickstart/round/0000000000435c44/00000000007ebe5e
'''
MOD = 10**9 + 7
MAX = 10**5
DEBUG = False

num_palin = [[1]*(MAX+1) for k in range(27)]
for k in range(1,27):
	num_palin[k][1] = k
	num_palin[k][2] = k
	for ln in range(3,MAX+1):
		num_palin[k][ln] = (k * num_palin[k][ln-2]) % MOD

def solve(N,K,S):
	res = 0
	mid = (N-1)//2

	# strictly smaller
	for i in range(mid+1):
		c = S[i]
		ln = max(N - 2*(i+1), 0)
		add = (ord(c)-ord('a'))*num_palin[K][ln]
		res = (res+add)%MOD
		if DEBUG: print(f'S={S} S[{i}]={S[i]}, ln={ln}, num_palin={num_palin[K][ln]}, add={add}')

	if N > 1:
		left, right = mid,mid+1
		if N%2 == 1: left, right = mid, mid
		while left >= 0 and right<N:
			if DEBUG: print(f'S[{left}]={S[left]}, S[{right}]={S[right]}')
			if S[left] < S[right]:
				if DEBUG: print(f'--> Add one')
				res += 1
				break
			if S[left] > S[right]:
				if DEBUG: print(f'--> Cannot add one')
				break
			left -= 1
			right += 1			

	return res % MOD


def main():
	from sys import stdin
	
	T = int(stdin.readline().strip())

	for t in range(T):
		N,K = list(map(int,stdin.readline().strip().split()))
		S = stdin.readline().strip()
		out = solve(N,K,S)
		print('Case #{}: {}'.format(t+1, out))


if __name__ == '__main__':
	main()
