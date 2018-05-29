res = []
def inorder_traversal(node):
    if node is not None:
        if node.left is not None:
            inorder_traversal(node.left)
        res.append(node.data)
        if node.right is not None:
            inorder_traversal(node.right)


def checkBST(root):
    inorder_traversal(root)
    if res == sorted(res) and res == list(set(res)):
        return True
    else:
        return False
