''' E. Replace the Numbers
https://codeforces.com/contest/1620/problem/E
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

DEBUG = os.environ.get('debug') is not None

if DEBUG:
    from varname.core import argname
    from inspect import currentframe

def debug(var, *more_vars):
    if not DEBUG: return
    var_names = argname('var', '*more_vars', func=debug)
    values = (var, *more_vars)
    name_and_values = [f'{var_name}={value}'  for var_name, value in zip(var_names, values)]
    prefix = f'{currentframe().f_back.f_lineno:02d}: '
    print(f'{prefix}{", ".join(name_and_values)}')


INF = float('inf')

# -----------------------------------------

def main():
    Q = int(input())
    res = []
    mp = list(range(5*10**5 + 2))
    queries = [list(map(int, input().split())) for _ in range(Q)]
    for i in range(Q-1, -1, -1):
        q = queries[i]
        if q[0] == 2:
            x, y = q[1], q[2]
            mp[x] = mp[y]
        else:
            x = q[1]
            res.append(mp[x])

    res.reverse()
    print(*res)

if __name__ == '__main__':
    main()

