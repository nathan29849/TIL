# 요세푸스 문제는 다음과 같다.

# 1번부터 N번까지 N명의 사람이 원을 이루면서 앉아있고, 양의 정수 K(≤ N)가 주어진다. 
# 이제 순서대로 K번째 사람을 제거한다. 한 사람이 제거되면 남은 사람들로 이루어진 원을 따라 이 과정을 계속해 나간다. 
# 이 과정은 N명의 사람이 모두 제거될 때까지 계속된다. 원에서 사람들이 제거되는 순서를 (N, K)-요세푸스 순열이라고 한다. 
# 예를 들어 (7, 3)-요세푸스 순열은 <3, 6, 2, 7, 5, 1, 4>이다.

# N과 K가 주어지면 (N, K)-요세푸스 순열을 구하는 프로그램을 작성하시오.

# BOJ 1158

def josephus_problem(n, k):
   # 이 부분을 채워보세요!
    j_list = []
    result = []
    for i in range(1, n+1):  
        j_list.append(i)
        
    while len(j_list) > 0:
        count = 1
        for j in range(1, k+1, 1):
            if count != k:
                a = j_list.pop(0)
                j_list.append(a)
                count += 1
                # print(j_list)
            else:
                b = j_list.pop(0)
                result.append(str(b))
                count = 1
    
    awesome = ", ".join(result)
    
    print("<"+awesome+">")


n, k = map(int, input().split())    # map, split, join 함수 익히기
josephus_problem(n, k)

# 해당 코드의 결과는 시간초과
# 코드를 줄이려 봤더니, 새로운 list에 append 하는 방식이 시간을 오래 잡아먹음 (K가 증가함에 따라 복잡도도 함께 증가)
# 따라서 규칙을 찾을려고 했는데 모범 답안의 방법을 어떤 식으로 생각하고 도출해낼 수 있는지가 궁금
# 연습을 어떤 방향으로 해야할까
# 직접 손으로 일일이 써가며 규칙을 찾는게 답?