class Node:
    def __init__(self):
        self.count = 1  # count of subtree nodes incl itself
        self.left = None  # 0
        self.right = None # 1

    def add_child(self, v):
        if v == 0:
            if not self.left: self.left = Node()
            self.count += 1
            return self.left
        if v == 1:
            if not self.right: self.right = Node()
            self.count += 1
            return self.right

    def del_child(self, v):
        if v == 0:
            if self.left and self.left.count > 0: self.count -= 1
            return self.left
        if v == 1:
            if self.right and self.right.count > 0: self.count -= 1
            return self.right

    def del_self(self):
        self.count -= 1


class Tree:
    def __init__(self):
        self.root = Node()

    def _add(self, curr, digit):
        return curr.add_child(digit)

    def add_x(self, x):
        # print('***** adding {}, bin={}, before {} nodes'.format(x, bin(x)[2:].zfill(4), self.root.count))
        curr = self.root
        for i in range(31,-1,-1):
            digit = (x & (1 << i)) >> i
            # print('i={}, digit={}, before curr.count={}'.format(i,digit,curr.count))
            curr = self._add(curr, digit)
            # print('-> go {}, after curr.count={}'.format('left' if digit==0 else 'right',curr.count))

    def _del(self, curr, digit):
        return curr.del_child(digit)

    def del_x(self, x):
        # print('***** deleting {}, bin={}, before {} nodes'.format(x, bin(x)[2:].zfill(4), self.root.count))
        curr = self.root
        for i in range(31,-1,-1):
            digit = (x & (1 << i)) >> i
            # print('i={}, digit={}, before curr.count={}'.format(i,digit,curr.count))
            curr = self._del(curr, digit)
            # print('-> go {}, after curr.count={}'.format('left' if digit==0 else 'right',curr.count))
        curr.del_self()

    def check_x(self, x):
        # print('***** checking {}, bin={}'.format(x, bin(x)[2:].zfill(4)))
        curr = self.root
        buff = 0
        for i in range(31,-1,-1):
            digit = (x & (1 << i)) >> i
            if digit == 0:
                if curr.right and curr.right.count > 0:
                    buff += (1 << i)
                    curr = curr.right
                    # print('i={}, digit={}, go right, buff={}'.format(i,digit,bin(buff)[2:].zfill(4)))
                elif curr.left and curr.left.count > 0:
                    curr = curr.left
                    # print('i={}, digit={}, go left, buff={}'.format(i,digit,bin(buff)[2:].zfill(4)))
                else:
                    # print('i={}, digit={}, short-circuit, buff={}'.format(i,digit,bin(buff)[2:].zfill(4)))
                    return buff
            else:
                if curr.left and curr.left.count > 0:
                    buff += (1 << i)
                    curr = curr.left
                    # print('i={}, digit={}, go left, buff={}'.format(i,digit,bin(buff)[2:].zfill(4)))
                elif curr.right and curr.right.count > 0:
                    curr = curr.right
                    # print('i={}, digit={}, go right, buff={}'.format(i,digit,bin(buff)[2:].zfill(4)))
                else:
                    # print('i={}, digit={}, short-circuit, buff={}'.format(i,digit,bin(buff)[2:].zfill(4)))
                    return buff
        return buff              


def main():
    from sys import stdin

    tree = Tree()
    q = int(stdin.readline().strip())
    for _ in range(q):
        ts = stdin.readline().strip().split(' ')
        op, x = ts[0], int(ts[1])
        if op == '+':
            tree.add_x(x)
        elif op == '-':
            tree.del_x(x)
        else:
            print(tree.check_x(x))

 
if __name__ == '__main__':
    main()