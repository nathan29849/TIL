Python의 deque라는 자료구조에 대해 알아보고, 언제 사용하는지 살펴보자.

## deque의 의미

- 큐(queue)는 선입선출(FIFO) 방식으로 작동하는 반면에 덱(deque)은 양방향 큐처럼 작동한다.

- 즉, 양쪽 방향에서 원소를 추가하거나 삭제할 수 있다.

- deque는 양 끝 원소의 append, pop이 압도적으로 빠르다 (`O(1)`의 시간 소요)
  - 반면, list는 양 끝 원소에 접근하여 삽입, 삭제를 하려고 하면 `O(n)`의 시간이 소요된다.

## deque 사용법

- `from collections import deque`를 입력해주고 사용한다.

```
from collections import deque

deq = deque()

# Add element to the start
deq.appendleft(1)

# Add element to the end
deq.append(2)

# Pop element from the start
deq.popleft()

# Pop element from the end
deq.pop()
```

| method                  | 설명                                                  |
| ----------------------- | ----------------------------------------------------- |
| deque.append(item)      | item을 덱 오른쪽 끝에 삽입                            |
| deque.appendleft(item)  | item을 덱 왼쪽 끝에 삽입                              |
| deque.pop()             | 덱의 오른쪽 끝 요소를 가져오면서 삭제                 |
| deque.popleft()         | 덱의 왼쪽 끝 요소를 가져오면서 삭제                   |
| deque.extend(array)     | 주어진 배열(array)를 순환하면서 <br> 덱 오른쪽에 추가 |
| deque.extendleft(array) | 주어진 배열(array)를 순환하면서 <br> 덱 왼쪽에 추가   |
| deque.remove(item)      | item을 덱에서 찾아 삭제                               |
| deque.rotate(num)       | 덱을 num만큼 회전 <br> (+ : 오른쪽, - : 왼쪽)         |

- 추가 : deque 안의 원소 개수를 구하기 위해서 `len(deque)`을 이용한다.

### deque.rotate(num) 추가 설명

- 양수 또는 음수 값을 파라미터(parameter)로 제공하여 덱을 좌, 우로 회전할 수 있다.

```
deq = deque([1, 2, 3, 4, 5])

deq.rotate(1)
print(deq)		# deque([5, 1, 2, 3, 4])

deq.rotate(-1)
print(deq)		# deque([1, 2, 3, 4, 5])
```

## deque는 언제 써야하는가?

- 덱은 스택(stack)처럼 사용할수도, 큐(queue)처럼 사용할수도 있다.

- 시작점의 값을 넣고 빼거나, 끝 점의 값을 넣고 빼는 데에 최적화된 연산 속도를 제공한다.

- 대부분의 경우 덱이 리스트보다 월등한 옵션을 가지고 있다고 말한다.

- 덱은 특히 push/pop 연산이 빈번한 알고리즘에서 장점이 부각된다.

---

참고 : [Leon's devlog](https://chaewonkong.github.io/posts/python-deque.html)
