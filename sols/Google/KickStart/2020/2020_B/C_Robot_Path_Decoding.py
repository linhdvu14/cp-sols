''' Robot Path Decoding
https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ffc8/00000000002d83dc
'''

LIM = 10**9

def solve(moves):
	dx = dy = 0
	stack = [1]
	for m in moves:
		if m == '(': continue
		if '2' <= m <= '9':
			stack.append(stack[-1]*int(m))
		elif m == ')':
			stack.pop()
		else:
			if m == 'W': dx -= stack[-1]
			if m == 'E': dx += stack[-1]
			if m == 'N': dy -= stack[-1]
			if m == 'S': dy += stack[-1]

		dx %= LIM
		dy %= LIM

	return dx+1,dy+1



def main():
	from sys import stdin
	
	T = int(stdin.readline().strip())

	for t in range(T):
		moves = stdin.readline().strip()
		x,y = solve(moves)
		print('Case #{}: {} {}'.format(t+1,x,y))


if __name__ == '__main__':
	main()