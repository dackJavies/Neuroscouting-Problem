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
            self.create_children([self])

    def create_children(self, queue):
        if len(queue) > 0:
            n = queue[0]
            queue.remove(n)

            left_pos = n.position + "L"
            right_pos = n.position + "R"

            left_val = right_val = 1

            left_depth = right_depth = n.depth + 1

            n.left = Node(left_pos, left_val, left_depth)
            n.right = Node(right_pos, right_val, right_depth)

            n.left.rgt_nbor = n.right
            n.right.lft_nbor = n.left

            if n.lft_nbor is not None:
                if n.lft_nbor.right is not None:
                    n.lft_nbor.right.rgt_nbor = n.left
                n.left.lft_nbor = n.lft_nbor.right

            if n.rgt_nbor is not None:
                if n.rgt_nbor.left is not None:
                    n.rgt_nbor.left.lft_nbor = n.right
                n.right.rgt_nbor = n.rgt_nbor.left

            if n.depth + 1 < Node.max_depth:
                queue.append(n.left)
                queue.append(n.right)

            self.create_children(queue)



def main():
    desired_depth_str = input("How deep should this tree be? ")
    desired_depth_int = int(desired_depth_str)
    if not valid_input(desired_depth_int):
        print "Invalid input: " + desired_depth_str + ". Input cannot be negative or zero."
        return
    Node.max_depth = desired_depth_int

    print "Generating tree..."
    root = Node(1, 1, None)

    if not valid_tree(root):
        print "Looks like this tree isn't correct"

    print "Let's take a look at your tree."
    display_tree(root)


def walk_tree(root, queue):
    if len(queue) > 0 and root.depth < Node.max_depth:
        root.left.value = root.value
        if root.lft_nbor is not None:
            root.left.value += root.lft_nbor.value
        root.right.value = root.value
        if root.rgt_nbor is not None:
            root.right.value = root.value + root.rgt_nbor.value
        queue.remove(root)
        if root.depth + 1 < Node.max_depth:
            queue.append(root.left)
            queue.append(root.right)
        if len(queue) > 0:
            walk_tree(queue[0], queue)



def valid_input(desired_depth):
    return desired_depth >= 1


def valid_tree(root):
    return True


def display_tree(root):
    print "Position: " + root.position + ", Value: " + str(root.value)
    if root.left is not None and root.right is not None:
        display_tree(root.left)
        display_tree(root.right)


def test_tree_building():
    Node.max_depth = 1
    print "~~~ depth 1 ~~~"
    root1 = Node("", 1, 1)
    walk_tree(root1, [root1])
    display_tree(root1)

    Node.max_depth = 2
    print "~~~ depth 2 ~~~"
    root2 = Node("", 1, 1)
    walk_tree(root2, [root2])
    display_tree(root2)

    Node.max_depth = 3
    print "~~~ depth 3 ~~~"
    root3 = Node("", 1, 1)
    walk_tree(root3, [root3])
    display_tree(root3)

    Node.max_depth = 4
    print "~~~ depth 4 ~~~"
    root4 = Node("", 1, 1)
    walk_tree(root4, [root4])
    display_tree(root4)

    Node.max_depth = 5
    print "~~~ depth 5 ~~~"
    root5 = Node("", 1, 1)
    walk_tree(root5, [root5])
    display_tree(root5)

test_tree_building()






