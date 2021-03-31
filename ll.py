import random
import pygame


class Node(pygame.sprite.Sprite):
    
    # definition for the init of a Node object
    #
    # color : the color of the Node
    # x     : the x coordinate of the Node
    # y     : the y coordinate of the Node
    #
    def __init__(self, color, x, y):
        if color != None and x != None and y != None:  # will allow creation of invisible tail w/o attributes
            pygame.sprite.Sprite.__init__(self)
            # drawing the instance of the Node
            self.image  = pygame.Surface([20, 20])
            self.image.fill(color)
            pygame.draw.rect(self.image, color, [x, y, 20, 20])
            self.rect = self.image.get_rect()
            # attributes of the Node
            self.rect.x = x
            self.rect.y = y
        self.next = None
        self.prev = None
    
    # defines movement of a Node in the x & y directions
    #
    # x : pixels moved in the x direction
    # y : pixels moved in the y direction
    #
    def move(self, x, y):
        self.rect.x += x
        self.rect.y += y
    
    # retrieves the x coordinate of the invoking Node
    #
    def get_x(self):
        return self.rect.x

    # retrieves the y coordinate of the invoking Node
    #
    def get_y(self):
        return self.rect.y


class LinkedList:
    
    # definition of a doubly-linked Linked List initialization
    #
    # color : the color to initialize the Head of a Linked List
    # x     : the x coordinate of the Head
    # y     : the y  coordinate of the Head
    #
    def __init__(self, color, x, y):
        self.head = Node(color, x, y)
        self.tail = Node(None, None, None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.length = 1
    
    # return the length of the Linked List itself
    # 
    def ll_length(self):
        return self.length
    
    # inserts a Node at the tail of a Linked List in O(1) time
    #
    # color : the color of the Node that will be inserted
    # x     : the x coordinate of the inserted Node
    # y     : the y coordinate of hte  inserted Node
    #
    def ll_insert(self, color, x, y):
        new_node = Node(color, x, y)
        new_node.next = self.tail
        new_node.prev = self.tail.prev
        self.tail.prev = new_node
        new_node.prev.next = new_node
        self.length += 1

    # searches a Linked List and returns the Node at the specified x
    # and y coordinates
    #
    # x : the x coordinate being searched for
    # y : the y coordinate being searched for
    #
    def ll_search(self, x, y):
        curr = self.head.next
        while curr != self.tail:
            if curr.get_x() == x and curr.get_y() == y:
                return curr
            curr = curr.next
        return None

