''' Chef and String
https://www.codechef.com/JUNE20B/problems/XYSTR
'''

def solve(S):
	res = 0
	used = False
	for i in range(1,len(S)):
		if i > 0 and S[i] != S[i-1] and not used:
			res += 1
			used = True
		else:
			used = False
	return res



def main():
	from sys import stdin
	
	T = int(stdin.readline().strip())
	for _ in range(T):
		S = stdin.readline().strip()
		out = solve(S)
		print(out)


if __name__ == '__main__':
	main()

