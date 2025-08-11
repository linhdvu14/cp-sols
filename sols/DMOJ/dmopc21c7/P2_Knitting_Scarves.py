''' DMOPC '21 Contest 7 P2 - Knitting Scarves
https://dmoj.ca/problem/dmopc21c7p2
'''

import sys
input = sys.stdin.readline

INF = float('inf')

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self, N):
        self.head = Node()
        self.tail = Node()
        self.lookup = [None] * (N + 1)
        self.lookup[0] = self.head
        cur = self.head
        for v in range(1, N+1):
            node = Node(v)
            self.lookup[v] = node
            cur.next = node
            node.prev = cur
            cur = cur.next
        cur.next = self.tail
        self.tail.prev = cur

    def move(self, l, r, k):
        nl = self.lookup[l]
        nr = self.lookup[r]
        nk = self.lookup[k]
        nl.prev.next = nr.next
        nr.next.prev = nl.prev
        tmp = nk.next
        nk.next = nl
        nl.prev = nk
        nr.next = tmp
        tmp.prev = nr


def main():
    N, Q = list(map(int, input().split()))
    ll = LinkedList(N)
    for _ in range(Q):
        l, r, k = map(int, input().split())
        ll.move(l, r, k)
    
    cur = ll.head.next
    while cur != ll.tail:
        print(cur.value, end=' ')
        cur = cur.next
    print()


if __name__ == '__main__':
    main()
