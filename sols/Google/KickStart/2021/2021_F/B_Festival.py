''' Festival
https://codingcompetitions.withgoogle.com/kickstart/round/0000000000435bae/0000000000887dba
'''

# TLE python, AC pypy

class AVLNode(object): 
    def __init__(self, val): 
        self.val = val 
        self.count = 1  # num nodes under this subtree
        self.sum = val  # sum nodes under this subtree
        self.height = 1
        self.left = None
        self.right = None  


class AVLTree(object): 
    def __init__(self):
        self.root = None

    def insert(self, val):
        def _insert(root, val): 
            if not root: return AVLNode(val) 
            root.count += 1
            root.sum += val
            if val < root.val: 
                root.left = _insert(root.left, val) 
            else: 
                root.right = _insert(root.right, val) 
    
            # update height
            root.height = 1 + max(self.get_height(root.left), self.get_height(root.right)) 
    
            # rebalance
            balance = self.get_balance(root) 
            if balance > 1 and val < root.left.val:    # left left
                return self.rotate_right(root)
            if balance < -1 and val >= root.right.val:  # right right
                return self.rotate_left(root)
            if balance > 1 and val >= root.left.val:    # left right
                root.left = self.rotate_left(root.left)
                return self.rotate_right(root) 
            if balance < -1 and val < root.right.val:  # right left
                root.right = self.rotate_right(root.right) 
                return self.rotate_left(root) 
            return root 
        
        self.root = _insert(self.root, val)

    def delete(self, val):
        def get_min_node(root): 
            if not root or not root.left: return root 
            return get_min_node(root.left) 

        def _delete(root, val): 
            if not root: return root 
            root.count -= 1
            root.sum -= val
            if val < root.val: 
                root.left = _delete(root.left, val) 
            elif val > root.val: 
                root.right = _delete(root.right, val) 
            else: 
                if not root.left or not root.right: return root.left or root.right
                tmp = get_min_node(root.right) 
                root.val = tmp.val 
                root.right = _delete(root.right, tmp.val) 
    
            # update height 
            root.height = 1 + max(self.get_height(root.left), self.get_height(root.right)) 
    
            # rebalance
            balance = self.get_balance(root) 
            if balance > 1 and self.get_balance(root.left) >= 0:  # left left
                return self.rotate_right(root) 
            if balance < -1 and self.get_balance(root.right) <= 0:  # right right
                return self.rotate_left(root) 
            if balance > 1 and self.get_balance(root.left) < 0:  # left right
                root.left = self.rotate_left(root.left) 
                return self.rotate_right(root) 
            if balance < -1 and self.get_balance(root.right) > 0:  # right left
                root.right = self.rotate_right(root.right) 
                return self.rotate_left(root) 
            return root 
        
        self.root = _delete(self.root, val)

    def rotate_left(self, root):
        new_root = root.right
        tmp = new_root.left

        root.right = tmp
        root.count -= new_root.count
        root.sum -= new_root.sum
        if tmp: 
            root.count += tmp.count
            root.sum += tmp.sum

        new_root.left = root
        new_root.count += root.count
        new_root.sum += root.sum
        if tmp:
            new_root.count -= tmp.count
            new_root.sum -= tmp.sum

        root.height = 1 + max(self.get_height(root.left),self.get_height(root.right))
        new_root.height = 1 + max(self.get_height(new_root.left),self.get_height(new_root.right))
        return new_root

    def rotate_right(self, root):
        new_root = root.left
        tmp = new_root.right
        
        root.left = tmp
        root.count -= new_root.count
        root.sum -= new_root.sum
        if tmp:
            root.count += tmp.count
            root.sum += tmp.sum

        new_root.right = root
        new_root.count += root.count
        new_root.sum += root.sum
        if tmp:
            new_root.count -= tmp.count
            new_root.sum -= tmp.sum

        root.height = 1 + max(self.get_height(root.left),self.get_height(root.right))
        new_root.height = 1 + max(self.get_height(new_root.left),self.get_height(new_root.right))
        return new_root
  
    def get_height(self, root): 
        if not root: return 0
        return root.height 
  
    def get_balance(self, root): 
        if not root: return 0
        return self.get_height(root.left) - self.get_height(root.right) 

    def sum_top_k(self, k):  # sum of k highest values
        def _sum(node, k):
            if not node or k<=0: return 0
            if k==node.count: return node.sum
            count_right = node.right.count if node.right else 0
            count_left = node.left.count if node.left else 0
            k_right = min(count_right, k)
            k_own = 0 if k_right >= k else 1
            k_left = min(k-k_own-k_right, count_left)
            return _sum(node.left, k_left) + _sum(node.right, k_right) + node.val * k_own
        return _sum(self.root, k)

