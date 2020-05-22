class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def target_sum_bst(root, target):
    _queue, _sum = list(), list()
    _queue.append(root)
    _sum.append(root.value)

    while len(_queue):
        curr = _queue[0]
        if curr:
            s = _sum[0]

            if not curr.left and not curr.right:
                if s==target:
                    return True

            if curr.left:
                _queue.append(curr.left)
                _sum.append(s + curr.left.value)

            if curr.right:
                _queue.append(curr.right)
                _sum.append(s + curr.right.value)

            _queue.__delitem__(0)
            _sum.__delitem__(0)

    return False

if __name__ == "__main__":
    n6 = Node(6)
    n4 = Node(4)
    n3 = Node(3, None, n4)
    n2 = Node(2, None, n6)
    n1 = Node(1, n2, n3)

    print(target_sum_bst(n1, 9))