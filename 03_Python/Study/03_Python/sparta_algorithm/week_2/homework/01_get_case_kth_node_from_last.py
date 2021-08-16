# Q. 링크드 리스트의 '끝에서' K번째 값을 반환하시오.
 
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

    def get_kth_node_from_last(self, k):
        # 구현해보세요!
        node = self.head
        length = 0
        while node is not None:
            length += 1
            node = node.next
        
        length = length - k
        result = self.head
        for i in range(length):
            result = result.next
        return result

        # fast = self.head
        # slow = self.head

        # for i in range(k):
        #     fast = fast.next

        # while fast is not None:
        #     fast = fast.next
        #     slow = slow.next
        
        # return slow


linked_list = LinkedList(6) # 1
linked_list.append(7)   # 2
linked_list.append(8)   # 3
# linked_list.append(9)   # 4
# linked_list.append(10)  # 5
# linked_list.append(11)  # 6
# linked_list.append(12)  # 7

print(linked_list.get_kth_node_from_last(2).data)  # 7이 나와야 합니다!
# linked_list.get_kth_node_from_last(3)