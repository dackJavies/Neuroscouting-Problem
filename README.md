# Neuroscouting Tree Problem
# Author: Jack Davis

**How it works**
* High level implementation
    * Recursively generate a tree, verify it, and display it to the user based on their specifications
    * Uses a static variable in a Node class to control the depth of the tree that it generates
        * Tree is generated in constructor, so once you make the root node the tree just creates itself
    * The verification process is just a recursive tree walk where it checks that each node's value is correct
        * i.e. the value must be the sum of its parent's value and the appropriate parent's neighbor if applicable
* How to run it
    * You should just be able to do `python tree_problem.py` on the command line
    * Written in Python 2.7.13

**Code organization**
* Node class
    * Fields
        * Position in the graph represented by a string
            * Empty string for root, _L_ for left child, _R_ for right child
            * Example: _LRL_
                * Start at root
                * Go to its left child
                * Go to that node's right child
                * Go to that node's left child
                * Arrived
        * Value stored in this node
        * The depth of this node
        * The left and right neighbors of this node
        * The left and right children of this node
    * Methods
        * `create_tree(queue)`
            * Recursive tree generation function only called if the desired depth is greater than 1
            * Creates children in a breadth-first manner, making sure to initialize their values and neighbors appropriately
            * _queue_ is an accumulating FIFO queue that stores the worklist of un-built nodes
        * `create_children()`
            * Instantiates the left and right child nodes for this node
            * Whitespace used to separate the different components of assembly
                * i.e. wanted to make the places where fields were being assigned distinct
            * This instantiation does not make concrete values; some are assigned later
        * `set_neighbors()`
            * Just a nice name grouping for calling two separate functions
        * `set_left_nbors()`
            * Sets all neighbor fields relating to the left child of this node
            * Sets the right neighbor to be the left child's sibling i.e. right child
            * Tests to see if this node's left child has an "uncle"/"aunt" node in the first place
            * If so, makes sure that the left child is neighbors with the appropriate cousin
                * Also confirms the relationship is mutual i.e. the cousin thinks of the left child as its neighbor
        * `set_right_nbors()`
            * Sets all neighbor fields relating to the right child of this node
            * Works the same as `set_left_nbors(), just with regards to the right child`
* Functions
    * `main()`
        * Prompts the user for their desired depth
        * Validates the given number
        * Generates the tree
        * States its validity
        * Displays the tree
    * `valid_input(desired_depth)`
        * Returns a boolean value of whether the desired depth given by the user is valid
        * i.e. the depth must be greater than 1
    * `valid_tree(root)`
        * Tests the validity of a tree given its root node
        * Recurs through the tree, checking that each value is correct
            * i.e. value of a node is the sum of its parent's value and the value of the parent's left/right neighbor
            * Direction of neighbor matches which child the node in question is; left for left, right for right
        * Returns boolean result of whether the tree is valid
    * `display_tree(root)`
        * Recurs through tree, printing the position and the value at that position
            * Position is represented as a string of L's and R's
            * Root node is empty string
            * Example: _LLR_
                * Start at root node
                * Go to its left child (_L_)
                * Go to that node's left child (_L_)
                * Go to that node's right child (_R_)
                * Arrived at position _LLR_
* Tests
    * `test_tree_building()`
        * Generates and displays trees of depths 1 through 5
        * At this stage, the validity checker was not written
        * I used these to manually check that the trees generated were correct
    * `test_tree_validity()`
        * Generates, displays, verifies, then mangles and re-displays and re-verifies trees of depths 1 through 5
        * Basically does what `test_tree_building()` did but adds a mutation of the tree and makes sure the validity checker senses the change
        * All the displaying was to confirm by hand that the validity checker was getting it right

**Flow of control**
* This is a single-threaded program
* Control starts in `main` to get input from the user
* Switches to `valid_input` to make sure the user didn't give a bad depth
    * Control returns to `main`, but program concludes if the program received bad input
    * Flow continues below if input is good
* Then the created instance of the Node object takes control to generate the tree
    * Control trickles through the hierarchy of functions here
    * `create_tree` calls `create_children` many times (once for each node in all layers but the last)
    * `create_tree` also calls `set_neighbors` many times (once for each node in all layers but the last)
    * `set_neighbors` calls `set_left_nbors` and then `set_right_nbors` once each
* Control returns to `main` and flows directly to `valid_tree`
* Once `valid_tree` is complete, control goes back to `main` and into `display_tree`
* After this, program is done

**Optimizations**
* As you'll see from my commit history, I progressed through a slightly sloppy initial solution to a cleaner final one
* Initially, I got my tests to pass using two passes through the tree. I created a skeleton of nodes with value 1
    * This skeleton tree was then fleshed out with the proper additions post-generation
    * In the cleanup phase, this was brought down to one clean pass done during instantiation
        * I spotted the redundancy in doing two separate breadth-first walks through the tree. The merging of the passes was pretty much trivial
* Other tree walking functions like `valid_tree` and `display_tree` also use one pass to do their work

