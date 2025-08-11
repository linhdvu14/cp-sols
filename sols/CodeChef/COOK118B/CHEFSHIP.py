''' Chef, Chefina and Their Friendship

https://www.codechef.com/COOK118B/problems/CHEFSHIP

'''

# Z[i] = max length d s.t. s[0..d] == s[i..i+d]
def z_func(s):  # O(n)
	z = [0]*len(s)
	l = r = 0
	for i in range(1,len(s)):
		if i <= r: z[i] = min(z[i-l], r-i+1)
		while i+z[i] < len(s) and s[z[i]] == s[i+z[i]]: z[i] += 1
		if i+z[i]-1 > r: l, r = i, i+z[i]-1
	return z


def solve(S):
	za = z_func(S)
	zb = z_func(S[::-1])  # backward idx
	res = 0
	for i in range(len(S)-2):  # cand split T1+T1|T2+T2
		if i % 2 == 0: continue
		ma = (i+1)//2
		mb = (len(S)-i-1)//2
		if za[ma] >= ma and zb[mb] >= mb: res += 1
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

