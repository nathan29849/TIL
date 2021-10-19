
class Node:
    def __init__(self, elem, link=None):
        self.data = elem
        self.link = link

from nodefile import Node
class LinkedList():
    def __init__(self):
        self.head = None
        self.data = elem
        self.link = link        

    def find(self, data):
        node = self.head

        while node is not None:
            if node.data == data: return node
            node = node.link
        return node
a = LinkedList()
a.head = "TEST"