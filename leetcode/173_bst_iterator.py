# https://leetcode.com/problems/binary-search-tree-iterator/

class Node:
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None


class BSTIterator:
    def __init__(self, root: Node) -> None:
        self.root = root
        self.parents = []

        if root:
            while root.left:
                self.parents.append(root)
                root = root.left
        self.node = root

    def next(self) -> int:
        nxt = self.node
        if self.node.right:
            self.node = self.node.right
            while self.node.left:
                self.parents.append(self.node)
                self.node = self.node.left
        else:
            self.node = self.parents.pop() if self.parents else None

        return nxt.value

    def hasNext(self) -> bool:
        return bool(self.node)