''' C - XX to XXX
https://atcoder.jp/contests/abc259/tasks/abc259_c
'''

import io, os, sys
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

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
    S = input().decode().strip()
    T = input().decode().strip()

    def count(s):
        res = []
        cnt = 1
        for i in range(1, len(s)):
            if s[i] != s[i-1]:
                res.append((s[i-1], cnt))
                cnt = 0
            cnt += 1
        res.append((s[-1], cnt))
        return res
    
    count_S = count(S)
    count_T = count(T)

    if len(count_S) != len(count_T): return False

    for ((s, cs), (t, ct)) in zip(count_S, count_T):
        if s != t or cs > ct: return False
        if cs < ct and cs == 1: return False
    
    return True



if __name__ == '__main__':
    out = main()
    print('Yes' if out else 'No')

