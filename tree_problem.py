# Tree problem solution by Jack Davis for Neuroscouting interview

class Node:

    def __init__(self, value, depth, max_depth):
        Node.max_depth = max_depth
        self.value = value
        self.depth = depth
        self.left = self.create_new_left()
        self.right = self.create_new_right()

    def create_new_left(self):
        return 1

    def create_new_right(self):
        return 1

def main():
    desired_depth_str = input("How deep should this tree be? ")
    desired_depth_int = int(desired_depth_str)
    if not valid_input(desired_depth_int) :
        return

    print "Generating tree..."
    root = Node(1, 0, desired_depth_int)

    if not valid_tree(root):
        print "Looks like this tree isn't correct"

    print "Let's take a look at your tree."
    display_tree(root)
