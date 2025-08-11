''' B. Was it Rated?
https://codeforces.com/contest/1812/problem/B
'''

import io, os, sys
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

i = int(input())
if i in [15, 20, 21]: print('NO')
else: print('YES')
