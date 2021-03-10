class Node:

    # definition of what a Node member contains
    #
    # self : the instance of Node
    # data : data contained in the Node
    #
    def __init__(self, data):
        self.data = data
        self.next = None
    
    # function for printing a Node 
    #
    # self : the instance of node
    #
    def node_print(self):
        print(self.data, end="")






