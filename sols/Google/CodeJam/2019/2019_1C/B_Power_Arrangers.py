''' Power Arrangers 
https://codingcompetitions.withgoogle.com/codejam/round/00000000000516b9/0000000000134e91
'''

from sys import stdin, stdout, stderr

def guess(indices, goal, sol, j, clues):
	count = [goal]*5
	for i in idx:
		print(5*i+j)
		stdout.flush()
		res = stdin.readline().strip()
		if res == 'N': exit(1)
		clues[i] += res
		count[ord(res)-ord('A')] -= 1

	for i, c in enumerate(count):
		if c < goal:
			sol += chr(ord('A')+i)
			break

	idx = []
	for i, c in enumerate(clues):
		if c.startswith(sol): idx.append(i)
	return sol


def main():
	T, F = list(map(int,stdin.readline().strip().split()))

	for t in range(T):
		clues = ['' for _ in range(119)]
		sol = ''

		# first letter
		count = [24]*5  # 4!
		for i in range(119):
			print(5*i+1)
			stdout.flush()
			res = stdin.readline().strip()
			if res == 'N': exit(1)
			clues[i] += res
			count[ord(res)-ord('A')] -= 1

		for i, c in enumerate(count):
			if c > 0 and chr(ord('A')+i) not in sol:
				sol += chr(ord('A')+i)
				break

		idx = []
		for i, c in enumerate(clues):
			if c.startswith(sol): idx.append(i)

		# 2nd
		count = [6]*5
		for i in idx:
			print(5*i+2)
			stdout.flush()
			res = stdin.readline().strip()
			if res == 'N': exit(1)
			clues[i] += res
			count[ord(res)-ord('A')] -= 1

		for i, c in enumerate(count):
			if c > 0 and chr(ord('A')+i) not in sol:
				sol += chr(ord('A')+i)
				break

		idx = []
		for i, c in enumerate(clues):
			if c.startswith(sol): idx.append(i)

		# 3rd
		count = [2]*5
		for i in idx:
			print(5*i+3)
			stdout.flush()
			res = stdin.readline().strip()
			if res == 'N': exit(1)
			clues[i] += res
			count[ord(res)-ord('A')] -= 1

		for i, c in enumerate(count):
			if c > 0 and chr(ord('A')+i) not in sol:
				sol += chr(ord('A')+i)
				break

		idx = []
		for i, c in enumerate(clues):
			if c.startswith(sol): idx.append(i)


		# 4th
		count = [1]*5
		for i in idx:
			print(5*i+4)
			stdout.flush()
			res = stdin.readline().strip()
			if res == 'N': exit(1)
			clues[i] += res
			count[ord(res)-ord('A')] -= 1

		for i, c in enumerate(count):
			if c > 0 and chr(ord('A')+i) not in sol:
				sol += chr(ord('A')+i)
				break

		idx = []
		for i, c in enumerate(clues):
			if c.startswith(sol): idx.append(i)

		# out
		for c in 'ABCDE':
			if c not in sol:
				sol += c
				break

		print(sol)
		stdout.flush()
		res = stdin.readline().strip()
		if res == 'N': exit(1)

	
 
if __name__ == '__main__':
	main()