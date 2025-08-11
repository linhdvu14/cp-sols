''' X or What? 
https://codingcompetitions.withgoogle.com/kickstart/round/0000000000051061/0000000000161426
'''

# ------------------------- small
def get_parity(num):
	return sum( ( num & (1 << i) == (1<<i) )  for i in range(11)) % 2

def update(ones, i, old, new):
	out = ones
	if old == 1: out = [j for j in ones if j != i]
	if new == 1: out.append(i)
	return out

def get_bounds(ones):
	left, right = len(ones), -1
	for i in ones:
		if i < left: left = i
		if i > right: right = i
	return left, right


def solve_small(n, nums, changes):
	nums = [get_parity(num) for num in nums]
	changes = [(i, get_parity(num)) for i,num in changes]
	s = sum(nums) % 2

	ones = [i for i, num in enumerate(nums) if num==1]

	out = []
	for i,new in changes:
		old = nums[i]
		ones = update(ones, i, old, new)
		s = (s + old + new) % 2
		if s == 0:
			out.append(n)
		else:
			left, right = get_bounds(ones)
			out.append(max(n-left-1, right))
		nums[i] = new
	return out


# ------------------------- big
from random import random
from math import log

class Node(object):
    __slots__ = 'value', 'next', 'width'
    def __init__(self, value, next, width):
        self.value, self.next, self.width = value, next, width

class End(object):
    'Sentinel object that always compares greater than another object'
    def __cmp__(self, other):
        return 1

NIL = Node(End(), [], [])               # Singleton terminator node

class IndexableSkiplist:
    'Sorted collection supporting O(lg n) insertion, removal, and lookup by rank.'

    def __init__(self, expected_size=100):
        self.size = 0
        self.maxlevels = int(1 + log(expected_size, 2))
        self.head = Node('HEAD', [NIL]*self.maxlevels, [1]*self.maxlevels)

    def __len__(self):
        return self.size

    def __getitem__(self, i):
        node = self.head
        i += 1
        for level in reversed(range(self.maxlevels)):
            while node.width[level] <= i:
                i -= node.width[level]
                node = node.next[level]
        return node.value

    def insert(self, value):
        # find first node on each level where node.next[levels].value > value
        chain = [None] * self.maxlevels
        steps_at_level = [0] * self.maxlevels
        node = self.head
        for level in reversed(range(self.maxlevels)):
            while node.next[level].value <= value:
                steps_at_level[level] += node.width[level]
                node = node.next[level]
            chain[level] = node

        # insert a link to the newnode at each level
        d = min(self.maxlevels, 1 - int(log(random(), 2.0)))
        newnode = Node(value, [None]*d, [None]*d)
        steps = 0
        for level in range(d):
            prevnode = chain[level]
            newnode.next[level] = prevnode.next[level]
            prevnode.next[level] = newnode
            newnode.width[level] = prevnode.width[level] - steps
            prevnode.width[level] = steps + 1
            steps += steps_at_level[level]
        for level in range(d, self.maxlevels):
            chain[level].width[level] += 1
        self.size += 1

    def remove(self, value):
        # find first node on each level where node.next[levels].value >= value
        chain = [None] * self.maxlevels
        node = self.head
        for level in reversed(range(self.maxlevels)):
            while node.next[level].value < value:
                node = node.next[level]
            chain[level] = node
        if value != chain[0].next[0].value:
            raise KeyError('Not Found')

        # remove one link at each level
        d = len(chain[0].next[0].next)
        for level in range(d):
            prevnode = chain[level]
            prevnode.width[level] += prevnode.next[level].width[level] - 1
            prevnode.next[level] = prevnode.next[level].next[level]
        for level in range(d, self.maxlevels):
            chain[level].width[level] -= 1
        self.size -= 1

    def __iter__(self):
        'Iterate over values in sorted order'
        node = self.head.next[0]
        while node is not NIL:
            yield node.value
            node = node.next[0]


def get_parity(num):
	return sum( ( num & (1 << i) == (1<<i) )  for i in range(11)) % 2


def solve_big(n, nums, changes):
	nums = [get_parity(num) for num in nums]
	changes = [(i, get_parity(num)) for i,num in changes]
	s = sum(nums) % 2

	ones = IndexableSkiplist(n)
	for i,num in enumerate(nums):
		if num == 1: ones.insert(i)

	out = []
	for i,new in changes:
		old = nums[i]
		if old == 1: ones.remove(i)
		if new == 1: ones.insert(i)
		s = (s + old + new) % 2
		if s == 0:
			out.append(n)
		else:
			left = ones.__getitem__(0)
			right = ones.__getitem__(ones.size-1)
			out.append(max(n-left-1, right))
		nums[i] = new
	return out


solve = solve_big

def main():
	from sys import stdin
	
	T = int(stdin.readline().strip())
	for t in range(T):
		n, q = list(map(int,stdin.readline().strip().split()))
		nums = list(map(int,stdin.readline().strip().split()))
		changes = [tuple(map(int,stdin.readline().strip().split())) for _ in range(q)]
		out = solve(n, nums, changes)
		print('Case #{}: {}'.format(t+1, ' '.join(map(str,out))))


if __name__ == '__main__':
	main()