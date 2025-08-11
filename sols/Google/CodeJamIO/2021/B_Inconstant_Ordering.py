''' Inconstant Ordering 
https://codingcompetitions.withgoogle.com/codejamio/round/00000000004360f2/00000000007772ed
'''

def solve(N, slots):
	res = ['A']
	for i in range(0,N-1,2):
		n1, n2 = slots[i], slots[i+1]
		add2 = [chr(ord('A')+i) for i in range(n2)[::-1]]
		add1 = [chr(ord('B')+i) for i in range(n1)] if n1 >= n2 else [chr(ord('B')+i) for i in range(n1-1)] + [chr(ord(add2[0])+1)]
		res += add1 + add2
	
	if N%2 == 1:
		n1 = slots[-1]
		res += [chr(ord('B')+i) for i in range(n1)]

	return ''.join(res)


def main():
	from sys import stdin
	
	T = int(stdin.readline().strip())
	for t in range(T):
		N = int(stdin.readline().strip())
		slots = list(map(int,stdin.readline().strip().split()))
		out = solve(N, slots)
		print('Case #{}: {}'.format(t+1, out))


if __name__ == '__main__':
	main()