# TLE python, AC pypy
def solve_avl(D, N, K, attractions):
    intervals = []
    for h,s,e in attractions:
        intervals.append((s,h))
        intervals.append((e+1,-h))
    intervals.sort()

    bst = AVLTree()
    res = prev = 0
    for cur,h in intervals:
        if cur != prev and prev != 0:
            res = max(res, bst.sum_top_k(K))
        prev = cur
        if h > 0:
            bst.insert(h)
        else:
            bst.delete(-h)
    return res 



from random import randint

class TreapNode:
    def __init__(self, val, priority):
        self.val = val
        self.priority = priority
        self.count = 1  # num nodes under this subtree
        self.sum = val  # sum nodes under this subtree
        self.left = None
        self.right = None


class Treap:
    def __init__(self):
        self.root = None
    
    def _rand(self):
        return randint(1,2**16)
    
    def update(self, node):
        if not node: return
        node.count, node.sum = 1, node.val
        if node.left:
            node.count += node.left.count
            node.sum += node.left.sum
        if node.right:
            node.count += node.right.count
            node.sum += node.right.sum
    
    # split subtree rooted here into 2 treaps: one < val, one >= val
    def split(self, root, val):
        if not root: return (None, None)
        if root.val < val:
            x, y = self.split(root.right, val)
            root.right = x
            self.update(root)
            return (root, y)
        else:
            x, y = self.split(root.left, val)
            root.left = y
            self.update(root)
            return (x, root)

    # merge 2 treaps into new treap, assuming x vals <= y vals
    def merge(self, x, y):
        if not x or not y: return x or y
        if x.priority > y.priority:  # make x root
            x.right = self.merge(x.right, y)
            self.update(x)
            return x
        else:
            y.left = self.merge(x, y.left)
            self.update(y)
            return y

    # split current tree, then merge 2 trees with new node
    def insert(self, val):
        y = TreapNode(val, self._rand())
        x, z = self.split(self.root, val)
        self.root = self.merge(self.merge(x, y), z)
    
    # delete one node with val
    def delete(self, val):
        def _delete(node):
            if not node: return node
            if node.val < val:
                node.right = _delete(node.right)
            elif node.val > val:
                node.left = _delete(node.left)
            else:
                node = self.merge(node.left, node.right)
            self.update(node)
            return node
        self.root = _delete(self.root)

    # sum of k highest values
    def sum_top_k(self, k):  
        def _sum(node, k):
            if not node or k<=0: return 0
            if k==node.count: return node.sum
            count_right = node.right.count if node.right else 0
            count_left = node.left.count if node.left else 0
            k_right = min(count_right, k)
            k_own = 0 if k_right >= k else 1
            k_left = min(k-k_own-k_right, count_left)
            return _sum(node.left, k_left) + _sum(node.right, k_right) + node.val * k_own
        return _sum(self.root, k)


# TLE python, AC pypy
def solve_treap(D, N, K, attractions):
    intervals = []
    for h,s,e in attractions:
        intervals.append((s,h))
        intervals.append((e+1,-h))
    intervals.sort()

    bst = Treap()
    res = prev = 0
    for cur,h in intervals:
        if cur != prev and prev != 0:
            res = max(res, bst.sum_top_k(K))
        prev = cur
        if h > 0:
            bst.insert(h)
        else:
            bst.delete(-h)
    return res 

solve = solve_treap

def main():
    from sys import stdin
    
    T = int(stdin.readline().strip())

    for t in range(T):
        D, N, K = map(int, stdin.readline().strip().split())
        attractions = [tuple(map(int, stdin.readline().strip().split())) for _ in range(N)]
        out = solve(D, N, K, attractions)
        print('Case #{}: {}'.format(t+1, out))


if __name__ == '__main__':
    main()
