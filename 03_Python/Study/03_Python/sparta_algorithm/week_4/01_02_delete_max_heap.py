# 15:46

class MaxHeap:
    def __init__(self):
        self.items = [None]

    def insert(self, value):
        self.items.append(value)
        cur_index = len(self.items) - 1

        while cur_index > 1:  # cur_index 가 1이 되면 정상을 찍은거라 다른 것과 비교 안하셔도 됩니다!
            parent_index = cur_index // 2
            if self.items[parent_index] < self.items[cur_index]:
                self.items[parent_index], self.items[cur_index] = self.items[cur_index], self.items[parent_index]
                cur_index = parent_index
            else:
                break

    def delete(self):
        # 구현해보세요!
        max_node = self.items[1]  # 8
        leaf_node = self.items[-1] # 4
        self.items[-1], self.items[1] = max_node, leaf_node  # 최댓값 노드와 리프노드를 교환함.
        cur_index = self.items.index(leaf_node)
        self.items.pop(-1)
        # child_index_2 = self.items.index(leaf_node)*2 + 1
        while cur_index*2 < len(self.items)-1:  # 현재 자식이 배열 안에 존재할 때까지만 반복하면 된다.
            child_index = cur_index*2
            if leaf_node < self.items[child_index]:
                self.items[child_index], self.items[cur_index] = leaf_node, self.items[child_index]
                cur_index = child_index
            elif leaf_node < self.items[child_index+1]:
                self.items[child_index+1], self.items[cur_index] = leaf_node, self.items[child_index+1]
                cur_index = child_index + 1
            else:
                break
        return max_node



max_heap = MaxHeap()
max_heap.insert(8)
max_heap.insert(7)
max_heap.insert(6)
max_heap.insert(2)
max_heap.insert(5)
max_heap.insert(4)
print(max_heap.items)  # [None, 8, 7, 6, 2, 5, 4]
print(max_heap.delete())  # 8 을 반환해야 합니다!
print(max_heap.items)  # [None, 7, 5, 6, 2, 4]