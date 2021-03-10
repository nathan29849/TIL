#Q.  다음과 같은 두 링크드 리스트를 입력받았을 때, 합산한 값을 반환하시오. 
# 예를 들어 아래와 같은 링크드 리스트를 입력받았다면,
# 각각 678, 354 이므로 두개의 총합
# 678 + 354 = 1032 를 반환해야 한다.

# 단, 각 노드의 데이터는 한자리 수 숫자만 들어갈 수 있다.
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


def get_linked_list_sum(linked_list_1, linked_list_2):
    # 구현해보세요!
    sum_1 = []
    sum_2 = []
    total_sum = 0
    # while문을 중첩은 아니지만 두 번 연속 쓰는건 좀 비효율적인가..? -> 정답이랑 비교 해보자!
    node_1 = linked_list_1.head
    node_2 = linked_list_2.head

    while node_1 is not None:
        sum_1.append(node_1.data)
        node_1 = node_1.next

    while node_2 is not None:
        sum_2.append(node_2.data)
        node_2 = node_2.next

    for i in range(len(sum_1)):
        total_sum += sum_1[i] * (10**(len(sum_1)-i-1))
        # total_sum = sum_2[i] * (10**(len(sum_2)-i))
    return total_sum

linked_list_1 = LinkedList(6)
linked_list_1.append(7)
linked_list_1.append(8)


linked_list_2 = LinkedList(3)
linked_list_2.append(5)
linked_list_2.append(4)

print(get_linked_list_sum(linked_list_1, linked_list_2))