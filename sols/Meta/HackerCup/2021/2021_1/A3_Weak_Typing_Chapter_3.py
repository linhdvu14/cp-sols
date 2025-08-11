''' Problem A3: Weak Typing - Chapter 3
https://www.facebook.com/codingcompetitions/hacker-cup/2021/round-1/problems/A3
'''

# Given string A, find all flip index pairs (i, j) of A
# |A| = len(A)
# LI(A), LV(A) = index, value of leftmost non-F char
# RI(A), RV(A) = index, value of rightmost non-F char
# P(A) = num flip pairs (i, j)
# L(A) = SUM i+1
# R(A) = SUM |A|-j
# G(A) = SUM_(i,j) (i+1)(|A|-j) = num flips over all substrings of A

# Let C = A+B, then
# LI(C), LV(C) = LI(A), LV(A)
# RI(C), RV(C) = RI(B) + |A|, RV(B)
# P(C) = P(A) + P(B) + (RV(A) != LV(B))
# L(C) = L(A) + L(B) + |A| * P(B) + (RV(A) != LV(B)) * (RI(A) + 1)
# R(C) = R(A) + R(B) + |B| * P(A) + (RV(A) != LV(B)) * (|B| - LI(B))
# G(C) = G(A) + L(A) * |B| + G(B) + R(B) * |A| + (RV(A) != LV(B)) * (RI(A) + 1) * (|A| + |B| - LI(B))


MOD = 10**9 + 7

def solve(U):
	def concat(SZa, LIa, LVa, RIa, RVa, Pa, La, Ra, Ga, SZb, LIb, LVb, RIb, RVb, Pb, Lb, Rb, Gb):
		flip = 1 if RVa and LVb and RVa != LVb else 0   # flip in middle 
		SZc = (SZa + SZb) % MOD
		LIc, LVc = LIa, LVa
		if not LVa and LVb: LIc, LVc = SZa + LIb, LVb
		RIc, RVc = RIb + SZa, RVb 
		if not RVb and RVa: RIc, RVc = RIa, RVa
		Pc = (Pa + Pb + flip) % MOD
		Lc = (La + Lb + SZa * Pb + flip * (RIa + 1)) % MOD
		Rc = (Ra + Rb + SZb * Pa + flip * (SZb - LIb)) % MOD
		Gc = (Ga + La * SZb + Gb + Rb * SZa + flip * (RIa + 1) * (SZb - LIb)) % MOD
		return SZc, LIc, LVc, RIc, RVc, Pc, Lc, Rc, Gc

	SZ, LI, LV, RI, RV, P, L, R, G = 0, -1, '', -1, '', 0, 0, 0, 0
	for c in U:
		if c == 'F': SZ, LI, LV, RI, RV, P, L, R, G = concat(SZ, LI, LV, RI, RV, P, L, R, G, 1, -1, '', -1, '', 0, 0, 0, 0)
		elif c == 'X': SZ, LI, LV, RI, RV, P, L, R, G = concat(SZ, LI, LV, RI, RV, P, L, R, G, 1, 0, 'X', 0, 'X', 0, 0, 0, 0)
		elif c == 'O': SZ, LI, LV, RI, RV, P, L, R, G = concat(SZ, LI, LV, RI, RV, P, L, R, G, 1, 0, 'O', 0, 'O', 0, 0, 0, 0)
		elif c == '.': SZ, LI, LV, RI, RV, P, L, R, G = concat(SZ, LI, LV, RI, RV, P, L, R, G, SZ, LI, LV, RI, RV, P, L, R, G)

	return G


def main():
	from sys import stdin
	
	T = int(stdin.readline().strip())
	for t in range(T):
		_ = int(stdin.readline().strip())
		u = stdin.readline().strip()
		out = solve(u)
		print('Case #{}: {}'.format(t+1, out))


if __name__ == '__main__':
	main()
