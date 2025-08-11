''' Cheerio Contest 3 P2 - Double-O-Seven
https://dmoj.ca/problem/cheerio3p2
'''

import os, sys
input = sys.stdin.readline  # strip() if str

def debug(*args):   
    if os.environ.get('debug') in [None, '0']: return
    from inspect import currentframe, getframeinfo
    from re import search
    frame = currentframe().f_back
    s = getframeinfo(frame).code_context[0]
    r = search(r"\((.*)\)", s).group(1)
    vnames = r.split(', ')
    var_and_vals = [f'{var}={val}' for var, val in zip(vnames, args)]
    prefix = f'{currentframe().f_back.f_lineno:02d}: '
    print(f'{prefix}{", ".join(var_and_vals)}')

INF = float('inf')

# -----------------------------------------


def main():
    N = int(input())
    S = input().strip()

    res = me = them = 0
    for c in S:
        if c == 'B': # R
            me += 1
        elif c == 'R':
            them += 1
            if not me: # R
                me += 1
            else: # F
                me -= 1
                res += 1
        else:
            if them: # B
                them -= 1
            else:
                if not me: # R
                    me += 1
                else: # F
                    me -= 1
                    res += 1
    
    print(res)


if __name__ == '__main__':
    main()

