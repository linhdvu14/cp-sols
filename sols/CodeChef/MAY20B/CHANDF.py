''' Chef and Bitwise Product 

https://www.codechef.com/MAY20B/problems/CHANDF

'''

def solve(X,Y,L,R):
	mx, mxz = -1, -1

	def search(i,Z,freeL,freeR):
		nonlocal mx, mxz

		if i < 0:
			res = (X & Z) * (Y & Z)
			if res > mx or (res == mx and Z < mxz): mx, mxz = res, Z
			return

		if freeL and freeR:
			Z = (Z << (i+1)) | ((X | Y) & ((1<<(i+1))-1))
			res = (X & Z) * (Y & Z)
			if res > mx or (res == mx and Z < mxz): mx, mxz = res, Z
			return

		x, y, l, r = (X >> i) & 1, (Y >> i) & 1, (L >> i) & 1, (R >> i) & 1
		Z <<= 1

		if freeL:
			if not r:
				search(i-1,Z,True,False)
			else:
				search(i-1,Z+1,True,False)
				search(i-1,Z,True,True)
			return

		if freeR:
			if l:
				search(i-1,Z+1,False,True)
			else:
				search(i-1,Z+1,True,True)
				search(i-1,Z,False,True)
			return

		if l == r:
			Z += r
			search(i-1,Z,False,False)
			return

		assert l < r
		search(i-1,Z,False,True)
		search(i-1,Z+1,True,False)

	search(42,0,False,False)
	return mxz



def main():
	from sys import stdin
	
	T = int(stdin.readline().strip())
	for t in range(T):
		X,Y,L,R = list(map(int,stdin.readline().strip().split()))
		out = solve(X,Y,L,R)
		print(out)


if __name__ == '__main__':
	main()

