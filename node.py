import pygame
from pygame.rect import Rect, RectType
from pygame.surface import SurfaceType, Surface
from typing import Union


class Node(pygame.sprite.Sprite):
    _image: Union[Surface, SurfaceType, None]
    _rect: Union[Rect, RectType, None]

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

    # Moves the node to the given x, y position
    #
    def move(self, x_val: int, y_val: int) -> None:
        self._rect.x = x_val
        self._rect.y = y_val
