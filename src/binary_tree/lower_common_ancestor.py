def lower_common_ancestor(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    # TC: O(n), SC: O(n)

    if p.val > root.val and q.val > root.val:
        return lower_common_ancestor(root.right, p, q)

    if p.val < root.val and q.val < root.val:
        return lower_common_ancestor(root.left, p, q)

    return root
