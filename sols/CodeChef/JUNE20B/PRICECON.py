''' Chef and Price Control
https://www.codechef.com/JUNE20B/problems/PRICECON
'''

def solve(N,K,prices):
	return sum(max(p-K,0) for p in prices)



def main():
	from sys import stdin
	
	T = int(stdin.readline().strip())
	for _ in range(T):
		N,K = list(map(int,stdin.readline().strip().split()))
		prices = list(map(int,stdin.readline().strip().split()))
		out = solve(N,K,prices)
		print(out)


if __name__ == '__main__':
	main()

