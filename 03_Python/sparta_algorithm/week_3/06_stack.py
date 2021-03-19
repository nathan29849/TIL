class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:    # 후입선출 Last In First Out(LIFO)
    def __init__(self):
        self.head = None # head를 통해 넣고 빼는 작업을 해주기 위함.
    
    # 첫번째 노드에 추가
    def push(self, value):
        new_node = Node(value)
        new_node.next = self.head # 새로 만든 노드의 다음을 self.head로 정한다.
        self.head = new_node    # 원래의 self.head는 더이상 처음에 있지 않으므로 self.head를 새로운 노드로 할당한다.

    # 첫번째 노드를 삭제
    def pop(self):
        soon_delete = self.head
        if self.is_empty():
            return "Stack is Empty"

        # if soon_delete.next is not None:
        #     self.head = soon_delete.next
        # else:
        #     self.head = None
        self.head = self.head.next
        return soon_delete # 학교에서와 달리 버려진 노드를 None처리 해주지는 않는듯.


    # 첫번째 노드 확인
    def peek(self):
        if self.is_empty():
            return "Stack is Empty"
        return self.head.data   # 보기 쉽게 data를 반환하기로 함

        

    # stack이 비어있는지 확인 (첫번째 노드 비어있으면 비어있는거겠지?)
    def is_empty(self):
        # if self.head is not None:   # 비어있지 않을 경우
        #     return False
        # else:   # 비어있을 경우
        #     return True
        
        return self.head is None    # 한 줄로도 구현이 가능함.



stack = Stack() # 인스턴스 생성이 가장 처음해야 할 일!
stack.push(3)
print(stack.peek())
stack.push(4)
print(stack.peek())
print(stack.pop().data)
print(stack.pop().data)
print(stack.pop())
print(stack.is_empty())