''' E. Mark and Professor Koro
https://codeforces.com/contest/1705/problem/E
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


from types import GeneratorType
def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack: return f(*args, **kwargs)
        to = f(*args, **kwargs)
        while True:
            if type(to) is GeneratorType:
                stack.append(to)
                to = next(to)
            else:
                stack.pop()
                if not stack: break
                to = stack[-1].send(to)
        return to
    return wrappedfunc


class IntKeyDict(dict):
    from random import randrange
    rand = randrange(1 << 62)
    def __setitem__(self, k, v): super().__setitem__(k^self.rand, v)
    def __getitem__(self, k): return super().__getitem__(k^self.rand)
    def get(self, k, default=None): return super().get(k^self.rand, default)
    def keys(self): return [k^self.rand for k in super().keys()]
    def items(self): return [(k^self.rand, v) for k, v in super().items()]


INF = float('inf')

# -----------------------------------------


class BitArray:
    '''The i-th bit is stored in block i/64 at bit position i % 64; msb are to the right'''
    BITS_PER_WORD = 6
    WORD_SZ = 1 << BITS_PER_WORD
    MASK = -1
    MASK_MAX = (1 << ((1 << BITS_PER_WORD) - 1)) - 1
    MASK_MIN = ~MASK_MAX
    
    MASK_SHIFT_LEFT = [MASK]
    for sh in range(1, WORD_SZ): MASK_SHIFT_LEFT.append(~(MASK_MAX >> (WORD_SZ - sh - 1)))
    
    MASK_SHIFT_RIGHT = [MASK]
    for sh in range(1, WORD_SZ): MASK_SHIFT_RIGHT.append(MASK_MAX >> (sh - 1))
    
    MASK_MOD = MASK_SHIFT_RIGHT[WORD_SZ - BITS_PER_WORD]
    
    def __init__(self, sz, lazy=True):
        '''create a bitset representing bit idx 0..sz-1'''
        self.sz = sz
        self.words = [0] * (self._get_word_idx(sz - 1) + 1)
        self.lazy = lazy  # whether to update first/last immediately
        if not lazy:
            self.first = sz  # lowest set bit
            self.last = -1   # highest set bit
    
    def _get_word_idx(self, bit_idx):
        '''given bit_idx, return idx of the word containing it'''
        if bit_idx >= self.sz: raise ValueError(f'out of bound index: {bit_idx}')
        return bit_idx >> self.BITS_PER_WORD
    
    def _mod(self, bit_idx):
        '''given bit_idx, return offset within the word containing it'''
        return bit_idx & self.MASK_MOD
    
    def _shift_one_left(self, shift):
        if shift == self.WORD_SZ - 1: return self.MASK_MIN
        return 1 << shift
    
    def __getitem__(self, bit_idx):
        '''return bitarray[bit_idx]'''
        word_idx = self._get_word_idx(bit_idx)
        return (self.words[word_idx] >> self._mod(bit_idx)) & 1
    
    def __setitem__(self, bit_idx, val):
        '''set bitarray[bit_idx] = val'''
        word_idx = self._get_word_idx(bit_idx)
        if val: self.words[word_idx] |= self._shift_one_left(self._mod(bit_idx))
        else: self.words[word_idx] &= ~self._shift_one_left(self._mod(bit_idx))
        if not self.lazy:
            if val:
                self.first = min(self.first, bit_idx)
                self.last = max(self.last, bit_idx)
            else:
                if bit_idx == self.first: self.first = self.next_set_bit(bit_idx + 1)
                if bit_idx == self.last: self.last = self.prev_set_bit(bit_idx - 1)
    
    def flip(self, bit_idx):
        '''set bitarray[bit_idx] ^= 1'''
        word_idx = self._get_word_idx(bit_idx)
        self.words[word_idx] ^= self._shift_one_left(self._mod(bit_idx))
        if not self.lazy:
            if (self.words[word_idx] >> self._mod(bit_idx)) & 1: 
                self.first = min(self.first, bit_idx)
                self.last = max(self.last, bit_idx)
            else:
                if bit_idx == self.first: self.first = self.next_set_bit(bit_idx + 1)
                if bit_idx == self.last: self.last = self.prev_set_bit(bit_idx - 1)
    
    def flip_range(self, l, r):
        '''set bitarray[l..r] ^= 1'''
        start_word_idx = self._get_word_idx(l)
        end_word_idx = self._get_word_idx(r)
        first_word_mask = self.MASK_SHIFT_LEFT[self._mod(l)]
        last_word_mask = self.MASK_SHIFT_RIGHT[self.WORD_SZ - 1 - self._mod(r)]
        if start_word_idx == end_word_idx:
            self.words[start_word_idx] ^= first_word_mask & last_word_mask
        else:
            self.words[start_word_idx] ^= first_word_mask
            for i in range(start_word_idx + 1, end_word_idx): self.words[i] ^= self.MASK
            self.words[end_word_idx] ^= last_word_mask
        
        if not self.lazy:
            if (self.words[start_word_idx] >> self._mod(l)) & 1: self.first = min(self.first, l)
            elif l == self.first: self.first = self.next_set_bit(l + 1)
            if (self.words[end_word_idx] >> self._mod(r)) & 1: self.last = max(self.last, r)
            elif r == self.last: self.last = self.prev_set_bit(r - 1)
    
    def next_set_bit(self, from_idx):
        '''return min i >= idx s.t. bitarray[i] == 1, or sz if no such bit'''
        if from_idx >= self.sz: return self.sz
        word_idx = self._get_word_idx(from_idx)
        word = self.words[word_idx] & self.MASK_SHIFT_LEFT[self._mod(from_idx)]
        while True:
            if word != 0: return word_idx * self.WORD_SZ + (word & -word).bit_length() - 1
            word_idx += 1
            if word_idx > len(self.words) - 1: return self.sz
            word = self.words[word_idx]
    
    def next_clear_bit(self, from_idx):
        '''return min i >= idx s.t. bitarray[i] == 0, or sz if no such bit'''
        if from_idx >= self.sz: return self.sz
        word_idx = self._get_word_idx(from_idx)
        word = ~self.words[word_idx] & self.MASK_SHIFT_LEFT[self._mod(from_idx)]
        while True:
            if word: return word_idx * self.WORD_SZ + (word & -word).bit_length() - 1
            word_idx += 1
            if word_idx > len(self.words) - 1: return self.sz
            word = ~self.words[word_idx]
    
    def prev_set_bit(self, from_idx):
        '''return max i <= idx s.t. bitarray[i] == 1, or -1 if no such bit'''
        if from_idx < 0: return -1
        word_idx = self._get_word_idx(from_idx)
        word = self.words[word_idx] & self.MASK_SHIFT_RIGHT[self.WORD_SZ - 1 - self._mod(from_idx)]
        while True:
            if word: return word_idx * self.WORD_SZ - 1 + (word.bit_length() if word > 0 else self.WORD_SZ)
            word_idx -= 1
            if word_idx < 0: return -1
            word = self.words[word_idx]
    
    def prev_clear_bit(self, from_idx):
        '''return max i <= idx s.t. bitarray[i] == 0, or -1 if no such bit'''
        if from_idx < 0: return -1
        word_idx = self._get_word_idx(from_idx)
        word = ~self.words[word_idx] & self.MASK_SHIFT_RIGHT[self.WORD_SZ - 1 - self._mod(from_idx)]
        while True:
            if word: return word_idx * self.WORD_SZ - 1 + (word.bit_length() if word > 0 else self.WORD_SZ)
            word_idx -= 1
            if word_idx < 0: return -1
            word = ~self.words[word_idx]

    def get_msb(self):
        '''return most significant set bit, or -1 if not exist'''
        if not self.lazy: return self.last
        return self.prev_set_bit(self.sz - 1)
    
    def get_lsb(self):
        '''return least significant set bit, or sz if not exist'''
        if not self.lazy: return self.first
        return self.next_set_bit(0)
    
    def _bitarray(self):
        res, st = [], 0
        while True:
            i = self.next_set_bit(st)
            if i != self.sz:
                res += [0] * (i - st)
                j = self.next_clear_bit(i)
                if j != self.sz:
                    res += [1] * (j-i)
                    st = j
                else:
                    res += [1] * (self.sz - i)
                    break
            else:
                res += [0] * (self.sz - st)
                break
        return res
    
    def __repr__(self) -> str:
        return ''.join(map(str, self._bitarray()))
    
    def __len__(self):
        return self.sz


# https://codeforces.com/contest/1705/submission/167118394
def solve(N, Q, A, queries):
    ba = BitArray(2 * 10**5 + 60, lazy=False)  # marginally faster than lazy=True
    
    def add(i): ba.flip_range(i, ba.next_clear_bit(i))
    def subtract(i): ba.flip_range(i, ba.next_set_bit(i))
 
    for a in A: add(a)
 
    res = []
    for k, l in queries:
        k -= 1
        subtract(A[k])
        A[k] = l
        add(A[k])
        res.append(ba.get_msb())
    
    return res

def main():
    N, Q = list(map(int, input().split()))
    A = list(map(int, input().split()))
    queries = [list(map(int, input().split())) for _ in range(Q)]
    out = solve(N, Q, A, queries)
    print(*out, sep='\n')


if __name__ == '__main__':
    main()


