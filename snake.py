from ll import LinkedList


class Snake(LinkedList):
    # definition of a Snake object
    #
    # self : the instance of the Snake itself
    #
    def __init__(self, color, x, y):
        super().__init__(color, x, y)
        self.color = color
        self.length = 1
    
    # function for growing the body of the snake object
    #
    # self : the instance of the Snake itself
    #
    def grow(self, x, y):
        self.ll_insert(self.color, x, y)
        self.ll_insert(self.color, x, y)
        self.ll_insert(self.color, x, y)
        self.ll_insert(self.color, x, y)
        self.length = self.ll_length()

    def move(self):
        last_pos = [self.head.get_x(), self.head.get_y()]
        curr = self.head.next
        while curr != None:
            temp_last_pos = [curr.get_x(), curr.get_y()]
            curr.rect.x = last_pos[0]
            curr.rect.y = last_pos[1]
            last_pos = temp_last_pos
            curr = curr.next
            
    
    # returns true if the Snake is out of bounds from the game grid
    #
    def out_of_bounds(self):
        if self.head.rect.x in range(0, 800) and self.head.rect.y in range(0, 600):
            return False
        return True
