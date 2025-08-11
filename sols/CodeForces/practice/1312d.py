''' D. Count the Arrays

Your task is to calculate the number of arrays such that:
* each array contains 𝑛 elements;
* each element is an integer from 1 to 𝑚;
* for each array, there is exactly one pair of equal elements;
* for each array 𝑎, there exists an index 𝑖 such that the array is strictly ascending before the 𝑖-th element and strictly descending after it (formally, it means that 𝑎𝑗<𝑎𝑗+1, if 𝑗<𝑖, and 𝑎𝑗>𝑎𝑗+1, if 𝑗≥𝑖 ). 

Input

The first line contains two integers n and 𝑚 (2≤𝑛≤𝑚≤2⋅105).
Output

Print one integer — the number of arrays that meet all of the aforementioned conditions, taken modulo 998244353

'''


# C(m,n-1) * (n-2) * 2^(n-3)


MOD = 998244353

def modular_inverse(a, m) : 
	if m == 1: return 0

	m0, x, y = m, 1, 0
	while a > 1:
		# q is quotient 
		q = a // m 
		t = m 
  
		# m is remainder
		m = a % m 
		a = t 
		t = y 
  
		# update x and y 
		y = x - q * y 
		x = t 
  
	# make x positive 
	if x < 0: 
		x += m0
  
	return x 

def pow(n):
	if n <= 0: return 1
	if n == 1: return 2
	x = (pow(n//2)) % MOD
	return (x*x) % MOD if n % 2 == 0 else (x*x*2) % MOD


def solve(n,m):
	if n < 3: return 0

	num = ((n-2) * pow(n-3)) % MOD
	for i in range(m,n-1,-1):
		num = (num*i) % MOD

	denom = 1
	for i in range(1,m-n+2):
		denom = (denom*i) % MOD

	return (num*modular_inverse(denom, MOD)) % MOD



def main():
	from sys import stdin
	
	T = int(stdin.readline().strip())
	for _ in range(T):
		n, m = list(map(int,stdin.readline().strip().split()))
		print(solve(n,m))
 
if __name__ == '__main__':
	main()