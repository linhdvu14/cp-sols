''' Incremental House of Pancakes
https://codingcompetitions.withgoogle.com/codejam/round/000000000019ffb9/00000000003384ea
'''



def solve(L,R):
	# equalize: find max n s.t. 1+2+...+n <= abs(L-R)
	# can also estimate floor(sqrt(2*abs(R-L)))
	n, lo, hi = 0, 0, abs(L-R)
	while lo <= hi:
		mi = lo + (hi-lo)//2
		s = mi*(mi+1)//2
		if s <= abs(L-R):
			n = mi
			lo = mi+1
		else:
			hi = mi-1

	if R > L:
		R -= n*(n+1)//2
	else:
		L -= n*(n+1)//2

	swap = L < R
	if swap: L,R = R,L

	# L first: max p s.t. (n+1) + (n+3) + ... + (n+2p+1) = n(p+1) + (p+1)^2 = (n+p+1)(p+1) <= L
	p, lo, hi = -1, 0, L
	while lo <= hi:
		mi = lo + (hi-lo)//2
		s = (n+mi+1)*(mi+1)
		if s <= L:
			p = mi
			lo = mi+1
		else:
			hi = mi-1
	if p >= 0: L -= (n+p+1)*(p+1)

	# R: max q s.t. (n+2) + (n+4) + ... + (n+2q) = nq + q(q+1) = (n+q+1)*q <= R
	q, lo, hi = -1, 1, R
	while lo <= hi:
		mi = lo + (hi-lo)//2
		s = (n+mi+1)*mi
		if s <= R:
			q = mi
			lo = mi+1
		else:
			hi = mi-1
	if q >= 0: R -= (n+q+1)*q

	end = max(n,n+2*p+1,n+2*q)
	if swap: L,R = R,L
	return end,L,R



def main():
	from sys import stdin
	
	T = int(stdin.readline().strip())

	for t in range(T):
		L,R = list(map(int,stdin.readline().strip().split()))
		end,l,r = solve(L,R)
		print('Case #{}: {} {} {}'.format(t+1,end,l,r))


if __name__ == '__main__':
	main()
