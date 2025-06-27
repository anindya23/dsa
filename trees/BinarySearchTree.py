from collections import deque

class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class Solutions:
    def add_child(self, data, root):
        if data < root.data:
            if root.left:
                self.add_child(data, root.left)
            else:
                root.left = TreeNode(data)
        else:
            if root.right:
                self.add_child(data, root.right)
            else:
                root.right = TreeNode(data)

    def build_tree(self, elements):
        root = TreeNode(elements[0])
        for i in range(1, len(elements)):
            self.add_child(elements[i], root)
        return root

    def in_order_traversal(self, node):
        elements = []

        if node.left:
            elements += self.in_order_traversal(node.left)

        elements.append(node.data)

        if node.right:
            elements += self.in_order_traversal(node.right)

        return elements

    def pre_order_traversal(self, node):
        elements = []

        elements.append(node.data)

        if node.left:
            elements += self.pre_order_traversal(node.left)

        if node.right:
            elements += self.pre_order_traversal(node.right)

        return elements

    def post_order_traversal(self, node):
        elements = []

        if node.left:
            elements += self.post_order_traversal(node.left)

        if node.right:
            elements += self.post_order_traversal(node.right)

        elements.append(node.data)

        return elements

    def search(self, data):
        if data == self.data:
            return True

        if data < self.data:
            if self.left:
                return self.left.search(data)
            else:
                return False

        if data > self.data:
            if self.right:
                return self.right.search(data)
            else:
                return False

    def calculate_sum(self):
        sum = 0
        if self.left:
            sum += self.left.calculate_sum()

        if self.right:
            sum += self.right.calculate_sum()

        sum += self.data

        return sum

    def get_min(self):
        if self.left:
            return self.left.get_min()
        else:
            return self.data

    def invert_binary_tree(self):
        if self is None:
            return

        tmp = self.left
        self.left = self.right
        self.right = tmp

        if self.left:
            self.left.invert_binary_tree()
        if self.right:
            self.right.invert_binary_tree()

    def max_depth_recursive(self, node):
        if node is None:
            return 0

        return 1 + max(node.max_depth_recursive(node.left), node.max_depth_recursive(node.right))

    def max_depth_bfs(self, node) -> int:
        if node is None:
            return 0

        level = 0
        queue = deque([node])
        while queue:

            for i in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            level += 1

        return level


    def lowestCommonAncestor(self, root: 'TreeNode', p: int, q: int) -> 'TreeNode':
        if not root or root.data == p or root.data == q:
            return root

        i = root.lowestCommonAncestor(root.left, p, q)
        j = root.lowestCommonAncestor(root.right, p, q)

        if (i and j) or root.data in [p, q]:
            return root
        else:
            return i or j

        # if not root or root == p or root == q:
        #     return root
        #
        # x = self.lowestCommonAncestor(root.left, p, q)
        # y = self.lowestCommonAncestor(root.right, p, q)
        #
        # if (x and y) or root in [p, q]:
        #     return root
        # else:
        #     return x or y

        """
        Function lowestCommonAncestor(root, p, q)
        """

    def findingMissing(arr, size):
        # Extreme cases
        # if (arr[0] != 1):
        #     return 1
        # if (arr[size - 1] != (size + 1)):
        #     return size + 1

        a = 0
        b = size - 1
        mid = 0
        while b > a + 1:
            mid = (a + b) // 2
            if (arr[a] - a) != (arr[mid] - mid):
                b = mid
            elif (arr[b] - b) != (arr[mid] - mid):
                a = mid
        return arr[a] + 1

if __name__ == "__main__":
    elements = [17, 4, 1, 20, 9, 23, 18, 34]
    obj = Solutions()
    root = obj.build_tree(elements)
    print(obj.in_order_traversal(root))
    print(obj.pre_order_traversal(root))
    print(obj.post_order_traversal(root))
    # print(root.search(10))
    # print(root.calculate_sum())
    # print(root.get_min())
    # print(root.invert_binary_tree())
    # root.print_tree()
    # print(root.max_depth_recursive(root))
    # print(root.max_depth_bfs(root))
    # print(root.lowestCommonAncestor(root, ))
    # root = BinarySearchTree(17)
    # root.left = BinarySearchTree(4)
    # root.right = BinarySearchTree(20)
    # root.left.left = BinarySearchTree(1)
    # root.left.right = BinarySearchTree(9)
    # root.right.left = BinarySearchTree(18)
    # root.right.right = BinarySearchTree(23)
    # root.right.right.right = BinarySearchTree(34)
    # print(root.lowestCommonAncestor(root, root.right.left.data, root.left.right.data).data)