import pygame
from pygame.rect import Rect, RectType
from pygame.surface import SurfaceType, Surface
from typing import Union


class Node(pygame.sprite.Sprite):
    _image: Union[Surface, SurfaceType, None]
    _rect: Union[Rect, RectType, None]
    next: None
    prev: None

    # definition for the initialization of a Node object
    #
    def __init__(
        self,
        color: Union[tuple, None],
        x_val: Union[int, None],
        y_val: Union[int, None],
    ) -> None:
        if color is not None and x_val is not None and y_val is not None:
            pygame.sprite.Sprite.__init__(self)
            self._image = pygame.Surface([20, 20])
            self._image.fill(color)
            pygame.draw.rect(self._image, color, [x_val, y_val, 20, 20])
            self._rect = self._image.get_rect()
            self._rect.x = x_val
            self._rect.y = y_val

        self.next = None
        self.prev = None

    # retrieves the image of a Node
    #
    @property
    def image(self) -> pygame.surface:
        return self._image

    # retrieves the rectangular surface of a Node
    #
    @property
    def rect(self) -> pygame.rect:
        return self._rect

    # retrieves the x coordinate of the invoking Node
    #
    @property
    def x(self) -> int:
        return self._rect.x

    # sets the x coordinate of the invoking Node
    #
    @x.setter
    def x(self, x_val: int) -> None:
        self._rect.x = x_val

    # retrieves the y coordinate of the invoking Node
    #
    @property
    def y(self) -> int:
        return self._rect.y

    # sets the x coordinate of the invoking Node
    #
    @y.setter
    def y(self, y_val: int) -> None:
        self._rect.y = y_val

    # increments movement of a Node in the x & y directions
    #
    def move(self, x_val: int, y_val: int) -> None:
        self._rect.x += x_val
        self._rect.y += y_val


class LinkedList:
    head: Node
    tail: Node
    _length: int

    # definition for the initialization of a doubly Linked List
    #
    def __init__(self, color: tuple, x_val: int, y_val: int) -> None:
        self.head = Node(color, x_val, y_val)
        self.tail = Node(None, None, None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self._length = 1

    # return the length of the Linked List itself
    #
    @property
    def length(self) -> int:
        return self._length

    # inserts a Node at the tail of a Linked List in O(1) time
    #
    def ll_insert(self, color: tuple, x_val: int, y_val: int) -> None:
        new_node = Node(color, x_val, y_val)
        new_node.next = self.tail
        new_node.prev = self.tail.prev
        self.tail.prev = new_node
        new_node.prev.next = new_node
        self._length += 1

    # searches a Linked List and returns the Node at the specified x
    # and y coordinates
    #
    def ll_search(self, x_val: int, y_val: int) -> Union[Node, None]:
        curr = self.head.next
        while curr != self.tail:
            if curr.x == x_val and curr.y == y_val:
                return curr
            curr = curr.next
        return None
