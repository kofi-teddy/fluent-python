class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def kth_largest_level_sum(root: TreeNode, k: int) -> int:
    if not root:
        return -1

    # initialize the queue with the root node
    queue = [root]
    level_sums = []

    while queue:
        level_size = len(queue)
        level_sum = 0

        # process all nodes at the current level
        for _ in range(level_size):
            node = queue.pop(0)

            # sum up the values at the current level
            level_sum += node.val

            # Enqueue the children nodes
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        # store the sum for the current level
        level_sums.append(level_sum)

    if len(level_sums) < k:
        return -1

    # sort the level sums in descending order
    level_sums.sort(reverse=True)

    # return the kth largest sum
    return level_sum[k-1]