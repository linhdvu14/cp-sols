def searchleft(arr,bound):  # last element strictly smaller than bound
	lo, hi = 0, len(arr)-1
	res = -1
	while lo <= hi:
		mi = lo + (hi-lo) // 2
		if arr[mi] >= bound: # discard right
			hi = mi-1
		else:  # search right
			res = mi
			lo = mi+1
	return res

def searchright(arr,bound):  # first element strictly greater than bound
	lo, hi = 0, len(arr)-1
	res = len(arr)
	while lo <= hi:
		mi = lo + (hi-lo) // 2
		if arr[mi] <= bound:  # discard left
			lo = mi+1
		else:  # search left
			res = mi
			hi = mi-1
	return res

def solve(n, arr):
	arr = sorted([abs(a) for a in arr if a != 0])

	# count (x,y) where |x| <= |y| <= 2|x|
	res = 0
	for x in arr:
		i, j = searchleft(arr, x), searchright(arr, 2*x)
		res += j-i-2
		# print('{} {}: {}..{} --> add {}, res={}'.format(arr,x,i,j,j-i-2,res))

	# count (x,x)
	res -= len(arr) - len(set(arr))

	return res


def test():
	from sys import stdin
	T = int(stdin.readline().strip())
	for _ in range(T):
		n = int(stdin.readline().strip())
		arr = list(map(int,stdin.readline().strip().split()))
		print(solve(n, arr))

def main():
	from sys import stdin
	n = int(stdin.readline().strip())
	arr = list(map(int,stdin.readline().strip().split()))
	print(solve(n, arr))


if __name__ == '__main__':
	main()