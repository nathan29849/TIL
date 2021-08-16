알고리즘 문제를 풀면서 TimeComplexity에 대해 자료형 별로 다르다는 것을 알게 되었다.

그래서 이번엔 파이썬의 다양한 자료형 별로 주요 연산자의 TimeComplexity를 비교해 보고자 한다.

(해당 내용은 초보몽키님의 개발공부로그를 참고하였다.)

# List

| Operation     | Example                   | Big-O       | Notes                                                                             |
| ------------- | ------------------------- | ----------- | --------------------------------------------------------------------------------- |
| Index         | List[i]                   | O(1)        | -                                                                                 |
| Store         | List[i] = "a"             | O(1)        | -                                                                                 |
| Length        | len(List)                 | O(1)        | -                                                                                 |
| Append        | List.append("a")          | O(1)        | 1개의 원소로 넣음                                                                 |
| Pop           | List.pop()                | O(1)        | List.pop(-1)과 동일<br/>마지막 인덱스의 element를 pop                             |
| Pop           | List.pop(i)               | O(N)        | index를 찾아 element를 pop                                                        |
| Clear         | List.clear()              | O(1)        | List=[]과 유사                                                                    |
| Slice         | List[k:n]                 | O(n-k)      | List[:] : O(len(List)-0<br/> = O(N)                                               |
| Extend        | List.extend(...)          | O(len(...)) | 확장 길이에 따라 다름<br/>리스트 형태로 넣으면,<br/>원소들이 차례로 들어가기 때문 |
| Construction  | List(...)                 | O(len(...)) | 생성 길이에 따라 다름                                                             |
| check ==, !=  | List_1 == List_2          | O(N)        | 비교                                                                              |
| Insert        | List.insert(index, value) | O(N)        | index를 찾아 value를 추가                                                         |
| Delete        | del [i]                   | O(N)        | index를 찾고난 후 삭제<br/>pop과 달리 리스트의 구간 삭제 가능                     |
| Remove        | List.remove(...)          | O(N)        | 인덱스가 아닌 값을 입력하는 방식<br/>(pop, del과 다름)                            |
| Containment   | x in/not in List          | O(N)        | 검색                                                                              |
| Copy          | List.copy()               | O(N)        | List[:]와 동일함                                                                  |
| Extreme value | min(List), max(List)      | O(N)        | 검색                                                                              |
| Reserve       | List.reverse()            | O(N)        | 반대로 정렬                                                                       |
| Iteration     | for v in List:            | O(N)        | 반복                                                                              |
| Sort          | List.sort()               | O(N\*logN)  | -                                                                                 |
| Multiply      | k\*List                   | O(k\*N)     | -                                                                                 |

# Dict

> 키와 값을 갖는 데이터 구조
> 키는 내부적으로 hash 값으로 저장
> 순서를 따지지 않는다. 즉, 인덱스가 없다.

- (참고)
  - 집합은 키를 변경할 수 없음
  - iteration 도중 size가 바뀌어선 안됨
  - value로 key 값을 찾아낼 수는 없음

| Operation          | Example     | Big-O       | Notes                   |
| ------------------ | ----------- | ----------- | ----------------------- |
| <mark>Index</mark> | d[k]        | O(1)        | -                       |
| Store              | d[k] = v    | O(1)        | -                       |
| Length             | len(d)      | O(1)        | -                       |
| Delete             | del d[k]    | O(1)        | -                       |
| get/set default    | d.method    | O(1)        | -                       |
| Pop                | d.pop(k)    | O(1)        | -                       |
| Pop item           | d.popitem() | O(1)        | -                       |
| Clear              | d.clear     | O(1)        | s = {} or = dict() 유사 |
| View               | d.keys()    | O(1)        | d.values()와 동일       |
| Construction       | dict(...)   | O(len(...)) | -                       |
| Iteration          | for k in d: | O(N)        | -                       |

# Set

> 중복을 허용하지 않고 순서가 없다(Unordered).
> 리스트나 튜플은 순서가 있기(ordered) 때문에 인덱싱을 통해 자료형의 값을 얻을 수 있지만,
> set 자료형은 순서가 없기(unordered) 때문에 인덱싱으로 값을 얻을 수 없다. 이는 딕셔너리와 비슷하다.

> 만약 set 자료형에 저장된 값을 인덱싱으로 접근하려면 다음과 같이 리스트나 튜플로 변환한후 해야 한다.

| Operation    | Example        | Big-O        | Notes                                                        |
| ------------ | -------------- | ------------ | ------------------------------------------------------------ |
| Length       | len(s)         | O(1)         | -                                                            |
| Add          | s.add(5)       | O(1)         | -                                                            |
| Containment  | x in/not in s  | O(1)         | list와 tuple은 모두 O(N)                                     |
| Remove       | s.remove(...)  | O(1)         | list와 tuple은 모두 O(N)                                     |
| Discard      | s.discard(...) | O(1)         | similar to s = set()                                         |
| Construction | set(...)       | O(len(....)) | depends on length                                            |
| check ==, != | s != t         | O(len(s))    | len(t)와 같음.<br/>두 집합의 길이가 다르면 False 반환 - O(1) |
| Iteration    | for v in s:    | O(N)         | Worst: no return/break in loop                               |
| Copy         | s.copy()       | O(N)         | -                                                            |

#### Reference

- [초보몽키 개발공부로그](https://wayhome25.github.io/python/2017/06/14/time-complexity/)
- [Python wiki's Time Complexity](https://wiki.python.org/moin/TimeComplexity)
- [Complexity of Python Operations](https://www.ics.uci.edu/~pattis/ICS-33/lectures/complexitypython.txt)
