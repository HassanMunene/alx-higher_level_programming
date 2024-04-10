class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        '''getter method for privated data attr'''
        return self.__data

    @data.setter
    def data(self, value):
        '''setter method for private data attr'''
        if not isinstance(value, int):
            raise TypeError('data must be an integer')
        self.__data = value

    @property
    def next_node(self):
        '''return next_node'''
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        '''assign next_node with a value'''
        if value is not None or not isinstance(value, Node):
            raise TypeError('next_node must be a Node object')
        else:
            self.__next_node = value


class SinglyLinkedList(Node):
    def __init__(self):
        self.__header = None

    def insert_node(self, value):
        #first create the node
        Node.
