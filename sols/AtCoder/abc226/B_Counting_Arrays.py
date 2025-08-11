''' B - Counting Arrays
https://atcoder.jp/contests/abc226/tasks/abc226_b
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write


from types import GeneratorType
def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to
    return wrappedfunc


class TrieNode:
    def __init__(self):
        self.links = {}
        self.is_end = False  # is this char marking end of a word

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        for char in word:
            if char not in curr.links:
                curr.links[char] = TrieNode()
            curr = curr.links[char]
        curr.is_end = True  # mark end of word

    def count_leaf(self):
        res = 0
        @bootstrap
        def tour(u):
            nonlocal res
            if u.is_end:
                res += 1
            for v in u.links.values():
                yield tour(v)
            yield None
        tour(self.root)
        return res


def main():
    N = int(input())
    trie = Trie()
    for _ in range(N):
        nums = list(map(int, input().split()))
        trie.insert(nums[1:])
    out = trie.count_leaf()
    print(out)


if __name__ == '__main__':
    main()

