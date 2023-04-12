from node import Node
from typing import List, Tuple, Union


class Snake:
    __body: List[Node]
    __color: Tuple
    __index: int = 0

    # definition for the initialization of a Snake object
    #
    def __init__(self, color: Tuple, x_val: int, y_val: int):
        self.__body = [Node(color, x_val, y_val)]
        self.__color = color
 
    # retrieves the length of the snake object
    #
    @property
    def length(self) -> int:
        return len(self.__body)

    # retrieves the head node of the snake object
    #
    @property
    def head(self) -> Node:
        return self.__body[0]
    
    # grows the snake object's body by a factor of four nodes
    #
    def grow(self, x: int, y: int) -> None:
        for _ in range(0, 4):
            self.__body.append(Node(self.__color, x, y))
    
    # moves the snake object along an x, y plane in the direction given
    #
    def move(self, direction: Tuple[int, int]) -> None:
        prev = self.head.x, self.head.y
        self.head.move(self.head.x + direction[0], self.head.y + direction[1])

        for node in self[1:]:
            tmp_prev = node.x, node.y
            node.move(*prev)
            prev = tmp_prev
    
    # checks if the snake object is in bounds of an x, y plane
    #
    def out_of_bounds(self, x_bound: int, y_bound: int) -> bool:
        bound = range(x_bound, y_bound)
        return not (self.__body[0].x in bound and self.__body[0].y in bound)
    
    # overloads the iteration operation for the snake object
    #
    def __iter__(self) -> None:
        return self
    
    # overloads the next operation for iterations over the snake object
    #
    def __next__(self) -> Node:
        if self.__index >= self.length:
            self.__index = 0
            raise StopIteration
        else:
            node = self[self.__index]
            self.__index += 1
            return node
    
    # overloads the indexing/slicing operation for the snake object
    #
    def __getitem__(self, key: Union[int, slice]) -> Union[Node, List[Node]]:
        if isinstance(key, slice):
            indices = range(*key.indices(self.length))
            return [self.__body[i] for i in indices]
        
        if 0 > key >= self.length:
            raise KeyError
        
        return self.__body[key]
