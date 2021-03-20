class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:    # linked list로 구현.
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, value):   # 맨 뒤에 데이터 추가하기
        new_node = Node(value)
        if self.is_empty(): # 비어있을 때는 head와 tail 모두 None상태 이므로
            self.head = new_node
            self.tail = new_node
        self.tail.next = new_node
        # print("self.tail.next.data",self.tail.next.data)
        # new_node = self.tail
        # print("new_node.data", new_node.data)
        self.tail = new_node    # self.tail을 바꿔야하는거다. new_node를 바꾸는게 아니다.

    def dequeue(self):  # 맨 앞의 데이터 뽑기
        if self.is_empty():
            return "Queue is Empty"
        node = self.head    # 우선 다른 변수에 저장, 포인터를 잃어버릴 수 있기 때문
        # node.next = self.head 
        self.head = node.next
        return node.data

    def peek(self): # 맨 앞의 데이터 보기
        if self.is_empty():
            return "Queue is empty"
        return self.head.data

    def is_empty(self): # 큐가 비었는지 안비었는지 여부 반환
        return (self.head is None)

queue = Queue()
queue.enqueue(3)
print(queue.peek())
queue.enqueue(5)
print(queue.peek())
queue.enqueue(7)
print(queue.peek())
queue.dequeue()
print(queue.peek())
queue.dequeue()
print(queue.peek())
queue.dequeue()
print(queue.peek())