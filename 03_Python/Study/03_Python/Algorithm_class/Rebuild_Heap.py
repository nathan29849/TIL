def rebuildHeap(A, r, n): # A : 리스트, r : 루트노드, n : 전체 노드 개수
# r은 left subtree와 right subtree가 최대 힙일 때, 루트가 r인 최대 힙을 만듦
# r은 리스트에서 root의 위치임
    current = r
    value = A[r]    # 루트의 값을 value가 참조(value에 저장)
    while (2*current + 1 < n):
        leftChild = 2*current + 1
        rightChild = leftChild + 1
        # 두 자식 노드 중 큰 값의 노드를 largerChild로 이동

        if rightChild < n and A[rightChild] > A[leftChild]:
            largerChild = rightChild
        else:
            largerChild = leftChild

        if value < A[largerChild]: # largerChild의 값이 크면
            A[current] = A[largerChild]
            current = largerChild   # current를 largerChild로 내림
        else:
            break
    A[current] = value  
    # while문 바깥에 있는 이유 : current로 비교한 후 일단 value보다 큰 값을 다 바꿔주고 마지막에 current자리
    # 즉 마지막에 바뀐 largerChild자리에 원래의 value값을 넣어주면 된다. (매번 할 필요가 없음)