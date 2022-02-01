import queue


class Node:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if not self.root:
            self.root = Node(val)
        else:
            self.insertion_node(self.root, val)

    def insertion_node(self, current, val):
        if not current:
            current = Node(val)
        elif current.val > val:
            current.left = self.insertion_node(current.left, val)
        else:
            current.right = self.insertion_node(current.right, val)

        return current

    def print(self, traversal):
        if traversal == 'in':
            self.inorder(self.root)
        if traversal == 'pre':
            self.preorder(self.root)
        if traversal == "pos":
            self.postorder(self.root)
        print('\n')

    def inorder(self, root):
        if not root:
            return
        else:
            self.inorder(root.left)
            print(root.val)
            self.inorder(root.right)

    def preorder(self, root):
        if not root:
            return
        else:
            print(root.val)
            self.preorder(root.left)
            self.preorder(root.right)

    def postorder(self, root):
        if not root:
            return
        else:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.val)

    def visible_nodes(self):
        root = self.root
        # Write your code here
        from collections import deque

        queue = deque()
        queue.append([0, root])
        result = {}
        while len(queue) > 0:
            current_level, current_node = queue.popleft()
            if current_level not in result.keys():
                result[current_level] = current_node
            else:
                pass
            if current_node.left:
                queue.append([current_level + 1, current_node.left])

            if current_node.right:
                queue.append([current_level + 1, current_node.right])

        return len(result)

    def bfs(self):
        root = self.root

        from collections import deque

        queue = deque()
        queue.append(root)

        while queue:
            node = queue.popleft()

            print(node.val, end=" ")

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

r = BST()
r.insert(30)
r.insert(20)
r.insert(40)
r.insert(10)
r.insert(15)
r.insert(80)

r.print('in')
r.print('pre')
r.print('pos')

print(r.visible_nodes())
r.bfs()

