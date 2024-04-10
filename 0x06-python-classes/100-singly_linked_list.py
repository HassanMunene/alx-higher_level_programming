#!/usr/bin/python3
'''define a node and create a singly linked list'''

class Node:
    '''define a node structure with two components'''
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        '''return data priv attr'''
        return self.__data

    @data.setter
    def data(self, value):
        '''assing data attr'''
        if isinstance(value, int) is False:
            raise TypeError('data must be an integer')
        else:
            self.__data = value

    @property
    def next_node(self):
        '''return next_node'''
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        '''assign a value to next node'''
        if value is not None and isinstance(value, Node) is False:
            raise TypeError('next_node must be a node object')
        else:
            self.__next_node = value

class SinglyLinkedList:
    '''create a singly linked list'''
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        '''define the linked list'''
        new_node = Node(value)
        if self.__head is None or self.__head.data >= new_node.data:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current = self.__head
            while current.next_node is not None and current.next_node.data < new_node.data:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        '''print the singly linked list'''
        if self.__head is None:
            return "Empty list"

        result = ""
        current = self.__head

        while current is not None:
            result += str(current.data) + "\n"
            current = current.next_node
        return result
