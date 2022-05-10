#Given a binary search tree, convert it into a sorted doubly-linked list by modifying the original tree nodes (do not create new nodes).

def search_tree_to_double_linked_list(root):
    if not root:
        return
    def depth_first_search(node):
        nonlocal head, tail
        if not node:
            return
        depth_first_search(node.left)
        if tail:
            tail.right = node
            node.left = tail
        else:
            head = node
        tail = node
        depth_first_search(node.right)
    head, tail = None, None
    depth_first_search(root)
    head.left = tail
    tail.right = head
    
    return head