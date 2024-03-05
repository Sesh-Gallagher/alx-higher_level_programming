#!/usr/bin/python3
"""Defines classes for a singly_linked list."""


class Node:
    """Represents a node in a singly_linked list."""

    def __init__(self, data, next_node=None):

        """Initialize a new node.
        Args:
            data (int): Data of the new node.
            next_node (Node): Next node of the new node.
        """

        self.next_node = next_node
        self.data = data

    @property
    def data(self):

        """Get and/or set the data of the node."""
        return (self.__data)

    @data.setter
    def data(self, value):

        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):

        """Get and/or set the next_node of the node."""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):

        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Represents a singly_LinkedList."""

    def __init__(self):
        """Initalize a new Singly_LinkedList."""
        self.__head = None

    def sorted_insert(self, value):
        """Insert a new node to the Singly_LinkedList.

        node is inserted into the list at the correct
        ordered numerical position.


        Args:
            value (node): The new node to insert.
        """

        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            tmp = self.__head
            while (tmp.next_node is not None and
                    tmp.next_node.data < value):
                tmp = tmp.next_node
            new.next_node = tmp.next_node
            tmp.next_node = new

    def __str__(self):
        """Define the print() representation of a Singly_LinkedList."""

        values = []
        tmp = self.__head
        while tmp is not None:
            values.append(str(tmp.data))
            tmp = tmp.next_node
        return ('\n'.join(values))
