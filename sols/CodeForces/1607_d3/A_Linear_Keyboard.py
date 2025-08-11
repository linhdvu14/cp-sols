''' A. Linear Keyboard
https://codeforces.com/contest/1607/problem/A
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

def solve(keys, text):
	key_pos = {c: i for i, c in enumerate(keys)}
	res = sum(abs(key_pos[a] - key_pos[b]) for a, b in zip(text, text[1:]))
	return res


def main():
	T = int(input())
	for _ in range(T):
		keys = input().decode().strip()
		text = input().decode().strip()
		out = solve(keys, text)
		output(str(out) + '\n')


if __name__ == '__main__':
	main()

