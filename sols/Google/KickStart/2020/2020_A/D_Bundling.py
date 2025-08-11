''' Bundling
https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ffc7/00000000001d3ff3
'''

# python2 (RE with max recursion depth)/ pypy2

class TrieNode(object):
	def __init__(self, d, v):
		self.links = {}
		self.depth = d
		self.val = v
		self.count = 0


class Trie(object):
	def __init__(self):
		self.root = TrieNode(0, '')
		
	def insert(self, word):
		curr = self.root
		curr.count += 1
		for char in word:
			if char not in curr.links: curr.links[char] = TrieNode(curr.depth+1, char)
			curr = curr.links[char]
			curr.count += 1

	# def print(self):
	# 	curr = [self.root]
	# 	i = 0
	# 	while curr:
	# 		nxt = []
	# 		for n in curr:
	# 			print 'lv={}, v={}, count={}, depth={}'.format(i,n.val,n.count,n.depth)
	# 			nxt.extend(n.links.values())
	# 		curr = nxt
	# 		i += 1



def solve(vals,n,k):
	trie = Trie()
	for v in vals:
		trie.insert(v)
	# trie.print()

	def dfs(node): # return sum prefix lengths, num nodes used in sum
		if node.count < k: 
			return 0, 0
		s, n = 0, 0
		for child in node.links.values():
			ss, nn = dfs(child)
			s += ss
			n += nn
		rem = node.count - n
		# print('1 node.val={}, depth={}, count={}, s={}, n={}, rem={}'.format(node.val,node.depth,node.count,s,n,rem))
		s += (rem // k) * node.depth
		n += rem-rem % k
		# print('2 node.val={}, depth={}, count={}, s={}, n={}, rem={}'.format(node.val,node.depth,node.count,s,n,rem))
		return s, n

	return dfs(trie.root)[0]



def main():
	from sys import stdin
	
	T = int(stdin.readline().strip())

	for t in range(T):
		n,k = list(map(int,stdin.readline().strip().split()))
		vals = [stdin.readline().strip() for _ in range(n)]
		out = solve(vals,n,k)
		print 'Case #{}: {}'.format(t+1, out)


if __name__ == '__main__':
	main()