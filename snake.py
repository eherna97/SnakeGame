from ll import LinkedList


class Snake(LinkedList):
    _color: tuple

    # definition for the initialization of a Snake object
    #
    def __init__(self, color: tuple, x_val: int, y_val: int) -> None:
        super().__init__(color, x_val, y_val)
        self._color = color

    # grows the body of a a Snake object by 4 Nodes
    #
    def grow(self, x_val: int, y_val: int) -> None:
        self.ll_insert(self._color, x_val, y_val)
        self.ll_insert(self._color, x_val, y_val)
        self.ll_insert(self._color, x_val, y_val)
        self.ll_insert(self._color, x_val, y_val)

    # moves a Snake and its body along the grid
    #
    def move(self) -> None:
        last_pos = [self.head.x, self.head.y]
        curr = self.head.next
        while curr != self.tail:
            temp_last_pos = [curr.x, curr.y]
            curr.x = last_pos[0]
            curr.y = last_pos[1]
            last_pos = temp_last_pos
            curr = curr.next

    # returns true if the Snake is out of bounds from the game grid
    #
    def out_of_bounds(self) -> bool:
        if self.head.x in range(20, 820) and self.head.y in range(20, 620):
            return False
        return True
