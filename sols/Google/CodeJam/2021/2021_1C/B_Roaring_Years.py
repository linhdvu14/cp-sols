''' Roaring Years 
https://codingcompetitions.withgoogle.com/codejam/round/00000000004362d7/00000000007c0f01
'''

def solve(Y):  # 68000
	strY = str(Y)
	N = len(strY)
	res = 1234567891011121314
	
	for d in range(1,10):
		if d>len(strY): break

		# 100,101,102...
		cur = int('1'+'0'*(d-1))
		cand = str(cur)
		cur += 1
		cand += str(cur)
		while int(cand) <= Y:
			cur += 1
			cand += str(cur)
		res = min(res, int(cand))
		# print(d, int(cand))

		# 97,98,99...
		for i in range(1000):
			cur = int(strY[:d])+i
			cand = str(cur)
			cur += 1
			cand += str(cur)
			while int(cand) <= Y:
				cur += 1
				cand += str(cur)
			res = min(res, int(cand))
			# print(d, i, int(cand))

	return res



def main():
	from sys import stdin
	
	T = int(stdin.readline().strip())

	for t in range(T):
		Y = int(stdin.readline().strip())
		out = solve(Y)
		print('Case #{}: {}'.format(t+1, out))


if __name__ == '__main__':
	main()