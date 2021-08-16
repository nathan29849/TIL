# 위의 그래프를 예시로 삼아서 인접 리스트 방식으로 표현했습니다!
graph = {
    1: [2, 3, 4],
    2: [1, 5],
    3: [1, 6, 7],
    4: [1, 8],
    5: [2, 9],
    6: [3, 10],
    7: [3],
    8: [4],
    9: [5],
    10: [6]
}


def bfs_queue(adj_graph, start_node):
    visited = []
    queue = [start_node]

    while queue:
        pop_node = queue.pop(0)         # 1 # 2
        if pop_node not in visited:
            visited.append(pop_node)    # 1 # [1, 2]
        for i in adj_graph[pop_node]:    # [2, 3, 4] # [1, 5]
            if i not in visited:
                queue.append(i)             # [2, 3, 4]
    return visited


print(bfs_queue(graph, 1))  # 1 이 시작노드입니다!
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 이 출력되어야 합니다!