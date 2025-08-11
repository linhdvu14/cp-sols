''' The Tom and Jerry Game!
https://www.codechef.com/JUNE20B/problems/EOEO
'''

def solve(TS):
	mult, ts = 2, TS
	while ts&1==0:
		mult <<= 1
		ts >>= 1
	return TS//mult


def main():
	from sys import stdin
	
	T = int(stdin.readline().strip())
	for _ in range(T):
		TS = int(stdin.readline().strip())
		out = solve(TS)
		print(out)


if __name__ == '__main__':
	main()

