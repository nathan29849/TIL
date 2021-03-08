class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next

    def get_node(self, index):
        node = self.head
        count = 0
        while count < index:
            node = node.next
            count += 1
        return node

    # index번 째에 새로운 노드 값을 추가하는 것
    def add_node(self, index, value):
        new_node = Node(value)

        if index > 0:
            node = self.get_node(index - 1)
            next_node = node.next  # 원래 해당 인덱스에 있던 노드를 prior_node에 할당
            node.next = new_node    # index-1에 해당하는 노드의 다음 노드를 new_node로 할당
            new_node.next = next_node  # new_node의 다음 노드를 prior_node로 할당
        elif index == 0:
            new_node.next = self.get_node(index) # self.head
            self.head = new_node
        
        return new_node

linked_list = LinkedList(5)
linked_list.append(12)
linked_list.append(8)
print(linked_list.get_node(1).data) # -> 5를 들고 있는 노드를 반환해야 합니다!
linked_list.print_all()
print("----")
print(linked_list.add_node(0, 6).data)
print("----")
linked_list.print_all()