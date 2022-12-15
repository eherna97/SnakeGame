from ll import Node
from typing import List, Tuple


class Snake:
    __body: List[Node]
    __color: Tuple

    def __init__(self, color: Tuple, x_val: int, y_val: int):
        self.__body.append(Node(color, x_val, y_val))
        self.__color = color
        
    @property
    def length(self) -> int:
        return len(self.body)
    
    def grow(self, x: int, y: int) -> None:
        self.__body.append(Node(self.__color, x, y))
        self.__body.append(Node(self.__color, x, y))
        self.__body.append(Node(self.__color, x, y))
        self.__body.append(Node(self.__color, x, y))
    
    def move(self, position: Tuple[int, int]) -> None:
        for node in self.__body:
            node.x, node.y, position = position, (node.x, node.y)
            # prev_position = (node.x, node.y)
            # node.x, node.y = position
            # position = prev_position
    
    def out_of_bounds(self) -> bool:
        bounds = range(20, 820)
        return not (self.__body[0].x in bounds and self.__body[0].y in bounds)
