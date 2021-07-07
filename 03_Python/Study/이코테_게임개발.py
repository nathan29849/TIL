# 이것이 코딩 테스트다 - 게임 개발 (구현 실전문제)
from sys import stdin
def solution(n, m, col, row, d, visited, game):
        # 0 1 2 3 (0 : 북, 1 : 동, 2 : 남, 3 : 서)
    dx = [0, -1, 0, +1] 
    dy = [-1, 0, +1, 0]
    count = 1                   # 처음 시작하는 지점은 무조건 육지
    visited[col][row] = True

    while True:
        flag = False
        for i in range(4):
            new = (d + i)%4
            if col+dx[new] < 0 or col+dx[new] > n-1 or row+dy[new] < 0 or row+dy[new] > m-1:
                # 애초에 방문할 수 없는 지역(맵을 벗어남)이라면 넘기기
                continue
            elif game[col+dx[new]][row+dy[new]] == 0 and visited[col+dx[new]][row+dy[new]] == False:
                # 육지 & 방문하지 않음 이라면, 방문하기.
                visited[col+dx[new]][row+dy[new]] = True    # 방문 True 변경
                count += 1      # 방문한 칸 + 1
                col += dx[new]  # 위치 업데이트
                row += dy[new]
                d = (new+1)%4   # 방향 업데이트 
                flag = True
                break
        if flag == False:   # 모든 방향을 탐색했는데도 불구하고 갈 곳이 없을 때 = 후진
            back = (d + 1)%4
            col += dx[back]
            row += dy[back]
            if game[col][row] == 1:
                return count # 게임 종료

    return

n, m = map(int, stdin.readline().split())
col, row, d = map(int, stdin.readline().split())
game = []
visited = []
for i in range(n):
    game.append(list(map(int, stdin.readline().split())))
    visited.append([False for i in range(m)])

print(solution(n, m, col, row, d, visited, game))

# 4 4
# 1 1 0
# 1 1 1 1
# 1 0 0 1
# 1 1 0 1
# 1 1 1 1 