#MEDIUM
# 1339


'''     https://leetcode.com/problems/maximum-product-of-splitted-binary-tree/description/      '''


# Given the root of a binary tree, split the binary tree into two subtrees by removing one edge such that the product of the sums of the subtrees is maximized.
# Return the maximum product of the sums of the two subtrees. Since the answer may be too large, return it modulo 109 + 7.
# Note that you need to maximize the answer before taking the mod and not after taking it.

# Example 1:
# Input: root = [1,2,3,4,5,6]
# Output: 110
# -------------------------------------------------------------------------------
# Explanation: Remove the red edge and get 2 binary trees with sum 11 and 10. Their product is 110 (11*10)

# Example 2:
# Input: root = [1,null,2,3,4,null,null,5,6]
# Output: 90
# ---------------------------------------------------------------------------------
# Explanation: Remove the red edge and get 2 binary trees with sum 15 and 6.Their product is 90 (15*6)



def maxProduct(root):
    def count(node) -> int:
        if not node: 
            return 0, 0
        left_so_far, left = count(node.left)
        right_so_far, right = count(node.right)
        current = node.val + left + right
        max_so_far = max(left_so_far, right_so_far, (total - current) * current)
        return max_so_far, current

    total = 0
    _, total = count(root)
    return count(root)[0] % (10 ** 9 + 7)

print(maxProduct([1,2,3,4,5,6]))