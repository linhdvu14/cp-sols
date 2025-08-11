''' Operations on a Tuple
https://www.codechef.com/JUNE20B/problems/TTUPLE

'''

# 	A	B	C
# 	---------
# 1	x		
# 		x	x
# 	---------
# 2	x		
# 	x	x	x
# 	---------
# 3	x	x	
# 		x	x
# 	---------
# 4	x	x	
# 	x	x	x
# 	---------
# 5	x	x	x
# 	x
# 	---------
# 6	x	x	x
# 	x	x
# 	---------
# 7	x	x	x
# 	x	x	x


UNK = float('inf')

def same(v1,v2): return v1==v2 and v1!=UNK

def divide(x,y): return y//x if x!=0 and y%x==0 else UNK

# can find integers m,b s.t. mx+b=y for all x,y
def has_sol(x1,y1,x2,y2,x3,y3):
	m1, m2 = divide(x1-x2,y1-y2), divide(x2-x3,y2-y3)
	if not same(m1,m2): return False
	b1, b2 = y1-m1*x1, y2-m2*x2
	return b1==b2

# can get 3 pairs in 2 steps
def check(pairs,da,dm):
	p1,p2,p3 = pairs[0],pairs[1],pairs[2]
	for p1,p2,p3 in [(p1,p2,p3),(p1,p3,p2),(p2,p1,p3),(p2,p3,p1),(p3,p1,p2),(p3,p2,p1)]:
		x1,y1,x2,y2,x3,y3 = *p1,*p2,*p3

		#1: A1,B2,C2
		if da[p2]==da[p3] or same(dm[p2],dm[p3]): return True

		#2: A12,B2,C2
		if same(dm[p2],dm[p3]) and y1%dm[p2]==0: return True  # add-mult
		if da[p2]==da[p3] and divide(x1,y1-da[p2]): return True  # mult-add

		#3: A1, B12, C2
		if da[p2]==da[p1]+da[p3]: return True  # add-add
		if dm[p2]!=UNK and dm[p2]==dm[p1]*dm[p3] : return True  # mult-mult
		if dm[p3]!=UNK and (x2+da[p1])*dm[p3]==y2: return True  # add-mult
		if dm[p1]!=UNK and (x2*dm[p1])+da[p3]==y2: return True  # mult-add

		#4: A12, B12, C2
		if dm[p3]!=UNK:  # add-mult
			d1, d2 = divide(dm[p3],y1), divide(dm[p3],y2)
			if d1!=UNK and d2!=UNK and d1-x1==d2-x2: return True
		if same(divide(x1,y1-da[p3]), divide(x2,y2-da[p3])): return True  # mult-add

		#5: A12,B1,C1
		if da[p2]==da[p3] and divide(x1+da[p2],y1)!=UNK: return True  # add-mult
		if same(dm[p2],dm[p3]): return True  # mult-add

		#6: A12,B12,C1
		if same(divide(x1+da[p3],y1),divide(x2+da[p3],y2)): return True  # add-mult
		if dm[p3]!=UNK and y1-x1*dm[p3]==y2-x2*dm[p3]: return True   # mult-add
		
		#7: A12,B12,C12	
		if has_sol(x1,y1,x2,y2,x3,y3): return True

	return False


def solve(x1,x2,x3,y1,y2,y3):
	pairs = list(set([(x,y) for x,y in zip((x1,x2,x3),(y1,y2,y3)) if x!=y]))

	if len(pairs)<2: return len(pairs)

	da, dm, dm_valid = {}, {}, {}
	for x,y in pairs:
		da[x,y] = y-x
		dm[x,y] = divide(x,y)
		if dm[x,y] != UNK: dm_valid[x,y] = dm[x,y]

	# 1 step
	if len(set(da.values()))==1 or (len(dm_valid)==len(pairs) and len(set(dm_valid.values()))==1): return 1

	# 2 steps, same op without overlap
	if len(set(da.values()))==2 or (len(dm_valid)==len(pairs) and len(set(dm_valid.values()))==2): return 2

	# 2 pairs
	if len(pairs)==2: return 2

	# 3 pairs, check if possible with 2 steps
	if check(pairs,da,dm): return 2
	
	return 3


def main():
	from sys import stdin
	
	T = int(stdin.readline().strip())
	for _ in range(T):
		p,q,r = list(map(int,stdin.readline().strip().split()))
		a,b,c = list(map(int,stdin.readline().strip().split()))
		out = solve(p,q,r,a,b,c)
		print(out)


if __name__ == '__main__':
	main()

