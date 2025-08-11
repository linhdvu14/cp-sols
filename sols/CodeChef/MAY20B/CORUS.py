''' Isolation Centers

https://www.codechef.com/MAY20B/problems/CORUS

''' 

from sys import stdin, stdout

def solve(N,Q,S):
	counts = [0]*26
	for c in S:
		counts[ord(c)-ord('a')] += 1

	for _ in range(Q):
		C = int(stdin.readline().strip())
		res = sum(max(c-C,0) for c in counts)
		print(res)
		stdout.flush()



def main():	
	T = int(stdin.readline().strip())

	for _ in range(T):
		N, Q = list(map(int,stdin.readline().strip().split()))
		S = stdin.readline().strip()
		solve(N,Q,S)


if __name__ == '__main__':
	main()