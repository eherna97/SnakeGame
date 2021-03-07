from ll import LinkedList

class Snake:
    
    # definition of a Snake object
    #
    # self : the instance of the Snake itself
    #
    def __init__(self):
        self.body = LinkedList()
        self.length = 1
    
    # function for growing the body of the snake object
    #
    # self : the instance of the Snake itself
    #
    def grow(self):
        self.body.ll_insert(None)
        self.body.ll_insert(None)
        self.body.ll_insert(None)
        self.body.ll_insert(None)
        self.length = self.ll_length()

