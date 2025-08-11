''' Allocation 
https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ffc7/00000000001d3f56
'''


def solve(B, costs):
	counts = [0 for _ in range(1001)]
	for c in costs:
		counts[c] += 1

	out = 0
	for cost,count in enumerate(counts):
		if B <= 0: break
		if count == 0: continue
		v = min(B // cost, count)
		out += v
		B -= cost*v

	return out


def main():
	from sys import stdin
	
	T = int(stdin.readline().strip())

	for t in range(T):
		N, B = list(map(int,stdin.readline().strip().split()))
		costs = list(map(int,stdin.readline().strip().split()))
		out = solve(B, costs)
		print('Case #{}: {}'.format(t+1, out))


if __name__ == '__main__':
	main()