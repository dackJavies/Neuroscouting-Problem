# Tree problem solution by Jack Davis for Neuroscouting interview


class Node:

    def __init__(self, position, value, depth):
        self.position = position
        self.value = value
        self.depth = depth
        self.lft_nbor = None
        self.rgt_nbor = None
        self.left = None
        self.right = None
        if self.depth == 1 and Node.max_depth > 1:
            self.create_tree([self])

    def create_tree(self, queue):
        if len(queue) > 0:
            n = queue[0]
            queue.remove(n)
            n.create_children()
            n.set_neighbors()
            if n.depth + 1 < Node.max_depth:
                queue.append(n.left)
                queue.append(n.right)
            self.create_tree(queue)

    def create_children(self):
        left_pos = self.position + "L"
        right_pos = self.position + "R"

        left_val = right_val = self.value

        left_depth = right_depth = self.depth + 1

        self.left = Node(left_pos, left_val, left_depth)
        self.right = Node(right_pos, right_val, right_depth)

    def set_neighbors(self):
        self.set_left_nbors()
        self.set_right_nbors()

    def set_left_nbors(self):
        self.left.rgt_nbor = self.right
        if self.lft_nbor is not None:
            if self.lft_nbor.right is not None:
                self.lft_nbor.right.rgt_nbor = self.left
            self.left.lft_nbor = self.lft_nbor.right
            self.left.value += self.lft_nbor.value

    def set_right_nbors(self):
        self.right.lft_nbor = self.left
        if self.rgt_nbor is not None:
            if self.rgt_nbor.left is not None:
                self.rgt_nbor.left.lft_nbor = self.right
            self.right.rgt_nbor = self.rgt_nbor.left
            self.right.value += self.rgt_nbor.value


def main():
    desired_depth_str = input("How deep should this tree be? ")
    desired_depth_int = int(desired_depth_str)
    if not valid_input(desired_depth_int):
        print "Invalid input: " + desired_depth_str + ". Input cannot be negative or zero."
        return
    Node.max_depth = desired_depth_int

    print "Generating tree..."
    root = Node("", 1, 1)

    if not valid_tree(root):
        print "Looks like this tree isn't correct."
    else:
        print "Great! The tree seems to be valid."

    print "Let's take a look at your tree."
    display_tree(root)


def valid_input(desired_depth):
    return desired_depth >= 1


def valid_tree(root):
    if root.left is None and root.right is None:
        if root.depth == 1:
            return root.value == 1
        return True
    else:
        left_valid = right_valid = False

        if root.lft_nbor is None:
            left_valid = root.left.value == root.value
        else:
            left_valid = root.left.value == root.value + root.lft_nbor.value

        if root.rgt_nbor is None:
            right_valid = root.right.value == root.value
        else:
            right_valid = root.right.value == root.value + root.rgt_nbor.value

        return left_valid and right_valid and valid_tree(root.left) and valid_tree(root.right)


def display_tree(root):
    print "Position: " + root.position + ", Value: " + str(root.value)
    if root.left is not None and root.right is not None:
        display_tree(root.left)
        display_tree(root.right)


def test_tree_building():
    Node.max_depth = 1
    print "~~~ depth 1 ~~~"
    root1 = Node("", 1, 1)
    display_tree(root1)

    Node.max_depth = 2
    print "~~~ depth 2 ~~~"
    root2 = Node("", 1, 1)
    display_tree(root2)

    Node.max_depth = 3
    print "~~~ depth 3 ~~~"
    root3 = Node("", 1, 1)
    display_tree(root3)

    Node.max_depth = 4
    print "~~~ depth 4 ~~~"
    root4 = Node("", 1, 1)
    display_tree(root4)

    Node.max_depth = 5
    print "~~~ depth 5 ~~~"
    root5 = Node("", 1, 1)
    display_tree(root5)


def test_tree_validity():
    Node.max_depth = 1
    print "~~~ depth 1 ~~~"
    root1 = Node("", 1, 1)
    display_tree(root1)
    print "Valid? " + str(valid_tree(root1))
    print "Changing root val to 45"
    root1.value = 45
    display_tree(root1)
    print "Valid? " + str(valid_tree(root1))

    Node.max_depth = 2
    print "~~~ depth 2 ~~~"
    root2 = Node("", 1, 1)
    display_tree(root2)
    print "Valid? " + str(valid_tree(root2))
    print "Changing R val to 8"
    root2.right.value = 8
    display_tree(root2)
    print "Valid? " + str(valid_tree(root2))

    Node.max_depth = 3
    print "~~~ depth 3 ~~~"
    root3 = Node("", 1, 1)
    display_tree(root3)
    print "Valid? " + str(valid_tree(root3))
    print "Changing RL val to 34"
    root3.right.left.value = 34
    display_tree(root3)
    print "Valid? " + str(valid_tree(root3))

    Node.max_depth = 4
    print "~~~ depth 4 ~~~"
    root4 = Node("", 1, 1)
    display_tree(root4)
    print "Valid? " + str(valid_tree(root4))
    print "Changing LRL val to 99"
    root4.left.right.left.value = 99
    display_tree(root4)
    print "Valid? " + str(valid_tree(root4))

    Node.max_depth = 5
    print "~~~ depth 5 ~~~"
    root5 = Node("", 1, 1)
    display_tree(root5)
    print "Valid? " + str(valid_tree(root5))
    print "Changing RRLL val to 535"
    root5.right.right.left.left.value = 535
    display_tree(root5)
    print "Valid? " + str(valid_tree(root5))

# test_tree_building()
# test_tree_validity()
main()
