# 21:14~

# 위의 그래프를 예시로 삼아서 인접 리스트 방식으로 표현했습니다!
graph = {
    1: [2, 5, 9],
    2: [1, 3],
    3: [2, 4],
    4: [3],
    5: [1, 6, 8],
    6: [5, 7],
    7: [6],
    8: [5],
    9: [1, 10],
    10: [9]
}


def dfs_stack(adjacent_graph, start_node):
    visited = []
    stack = [start_node]    # [1]
    
    # while len(stack) != 0:
    while stack:    # 이렇게 조건을 걸어도 됨.
        pop_node = stack.pop()  # 1 # 9 # 10 # 5
        visited.append(pop_node) # [1] # [1, 9] # [1, 9, 10]  # [1, 9, 10, 5]
        for i in adjacent_graph[pop_node]:    # [2, 5, 9] # [1, 10] # [9] # [1, 6, 8]
            if i not in visited:    # 방문하지 않은 것들만 stack에 넣어줌.
                stack.append(i)     # [2, 5, 9] # [2, 5, 10] # [2, 5] # [2, 6,]
    
    return visited

                
    






print(dfs_stack(graph, 1))  # 1 이 시작노드입니다!
# [1, 9, 10, 5, 8, 6, 7, 2, 3, 4] 이 출력되어야 합니다!