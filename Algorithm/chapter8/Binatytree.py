class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Binatytree:
    def __init__(self, value):
        self.root = Node(value)

    # ---------- Insert ----------
    def insert(self, value):
        self.root = self._insert(self.root, value)

    def _insert(self, node, value):
        if node is None:
            return Node(value)
        if value < node.value:
            node.left = self._insert(node.left, value)
        else:
            node.right = self._insert(node.right, value)
        return node

    # ---------- Search ----------
    def search(self, value):
        return self._search(self.root, value)

    def _search(self, node, value):
        if node is None:
            return False
        if value == node.value:
            return True
        if value < node.value:
            return self._search(node.left, value)
        return self._search(node.right, value)

    # ---------- Delete ----------
    def delete(self, value):
        self.root, deleted = self._delete(self.root, value)
        return deleted

    def _delete(self, node, value):
        if node is None:
            return node, False

        if value < node.value:
            node.left, deleted = self._delete(node.left, value)
            return node, deleted
        elif value > node.value:
            node.right, deleted = self._delete(node.right, value)
            return node, deleted
        else:
            # node.value == value : 실제 삭제
            if node.left is None:
                return node.right, True
            if node.right is None:
                return node.left, True
            # 두 자식: 오른쪽 서브트리의 최소값으로 대체
            successor = self.get_min(node.right)
            node.value = successor.value
            node.right, _ = self._delete(node.right, successor.value)
            return node, True

    # ---------- Successor / Min ----------
    def get_min(self, node):
        current = node
        while current and current.left:
            current = current.left
        return current

    def successor(self, node):
        # 1) 오른쪽 서브트리 있으면 그쪽 최소
        if node.right:
            return self.get_min(node.right)
        # 2) 없으면 root에서 내려가며 가장 최근의 왼쪽-조상 추적
        current = self.root
        succ = None
        while current:
            if node.value < current.value:
                succ = current
                current = current.left
            elif node.value > current.value:
                current = current.right
            else:
                break
        return succ

    # ---------- Traversals ----------
    def inorder_traversal(self):
        res = []
        self._inorder(self.root, res)
        return res

    def _inorder(self, node, res):
        if not node:
            return
        self._inorder(node.left, res)
        res.append(node.value)
        self._inorder(node.right, res)

    def preorder_traversal(self):
        res = []
        self._preorder(self.root, res)
        return res

    def _preorder(self, node, res):
        if not node:
            return
        res.append(node.value)
        self._preorder(node.left, res)
        self._preorder(node.right, res)

    def postorder_traversal(self):
        res = []
        self._postorder(self.root, res)
        return res

    def _postorder(self, node, res):
        if not node:
            return
        self._postorder(node.left, res)
        self._postorder(node.right, res)
        res.append(node.value)


def main():
    btree = Binatytree(10)
    for v in [5, 15, 3, 7, 12, 18]:
        btree.insert(v)

    print("Inorder Traversal:", btree.inorder_traversal())
    print("Preorder Traversal:", btree.preorder_traversal())
    print("Postorder Traversal:", btree.postorder_traversal())

    print("Search 7:", btree.search(7))
    print("Search 20:", btree.search(20))

    node = btree.root.left  # 5
    succ = btree.successor(node)
    print("Successor of 5:", succ.value if succ else None)

    print("Delete 3:", btree.delete(3))
    print("Inorder Traversal after deleting 3:", btree.inorder_traversal())
    print("Delete 10:", btree.delete(10))
    print("Inorder Traversal after deleting 10:", btree.inorder_traversal())
    print("Delete 20 (not present):", btree.delete(20))
    print("Inorder Traversal after trying to delete 20:", btree.inorder_traversal())

if __name__ == "__main__":
    main()