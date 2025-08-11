''' Candies 
https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ff43/0000000000337b4d
'''

# pypi2

HEIGHT = 20

class SegmentTreeSum(object):
	def __init__(self, nums):
		def construct(tree, nums, ti, tlo, thi):  # tree[ti] = sum(nums[tlo..thi])
			if tlo == thi:
				tree[ti] = nums[tlo]
			else:
				tmi = tlo + (thi - tlo)//2
				construct(tree, nums, 2*ti+1, tlo, tmi)
				construct(tree, nums, 2*ti+2, tmi+1, thi)
				tree[ti] = tree[2*ti+1] + tree[2*ti+2]

		size = 2**(HEIGHT+1) - 1

		self.tree = [0]*size
		self.N = len(nums)
		construct(self.tree, nums, 0, 0, self.N-1)

	
	def query(self, qlo, qhi): 
		# returns the portion of nums[qlo..qhi] covered by node
		# tree[ti] which covers nums[tlo..thi]
		def helper(tree, ti, tlo, thi, qlo, qhi):
			if qlo > thi or qhi < tlo: return 0
			if qlo <= tlo <= thi <= qhi: return tree[ti]
			
			tmi = tlo + (thi - tlo)//2
			left = helper(tree, 2*ti+1, tlo, tmi, qlo, qhi)
			right = helper(tree, 2*ti+2, tmi+1, thi, qlo, qhi)
			return left + right

		return helper(self.tree, 0, 0, self.N-1, qlo, qhi)


	def add(self, qi, diff):
		# updates tree[ti] which covers nums[tlo..thi] and
		# any descendants that includes nums[i], 
		# where nums[i] is incremented by diff
		def helper(tree, ti, tlo, thi, qi, diff):
			if qi < tlo or qi > thi: return
			tree[ti] += diff
			if tlo < thi:  # update descendants if internal node
				tmi = tlo + (thi - tlo)//2
				helper(tree, 2*ti+1, tlo, tmi, qi, diff)
				helper(tree, 2*ti+2, tmi+1, thi, qi, diff)
		helper(self.tree, 0, 0, self.N-1, qi, diff)


# A[l]*1 - A[l+1]*2 + A[l+2]*3 - ... +/- A[r]*(r-l+1)
# = A[l]*[l-(l-1)] - A[l+1]*[(l+1)-(l-1)] + A[l+2]*[(l+2)-(l-1)] - ... +/- A[r]*[r-(l-1)]
# = A[l]*l - A[l+1]*(l+1) + A[l+2]*(l-2) - ... +/- A[r]*r
#	- (A[l] - A[l+1] + A[l+2] - ...  +/- A[r])*(l-1)
def solve(N,nums,queries):
	def pref(tree):
		res = []
		for i in range(N):
			res.append(tree.query(0,i))
		return res

	nums1 = [(i+1)*num*(-1)**(i%2) for i,num in enumerate(nums)]
	nums2 = [num*(-1)**(i%2) for i,num in enumerate(nums)]
	tree1 = SegmentTreeSum(nums1)
	tree2 = SegmentTreeSum(nums2)

	res = 0
	for query in queries:
		ts = query.split()
		v1,v2  = int(ts[1]), int(ts[2])
		if ts[0] == 'Q':
			l,r = v1-1,v2-1
			s1 = tree1.query(l,r)
			s2 = tree2.query(l,r)
			s = s1 - s2*l
			res += s*(-1)**(l%2)
		else:
			i,v = v1-1,v2
			d1, d2 = (i+1)*(v-nums[i])*(-1)**(i%2), (v-nums[i])*(-1)**(i%2)
			tree1.add(i,d1)
			tree2.add(i,d2)
			nums[i] = v

	return res


def main():
	from sys import stdin
	
	T = int(stdin.readline().strip())

	for t in range(T):
		N,Q = list(map(int,stdin.readline().strip().split()))
		nums = list(map(int,stdin.readline().strip().split()))
		queries = [stdin.readline().strip() for _ in range(Q)]
		out = solve(N,nums,queries)
		print 'Case #{}: {}'.format(t+1, out)


if __name__ == '__main__':
	main()