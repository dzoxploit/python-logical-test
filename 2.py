class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def diameter_of_binary_tree(root):
    if root is None:
        return 0

    # Calculate the height of the left and right subtrees
    left_height = height_of_binary_tree(root.left)
    right_height = height_of_binary_tree(root.right)

    # Calculate the diameter of the left and right subtrees recursively
    left_diameter = diameter_of_binary_tree(root.left)
    right_diameter = diameter_of_binary_tree(root.right)

    # Return the maximum of the following:
    # 1. Diameter of the left subtree
    # 2. Diameter of the right subtree
    # 3. Longest path between leaves that goes through the root
    return max(left_height + right_height + 1, max(left_diameter, right_diameter))


def height_of_binary_tree(root):
    if root is None:
        return 0

    # Calculate the height of the tree recursively
    left_height = height_of_binary_tree(root.left)
    right_height = height_of_binary_tree(root.right)

    # Return the maximum height between the left and right subtrees, plus 1 for the root
    return max(left_height, right_height) + 1


# Create the binary tree based on the given input
root = TreeNode(40)
root.left = TreeNode(30)
root.right = TreeNode(65)
root.left.left = TreeNode(22)
root.left.right = TreeNode(38)
root.right.right = TreeNode(70)

# Calculate the diameter of the binary tree
diameter = diameter_of_binary_tree(root)

print("The diameter of the tree is:", diameter)
