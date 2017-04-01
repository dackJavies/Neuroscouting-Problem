# Tree problem solution by Jack Davis for Neuroscouting interview


class Node:

    def __init__(self, value, depth, lft_nbor, rgt_nbor):
        self.value = value
        self.depth = depth
        self.lft_nbor = lft_nbor
        self.rgt_nbor = rgt_nbor
        self.left = None
        self.right = None
        if depth < Node.max_depth:
            self.left = self.create_new_left()
            self.right = self.create_new_right()

    def create_new_left(self):
        left_val = self.value
        left_depth = self.depth + 1
        left_lft_nbor = None
        left_rgt_nbor = self.right
        if self.lft_nbor is not None:
            left_val += self.lft_nbor.value
            left_lft_nbor = self.lft_nbor.right
        return Node(left_val, left_depth, left_lft_nbor, left_rgt_nbor)

    def create_new_right(self):
        right_val = self.value
        right_depth = self.depth + 1
        right_lft_nbor = self.left
        right_rgt_nbor = None
        if self.rgt_nbor is not None:
            right_val += self.rgt_nbor.value
            right_rgt_nbor = self.rgt_nbor.left
        return Node(right_val, right_depth, right_lft_nbor, right_rgt_nbor)


def main():
    desired_depth_str = input("How deep should this tree be? ")
    desired_depth_int = int(desired_depth_str)
    if not valid_input(desired_depth_int):
        print "Invalid input: " + desired_depth_str + ". Input cannot be negative or zero."
        return
    Node.max_depth = desired_depth_int

    print "Generating tree..."
    root = Node(1, 1, None, None)

    if not valid_tree(root):
        print "Looks like this tree isn't correct"

    print "Let's take a look at your tree."
    display_tree(root)


def valid_input(desired_depth):
    return desired_depth >= 1


def valid_tree(root):
    return True


def display_tree(root):
    print ""


def test_tree_building():
    Node.max_depth = 1
    root1 = Node(1, 1, None, None)
    print "root1's value: " + str(root1.value)
    print "is root1's left none? " + str(root1.left is None)
    print "is root1's right none? " + str(root1.right is None)

    Node.max_depth = 2
    root2 = Node(1, 1, None, None)
    print "root2's value: " + str(root2.value)
    print "root2's left's value: " + str(root2.left.value)
    print "root2's right's value: " + str(root2.right.value)

    Node.max_depth = 3
    root3 = Node(1, 1, None, None)
    print "root3's value: " + str(root3.value)
    print "root3's left val: " + str(root3.left.value)
    print "root3's right val: " + str(root3.right.value)
    print "root3's left's left val: " + str(root3.left.left.value)
    print "root3's left's right val: " + str(root3.left.right.value)
    print "root3's right's left val: " + str(root3.right.left.value)
    print "root3's right's right val: " + str(root3.right.right.value)


test_tree_building()






