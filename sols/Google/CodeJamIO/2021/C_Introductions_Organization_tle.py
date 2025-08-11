''' C. Introductions Organization
'''

def solve(M,N,P,conn,pairs):
	def bfs(start,end):
		if end in conn[start]: return 0
		res = 1
		cur = [m for m in conn[start] if m<M]
		seen = set(cur + [start])
		while cur:
			nxt = []
			for u in cur:
				for v in conn[u]:
					if v == end: return res
					if v in seen or v>=M: continue
					seen.add(v)
					nxt.append(v)
			cur = nxt
			res += 1
		return -1

	res = [bfs(u,v) for u,v in pairs]
	return res


def main():
	from sys import stdin
	
	T = int(stdin.readline().strip())

	for t in range(T):
		M,N,P = list(map(int,stdin.readline().strip().split()))
		conn = [set() for _ in range(M+N)]
		for i in range(M+N):
			S = stdin.readline().strip()
			for j,known in enumerate(S):
				if i!=j and known=='Y':
					conn[i].add(j)
					conn[j].add(i)
		pairs = []
		for _ in range(P):
			i,j = list(map(int,stdin.readline().strip().split()))
			pairs.append((i-1,j-1))
		out = solve(M,N,P,conn,pairs)
		print('Case #{}: {}'.format(t+1, ' '.join(map(str,out))))


if __name__ == '__main__':
	main()