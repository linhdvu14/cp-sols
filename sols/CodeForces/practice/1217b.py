from math import ceil

def solve(x, step, d):
	if x <= d: return 1
	if step <= 0: return -1
	t = int(ceil((x-d)/step))
	return t if x-step*t <= 0 else t+1


def main():
	from sys import stdin
	
	T = int(stdin.readline().strip())
	for _ in range(T):
		n, x = list(map(int,stdin.readline().strip().split()))
		step = mx_d = -10**9
		for _ in range(n):
			d, h= list(map(int,stdin.readline().strip().split()))
			if d-h > step: step = d-h
			if d > mx_d: mx_d = d
		print(solve(x, step, mx_d))
 
if __name__ == '__main__':
	main()