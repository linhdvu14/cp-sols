''' D. Irrefutable Outcome
'''

def solve(s):
	def dp(lo,hi,turn,memo):
		if lo>hi: return -1
		if (lo,hi) in memo: return memo[lo,hi]
		if turn=='I' and s[lo]==s[hi]=='O': return -(hi-lo+2)
		if turn=='O' and s[lo]==s[hi]=='I': return -(hi-lo+2)
		res = -float('inf')
		if turn=='I':
			if s[lo]=='I': res = max(res, -dp(lo+1,hi,'O',memo))
			if s[hi]=='I': res = max(res, -dp(lo,hi-1,'O',memo))
		else:
			if s[lo]=='O': res = max(res, -dp(lo+1,hi,'I',memo))
			if s[hi]=='O': res = max(res, -dp(lo,hi-1,'I',memo))
		memo[lo,hi] = res
		return res

	memo = {}
	return dp(0, len(s)-1, 'I', memo)


def main():
	from sys import stdin
	
	T = int(stdin.readline().strip())

	for t in range(T):		
		s = stdin.readline().strip()
		out = solve(s)
		if out > 0:
			print('Case #{}: I {}'.format(t+1, out))
		else:
			print('Case #{}: O {}'.format(t+1, -out))

if __name__ == '__main__':
	main()