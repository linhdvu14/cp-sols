''' Moons and Umbrellas 
https://codingcompetitions.withgoogle.com/codejam/round/000000000043580a/00000000006d1145
'''

def solve1(cj,jc,S):
	def count(s,e):
		left = S[s-1] if s>0 else ''
		right = S[e+1] if e<len(S)-1 else ''
		if not left or not right or left==right: return 0
		return cj if left=='C' else jc

	s = e = -1
	res = 0
	for i,c in enumerate(S):
		if i<len(S)-1 and S[i:i+2]=='CJ': res += cj
		if i<len(S)-1 and S[i:i+2]=='JC': res += jc
		if c=='?':
			if s < 0: s = i
			e = i
		elif s >= 0:
			res += count(s,e)
			s = e = -1
	if s >= 0: res += count(s, e)
	return res


def solve(cj,jc,S):
	N = len(S)

	dp_j = [float('inf')]*N
	dp_c = [float('inf')]*N
	if S[0]=='C': dp_c[0] = 0
	if S[0]=='J': dp_j[0] = 0
	if S[0]=='?': dp_c[0] = dp_j[0] = 0

	for i in range(1,N):
		if S[i]=='C' or S[i]=='?':
			dp_c[i] = min(dp_c[i-1], dp_j[i-1]+jc)
		if S[i]=='J' or S[i]=='?':
			dp_j[i] = min(dp_j[i-1], dp_c[i-1]+cj)

	return min(dp_j[-1], dp_c[-1])


def main():
	from sys import stdin
	
	T = int(stdin.readline().strip())

	for t in range(T):
		cj,jc,S = stdin.readline().strip().split()
		out = solve(int(cj),int(jc),S)
		print('Case #{}: {}'.format(t+1, out))


if __name__ == '__main__':
	main()

