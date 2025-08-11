''' Problem A2: Consistency - Chapter 2
https://www.facebook.com/codingcompetitions/hacker-cup/2021/qualification-round/problems/A2
'''


def solve(s, edges):
	count = [0]*26
	for c in s:
		count[ord(c)-ord('A')] += 1
	
	adj = [[] for _ in range(26)]
	for edge in edges:
		u, v = ord(edge[0])-ord('A'), ord(edge[1])-ord('A')
		adj[u].append(v)

	# bfs
	dist = [[float('inf')]*26 for _ in range(26)]
	for i in range(26):
		cur = set([i])
		seen = set([i])
		d = 0
		while cur:
			nxt = set()
			for u in cur:
				dist[i][u] = min(dist[i][u], d)
				for v in adj[u]: 
					if v in seen: continue
					seen.add(v)
					nxt.add(v)
			d += 1
			cur = nxt

	res = float('inf')
	for i in range(26):
		cand = sum(dist[j][i]*c for j,c in enumerate(count) if c>0)
		res = min(res, cand)
	
	return res if res < float('inf') else -1


def main():
	from sys import stdin
	
	T = int(stdin.readline().strip())
	for t in range(T):
		s = stdin.readline().strip()
		k = int(stdin.readline().strip())
		edges = [stdin.readline().strip() for _ in range(k)]
		out = solve(s, edges)
		print('Case #{}: {}'.format(t+1, out))


def gen():
	import random
	random.seed(12)

	T = 1000
	print(T)
	for _ in range(T):
		N = random.randint(1,100)
		s = [random.randint(0,25) for _ in range(N)]
		s = [chr(i+ord('A')) for i in s]
		print(''.join(s))

		K = random.randint(0,300)
		print(K)
		edges = set()
		while len(edges) < K:
			a = chr(random.randint(0,25)+ord('A'))
			b = chr(random.randint(0,25)+ord('A'))
			edges.add((a,b))
		for a,b in edges:
			print(f'{a}{b}')


if __name__ == '__main__':
	main()
