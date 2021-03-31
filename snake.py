from ll import LinkedList


class Snake(LinkedList):

    # definition for a Snake initialization
    #
    # color : the color for each Node of the Snake
    # x     : the x coordinate of the Snake head
    # y     : the y coordinate of the Snake head
    #
    def __init__(self, color, x, y):
        super().__init__(color, x, y)
        self.color = color
        self.length = 1
    
    # grows the body of a a Snake object by 4 Nodes
    #
    # x : the x coordinate to insert the Nodes at
    # y : the y coordinate to insert the Nodes at
    #
    def grow(self, x, y):
        self.ll_insert(self.color, x, y)
        self.ll_insert(self.color, x, y)
        self.ll_insert(self.color, x, y)
        self.ll_insert(self.color, x, y)
        self.length = self.ll_length()
    
    # moves a Snake and its body along the grid
    #
    def move(self):
        last_pos = [self.head.get_x(), self.head.get_y()]
        curr = self.head.next
        while curr != self.tail:
            temp_last_pos = [curr.get_x(), curr.get_y()]
            curr.rect.x = last_pos[0]
            curr.rect.y = last_pos[1]
            last_pos = temp_last_pos
            curr = curr.next
            
    
    # returns true if the Snake is out of bounds from the game grid
    #
    def out_of_bounds(self):
        if self.head.rect.x in range(20, 820) and self.head.rect.y in range(20, 620):
            return False
        return True

