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
visited = []


def dfs_recursion(adjacent_graph, cur_node, visited_array):
    # if cur_node not in visited_array:
    #     visited_array.append(cur_node)      # root_node를 visited_array에 넣는 것 부터 시작!
    # for i in adjacent_graph[cur_node]:      # 인접 노드를 하나씩 돌면서 ~
    #     if i not in visited_array:          # 아직 방문하지 않았다면,
    #         visited_array.append(i)         # 추가해 준다.
    #         dfs_recursion(adjacent_graph, i, visited_array) # 그리고 추가해 준 노드를 시작노드로 삼고, recursion
    #     else:   # 모든 인접 노드를 다 방문했을 때. ( i in visited_array )
    #         if cur_node == 1:   # 만약 root_node로 돌아왔다면 끝낸다. (더 이상 돌 node가 없기 때문)
    #             return
    #         prior_node = adjacent_graph[cur_node][0]    # 이전 노드로 돌아가야해
    #         dfs_recursion(adjacent_graph, prior_node, visited_array)    # 그리고 이전 노드를 시작노드로 삼고, recursion
    # 해설
    visited_array.append(cur_node)
    for adjacent_node in adjacent_graph[cur_node]:
        if adjacent_node not in visited_array:
            dfs_recursion(adjacent_graph, adjacent_node, visited_array)

dfs_recursion(graph, 1, visited)  # 1 이 시작노드입니다!
print(visited)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 이 출력되어야 합니다!