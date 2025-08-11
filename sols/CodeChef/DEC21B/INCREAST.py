''' Increasing String
https://www.codechef.com/DEC21B/problems/INCREAST
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

def solve(S):
    # how many left of each type
    cnt = [0]*26
    for c in S: cnt[ord(c)-ord('a')] += 1

    # remove current char if
    # * orig string has smaller char behind
    # * current char > first char of removed suffix
    # * current char == first char of removed suffix, > second unique char of removed suffix
    pref = suff = suff2 = ''
    for c in S:
        i = ord(c) - ord('a')
        cnt[i] -= 1

        rm = any(cnt[j] > 0  for j in range(i))
        if len(suff) > 0:
            if c > suff[0]: rm = True
            if c == suff[0] and suff2 != '' and c > suff2: rm = True
        
        if rm:
            suff += c
            if suff2 == '' and c != suff[0]: suff2 = c
        else:
            pref += c

    return pref + suff


def main():
    T = int(input())
    for _ in range(T):
        S = input().decode().strip()
        out = solve(S)
        output(f'{out}\n')


if __name__ == '__main__':
    main()

