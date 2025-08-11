''' ESAb ATAd
https://codingcompetitions.withgoogle.com/codejam/round/000000000019fd27/0000000000209a9e
'''

# python interactive_runner.py python local_testing_tool.py 0 -- python3 d.py

from sys import stdin, stdout, stderr

def query(x):
	print(x)
	stdout.flush()
	xx = stdin.readline().strip()
	if xx == 'N': exit(1)
	# stderr.write('querying {} returns {}\n'.format(x,xx))
	return xx


def solve(B):
	l00,l01,l10,l11 = [],[],[],[]
	i = 1
	while True:
		# mirror
		if not l00 and not l11:
			_ = query(1)
		elif l00:
			x = query(l00[0])
			if x == '1': l00,l11 = l11,l00
		elif l11:
			x = query(l11[0])
			if x == '0': l00,l11 = l11,l00

		# opposite
		if not l01 and not l10:
			_ = query(1)
		elif l01:
			x = query(l01[0])
			if x == '1': l10,l01 = l01, l10
		elif l10:
			x = query(l10[0])
			if x == '0': l10,l01 = l01, l10

		# new
		done = False
		for _ in range(4):
			x = query(i)
			y = query(B-i+1)
			if x == '0' and y == '0':
				l00.append(i)
			elif x == '0' and y == '1':
				l01.append(i)
			elif x == '1' and y == '0':
				l10.append(i)
			elif x == '1' and y == '1':
				l11.append(i)
			i += 1
			if i > B//2:
				done = True
				break

		if done: break

	# stderr.write('final: l00={}, l01={}, l10={}, l11={}\n'.format(l00,l01,l10,l11))

	res = [-1]*B
	for i in l00:
		res[i-1] = 0
		res[-i] = 0
	for i in l01:
		res[i-1] = 0
		res[-i] = 1
	for i in l10:
		res[i-1] = 1
		res[-i] = 0
	for i in l11:
		res[i-1] = 1
		res[-i] = 1

	_ = query(''.join(list(map(str,res))))
		


def main():
	T, B = list(map(int,stdin.readline().strip().split()))
	for t in range(T):
		solve(B)
	
 
if __name__ == '__main__':
	main()