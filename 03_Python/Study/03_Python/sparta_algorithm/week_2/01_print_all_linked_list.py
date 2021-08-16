class Node:
    def __init__(self, data):
        self.data = data
        self.next = None # 처음 생성한 노드는 아무 것도 가리키지 않음.


node = Node(3)
print(node.data)
first_node = Node(4)
node.next = first_node
print(node.next.data)

class LinkedList:
    def __init__(self, data):
        self.head = Node(data)
    
    def append(self, data):
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = Node(data)

    def print_all(self):
        print("hihihi")
        cur = self.head
        # flag = True
        # while flag:
        #     if cur.next == None:
        #         flag = False
        while cur is not None:
            print(cur.data)
            cur = cur.next

linked_list = LinkedList(3)
print(linked_list.head.data) # 3
print(linked_list.head.next) # None

# [3] -> [4] -> [5] -> [6] -> [new]
linked_list.append(4)
linked_list.append(5)
linked_list.print_all() 