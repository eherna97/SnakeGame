from ll import Node
from typing import List, Tuple


class Snake:
    __body: List[Node]
    __color: Tuple
    __index: int = 0

    def __init__(self, color: Tuple, x_val: int, y_val: int):
        self.__body = [Node(color, x_val, y_val, (0, 0))]
        self.__color = color

        
    @property
    def length(self) -> int:
        return len(self.__body)

    @property
    def head(self) -> Node:
        return self.__body[0]
    
    def grow(self, x: int, y: int, direction: Tuple[int, int]) -> None:
        for _ in range(0, 4):
            self.__body.append(Node(self.__color, x, y, direction))
    
    def move(self, position: Tuple[int, int]) -> None:
        for node in self.__body:
            node.move(position[0], position[1])
            position, node.direction = node.direction, position
            # node.x, node.y, position = position, (node.x, node.y)
            # prev_position = (node.x, node.y)
            # node.x, node.y = position
            # position = prev_position
    
    def out_of_bounds(self) -> bool:
        bounds = range(20, 820)
        return not (self.__body[0].x in bounds and self.__body[0].y in bounds)
    
    def __iter__(self) -> None:
        return self
    
    def __next__(self):
        
