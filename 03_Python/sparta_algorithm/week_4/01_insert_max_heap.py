class MaxHeap:
    def __init__(self):
        self.items = [None]

    def insert(self, value):
        self.items.append(value)    # 일단 맨 마지막 노드에 위치 시키기.
        n = len(self.items)
        if n == 2:  # 루트 노드라면 그대로 끝내기.
            return
        else:   # 루트 노드가 아니라면 부모 노드와 크기 비교.
            child_index = self.items.index(value)
            parent_index = child_index//2
            while self.items[parent_index] < value: # 새로운 node가 부모노드보다 크다면,
                
                parent_value = self.items[parent_index]
                print("parent_index", parent_index, "parent_value", parent_value)
                print("child_index", child_index, "value", value)
                self.items[child_index] = parent_value   # 자식 노드에 부모 노드의 value 넣기.
                self.items[parent_index] = value # 부모 노드에 자식 노드의 value 넣기
                print("self.items", self.items)
                child_index = self.items.index(value)
                parent_index = child_index//2
                if parent_index == 0:
                    break
            return
                
                


# 부모노드 = 자식노드 인덱스 // 2
# 자식노드_1 = 부모노드 인덱스 * 2
# 자식노드_2 = (부모노드 인덱스) * 2 + 1  

max_heap = MaxHeap()
max_heap.insert(3)
max_heap.insert(4)
max_heap.insert(2)
max_heap.insert(9)
print(max_heap.items)  # [None, 9, 4, 2, 3] 가 출력되어야 합니다!