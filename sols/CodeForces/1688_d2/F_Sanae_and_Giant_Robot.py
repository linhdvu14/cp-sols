''' F. Sanae and Giant Robot
https://codeforces.com/contest/1688/problem/F
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

DEBUG = os.environ.get('debug') not in [None, '0']

if DEBUG:
    from inspect import currentframe, getframeinfo
    from re import search

def debug(*args):
    if not DEBUG: return
    frame = currentframe().f_back
    s = getframeinfo(frame).code_context[0]
    r = search(r"\((.*)\)", s).group(1)
    vnames = r.split(', ')
    var_and_vals = [f'{var}={val}' for var, val in zip(vnames, args)]
    prefix = f'{currentframe().f_back.f_lineno:02d}: '
    print(f'{prefix}{", ".join(var_and_vals)}')


INF = float('inf')

# -----------------------------------------

class SortedList:
    def __init__(self, iterable=[], _load=200):
        '''Initialize sorted list instance.'''
        values = sorted(iterable)
        self._len = _len = len(values)
        self._load = _load
        self._lists = _lists = [values[i:i + _load] for i in range(0, _len, _load)]
        self._list_lens = [len(_list) for _list in _lists]
        self._mins = [_list[0] for _list in _lists]
        self._fen_tree = []
        self._rebuild = True

    def add(self, value):
        '''Add `value` to sorted list.'''
        _load = self._load
        _lists = self._lists
        _mins = self._mins
        _list_lens = self._list_lens

        self._len += 1
        if _lists:
            pos, idx = self._loc_right(value)
            self._fen_update(pos, 1)
            _list = _lists[pos]
            _list.insert(idx, value)
            _list_lens[pos] += 1
            _mins[pos] = _list[0]
            if _load + _load < len(_list):
                _lists.insert(pos + 1, _list[_load:])
                _list_lens.insert(pos + 1, len(_list) - _load)
                _mins.insert(pos + 1, _list[_load])
                _list_lens[pos] = _load
                del _list[_load:]
                self._rebuild = True
        else:
            _lists.append([value])
            _mins.append(value)
            _list_lens.append(1)
            self._rebuild = True

    def discard(self, value):
        '''Remove `value` from sorted list if it is a member.'''
        _lists = self._lists
        if _lists:
            pos, idx = self._loc_right(value)
            if idx and _lists[pos][idx - 1] == value:
                self._delete(pos, idx - 1)

    def remove(self, value):
        '''Remove `value` from sorted list; `value` must be a member.'''
        _len = self._len
        self.discard(value)
        if _len == self._len: raise ValueError('{0!r} not in list'.format(value))

    def pop(self, index=-1):
        '''Remove and return value at `index` in sorted list.'''
        pos, idx = self._fen_findkth(self._len + index if index < 0 else index)
        value = self._lists[pos][idx]
        self._delete(pos, idx)
        return value

    def bisect_left(self, value):
        '''Return the first index to insert `value` in the sorted list.'''
        pos, idx = self._loc_left(value)
        return self._fen_query(pos) + idx

    def bisect_right(self, value):
        '''Return the last index to insert `value` in the sorted list.'''
        pos, idx = self._loc_right(value)
        return self._fen_query(pos) + idx

    def count(self, value):
        '''Return number of occurrences of `value` in the sorted list.'''
        return self.bisect_right(value) - self.bisect_left(value)

    def _fen_build(self):
        '''Build a fenwick tree instance.'''
        self._fen_tree[:] = self._list_lens
        _fen_tree = self._fen_tree
        for i in range(len(_fen_tree)):
            if i | i + 1 < len(_fen_tree):
                _fen_tree[i | i + 1] += _fen_tree[i]
        self._rebuild = False

    def _fen_update(self, index, value):
        '''Update `fen_tree[index] += value`.'''
        if not self._rebuild:
            _fen_tree = self._fen_tree
            while index < len(_fen_tree):
                _fen_tree[index] += value
                index |= index + 1

    def _fen_query(self, end):
        '''Return `sum(_fen_tree[:end])`.'''
        if self._rebuild: self._fen_build()
        _fen_tree = self._fen_tree
        x = 0
        while end:
            x += _fen_tree[end - 1]
            end &= end - 1
        return x

    def _fen_findkth(self, k):
        '''Return a pair of (the largest `idx` such that `sum(_fen_tree[:idx]) <= k`, `k - sum(_fen_tree[:idx])`).'''
        _list_lens = self._list_lens
        if k < _list_lens[0]: return 0, k
        if k >= self._len - _list_lens[-1]: return len(_list_lens) - 1, k + _list_lens[-1] - self._len
        if self._rebuild: self._fen_build()

        _fen_tree = self._fen_tree
        idx = -1
        for d in reversed(range(len(_fen_tree).bit_length())):
            right_idx = idx + (1 << d)
            if right_idx < len(_fen_tree) and k >= _fen_tree[right_idx]:
                idx = right_idx
                k -= _fen_tree[idx]
        return idx + 1, k

    def _delete(self, pos, idx):
        '''Delete value at the given `(pos, idx)`.'''
        _lists = self._lists
        _mins = self._mins
        _list_lens = self._list_lens

        self._len -= 1
        self._fen_update(pos, -1)
        del _lists[pos][idx]
        _list_lens[pos] -= 1

        if _list_lens[pos]:
            _mins[pos] = _lists[pos][0]
        else:
            del _lists[pos]
            del _list_lens[pos]
            del _mins[pos]
            self._rebuild = True

    def _loc_left(self, value):
        '''Return an index pair that corresponds to the first position of `value` in the sorted list.'''
        if not self._len: return 0, 0
        _lists = self._lists
        _mins = self._mins

        lo, pos = -1, len(_lists) - 1
        while lo + 1 < pos:
            mi = (lo + pos) >> 1
            if value <= _mins[mi]: pos = mi
            else: lo = mi

        if pos and value <= _lists[pos - 1][-1]: pos -= 1

        _list = _lists[pos]
        lo, idx = -1, len(_list)
        while lo + 1 < idx:
            mi = (lo + idx) >> 1
            if value <= _list[mi]: idx = mi
            else: lo = mi

        return pos, idx

    def _loc_right(self, value):
        '''Return an index pair that corresponds to the last position of `value` in the sorted list.'''
        if not self._len: return 0, 0
        _lists = self._lists
        _mins = self._mins

        pos, hi = 0, len(_lists)
        while pos + 1 < hi:
            mi = (pos + hi) >> 1
            if value < _mins[mi]: hi = mi
            else: pos = mi

        _list = _lists[pos]
        lo, idx = -1, len(_list)
        while lo + 1 < idx:
            mi = (lo + idx) >> 1
            if value < _list[mi]: idx = mi
            else: lo = mi

        return pos, idx

    def __len__(self):
        '''Return the size of the sorted list.'''
        return self._len

    def __getitem__(self, index):
        '''Lookup value at `index` in sorted list.'''
        pos, idx = self._fen_findkth(self._len + index if index < 0 else index)
        return self._lists[pos][idx]

    def __delitem__(self, index):
        '''Remove value at `index` from sorted list.'''
        pos, idx = self._fen_findkth(self._len + index if index < 0 else index)
        self._delete(pos, idx)

    def __contains__(self, value):
        '''Return true if `value` is an element of the sorted list.'''
        _lists = self._lists
        if _lists:
            pos, idx = self._loc_left(value)
            return idx < len(_lists[pos]) and _lists[pos][idx] == value
        return False

    def __iter__(self):
        '''Return an iterator over the sorted list.'''
        return (value for _list in self._lists for value in _list)

    def __reversed__(self):
        '''Return a reverse iterator over the sorted list.'''
        return (value for _list in reversed(self._lists) for value in reversed(_list))

    def __repr__(self):
        '''Return string representation of sorted list.'''
        return 'SortedList({0})'.format(list(self))
 
    def val(self, it):  # added
        '''Return the value of the `it` in the sorted list.'''
        pos, idx = it
        return self._lists[pos][idx]
 
    def begin(self):  # added
        '''Return the begin of the it in the sorted list.'''
        return (0, 0)
 
    def end(self):  # added
        '''Return the end of the it in the sorted list.'''
        return (len(self._lists)-1, len(self._lists[-1])) if self._lists else (0, 0)
 
    def prev(self, it):  # added
        '''Return the previous `it` in the sorted list.'''
        if it == self.begin(): raise ValueError('{0!r} already list begin'.format(it))
        pos, idx = it
        return (pos, idx-1) if idx else (pos-1, len(self._lists[pos-1])-1)
 
    def next(self, it):  # added
        '''Return the next `it` in the sorted list.'''
        if it == self.end(): raise ValueError('{0!r} already list end'.format(it))
        pos, idx = it
        return (pos, idx+1) if pos+1 == len(self._lists) or idx+1 != len(self._lists[pos]) else (pos+1, 0)


# let C[i] = A[i] - B[i]    --> want to make C[i] all 0 by changing C[l..r] to 0, if sum(C[l..r]) == 0
# let D[i] = pref_sum(C[i]) --> want to make D[i] all 0 by changing D[l..r] to D[r], if D[r] == D[l-1]

def solve(N, M, A, B, segs):
    D = [0] * (N + 1)
    stack = [0]    # zero indices in D; each idx is moved from nonzero to stack once
    nonzero = SortedList()  # nonzero indices in D
    for i, (a, b) in enumerate(zip(A, B)): 
        D[i+1] = D[i] + a - b 
        if D[i+1] == 0: stack.append(i+1)
        else: nonzero.add(i+1)

    deg = [2] * M  # seg idx -> how many ends are nonzero
    adj = [[] for _ in range(N+1)]
    for i, (l, r) in enumerate(segs):
        adj[l-1].append(i)
        adj[r].append(i)

    while stack:
        i = stack.pop()
        for j in adj[i]:
            deg[j] -= 1
            if deg[j] == 0:  # both ends of segment j are nonzero, zero out segs[j][l]..segs[j][r]
                l, r = segs[j]
                rm = []
                k = nonzero.bisect_left(l)
                while k < len(nonzero) and nonzero[k] <= r:
                    rm.append(nonzero[k])
                    k += 1
                for v in rm:
                    nonzero.discard(v)
                    stack.append(v)
    
    return 'YES' if not nonzero else 'NO'



def main():
    T = int(input())
    for _ in range(T):
        N, M = list(map(int, input().split()))
        A = list(map(int, input().split()))
        B = list(map(int, input().split()))
        segs = [list(map(int, input().split())) for _ in range(M)]
        out = solve(N, M, A, B, segs)
        print(out)


if __name__ == '__main__':
    main()

