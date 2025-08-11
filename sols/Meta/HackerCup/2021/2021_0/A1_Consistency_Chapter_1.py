''' Problem A1: Consistency - Chapter 1
https://www.facebook.com/codingcompetitions/hacker-cup/2021/qualification-round/problems/A1
'''

VOWELS = set([ord(c)-ord('A') for c in 'AEIOU'])

def solve(s):
    count = [0]*26
    for c in s:
        count[ord(c)-ord('A')] += 1

    tot_vow = sum([v for i,v in enumerate(count) if i in VOWELS])
    tot_con = sum([v for i,v in enumerate(count) if i not in VOWELS])
    res = float('inf')
    for i in range(26):
        cost = tot_con + (tot_vow-count[i])*2 if i in VOWELS else tot_vow + (tot_con-count[i])*2
        res = min(res, cost)
    return res


def main():
	from sys import stdin
	
	T = int(stdin.readline().strip())
	for t in range(T):
		s = stdin.readline().strip()
		out = solve(s)
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


if __name__ == '__main__':
	main()
