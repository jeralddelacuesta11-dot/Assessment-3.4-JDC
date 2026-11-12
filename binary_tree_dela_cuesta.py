from collections import deque


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def bfs(root):
    if root is None:
        return []

    result = []
    queue = deque([root])

    while queue:
        current = queue.popleft()
        result.append(current.data)

        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

    return result


def dfs_preorder(root):
    if root is None:
        return []

    return (
        [root.data]
        + dfs_preorder(root.left)
        + dfs_preorder(root.right)
    )


# Binary tree made from DELA CUESTA (space excluded)
root = Node("D")

root.left = Node("E")
root.right = Node("L")

root.left.left = Node("A")
root.left.right = Node("C")

root.right.left = Node("U")
root.right.right = Node("E")

root.left.left.left = Node("S")
root.left.left.right = Node("T")

root.left.right.left = Node("A")


print("BINARY TREE - DELA CUESTA")
print("BFS:", " - ".join(bfs(root)))
print("DFS (Preorder):", " - ".join(dfs_preorder(root)))
