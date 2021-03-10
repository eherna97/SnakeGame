from ll import LinkedList


class Snake:
    # definition of a Snake object
    #
    # self : the instance of the Snake itself
    #
    def __init__(self, x, y):
        self.body = LinkedList()
        self.length = 1
        self.x = x  # starting x coordinate
        self.y = y  # starting y coordinate
    
    # function for growing the body of the snake object
    #
    # self : the instance of the Snake itself
    #
    def grow(self):
        self.body.ll_insert(None)
        self.body.ll_insert(None)
        self.body.ll_insert(None)
        self.body.ll_insert(None)
        self.body.ll_insert(None)
        self.length = self.body.ll_length()
    
    # moves the Snake instance to the left 1 block
    # 
    # self : the instance of the Snake itself
    #
    def move_left(self):
        self.x -= 1
    
    # moves the Snake instance to the right 1 block
    #
    # self : the instance of the Snake itself
    #
    def move_right(self):
        self.x += 1
    
    # moves the Snake instance upwards 1 block
    #
    # self : the instance of the Snake itself
    #
    def move_up(self):
        self.y += 1
    
    # moves the Snake instance downward 1 block
    #
    # self : the instance of the Snake itself
    #
    def move_down(self):
        self.y -= 1
