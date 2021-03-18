import random
import pygame


class Node(pygame.sprite.Sprite):
    
    # definition for the init of a Node object
    #
    # surface : he game surface as defined in main game file
    # x       : the x coordinate of the Node
    # y       : the y coordinate of the Node
    # state   : whether the Node is alive or not
    #
    def __init__(self, color, x, y, state = False):
        pygame.sprite.Sprite.__init__(self)
        self.image  = pygame.Surface([20, 20])
        self.image.fill(color)
        pygame.draw.rect(self.image, color, [x, y, 20, 20])
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.state  = state
        self.next = None
    
    # defines the left movement of a single Node
    #
    def move_left(self):
        self.rect.x -= 20
    
    # defines the right movement of a singe Node
    #
    def move_right(self):
        self.rect.x += 20
    
    #defines the up movement of a single Node
    #
    def move_up(self):
        self.rect.y -= 20

    # defines the down movement of a single Node
    #
    def move_down(self):
        self.rect.y += 20


class LinkedList(Node):
    
    # definition for a singly-linked linked-list
    #
    # surface : the surface on which the Nodes will be displayed
    #
    def __init__(self):
        super.__init__(self, surface, color, x, y, state = False)
        self.head = Node(color, x, y)
        self.length = 1
    
    # return the length of the linked-list itself
    # 
    def ll_length(self):
        return self.length
    
    # inserts a node with specified data at the head of the linke-list
    #
    # surface : the surface that the Node will be added to
    #
    def ll_insert(self, surface):
        new_node = Node(surface, self.rect.x, self.rect.y)
        new_node.next = self.head.next # link before unlinking head
        self.head.next = new_node # now unlink head and link to new
        self.length += 1
    
    # traverses the linkedlist and searches for the state of the Node
    #
    # state : the state of the Node, dead or alive
    #
    def ll_search(self, state):
        temp_node = self.head.next
        while temp_node != None:
            if temp_node.state == state:
                return state  # return the state if the value is equal
            temp_node = temp_node.next
        return None

    # prints a LinkedList's members
    #
    def ll_print(self):
        temp_node = self.head.next
        while temp_node != None:
            temp_node.node_print()
            print(" -> ", end="")
            temp_node = temp_node.next  # move to the next node
        print("\n")
