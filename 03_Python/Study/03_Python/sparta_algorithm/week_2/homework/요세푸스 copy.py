# 요세푸스 문제는 다음과 같다.

# 1번부터 N번까지 N명의 사람이 원을 이루면서 앉아있고, 양의 정수 K(≤ N)가 주어진다. 
# 이제 순서대로 K번째 사람을 제거한다. 한 사람이 제거되면 남은 사람들로 이루어진 원을 따라 이 과정을 계속해 나간다. 
# 이 과정은 N명의 사람이 모두 제거될 때까지 계속된다. 원에서 사람들이 제거되는 순서를 (N, K)-요세푸스 순열이라고 한다. 
# 예를 들어 (7, 3)-요세푸스 순열은 <3, 6, 2, 7, 5, 1, 4>이다.

# N과 K가 주어지면 (N, K)-요세푸스 순열을 구하는 프로그램을 작성하시오.

# BOJ 11583
import time
start = time.time()
def josephus_problem(n, k):
   # 이 부분을 채워보세요!
    # josephus_list = list(range(1, n+1))
    josephus_list = [i for i in range(1, n+1)]   # 리스트를 한 줄로 나타내기
    number = len(josephus_list)
    result_list = []
    first_index = k-1
    index = first_index
    a = str(josephus_list.pop(index))
    result_list.append(a)
    # while len(josephus_list) > 0:
    for i in range(n-2):
        # number = len(josephus_list)
        index += first_index
        # index: 4 -> element 6제거  /  index: 6 -> number = 5 -> index: 1 -> element 2제거
        # index: 3 -> element 7제거  / index: 5 -> number = 3 -> index: 2 -> element 5제거
        # index: 4 -> number = 2 -> index : 2 
        while index >= len(josephus_list):
            index = index - len(josephus_list) 
        a = str(josephus_list.pop(index))
        result_list.append(a)
    result_list.append(josephus_list.pop(0))       # 마지막 남은 하나.
    print("<", ", ".join(map(str, result_list)), ">", sep='')



n, k = map(int, input().split())    # map, split, join 함수 익히기
josephus_problem(n, k)

finish = time.time()
print(finish - start)

# 해당 코드의 결과는 시간초과
# 코드를 줄이려 봤더니, 새로운 list에 append 하는 방식이 시간을 오래 잡아먹음 (K가 증가함에 따라 복잡도도 함께 증가)
# 따라서 규칙을 찾을려고 했는데 모범 답안의 방법을 어떤 식으로 생각하고 도출해낼 수 있는지가 궁금
# 연습을 어떤 방향으로 해야할까
# 직접 손으로 일일이 써가며 규칙을 찾는게 답?