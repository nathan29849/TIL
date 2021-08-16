정렬을 배우고 나서 sort를 자주 썼었는데,
리스트 이외의 자료형에서도 정렬을 해주고 싶었으나 sort는 list 내장 함수이기 때문에 불가능 하였다.

하지만 우리에겐 sorted()가 있었으니.. 비교를 해보며 어떨 때 써야할지 체크해보자

## Sort()

- 기존 리스트 내부의 원소들을 정렬된 상태로 바꾸어 준다.
- 리스트 내장함수로써 리스트에서만 사용이 가능하다.
- .sort(reverse=True)를 통해 역순 정렬이 가능하다.

## Sorted()

- 기존의 리스트 원소를 정렬해주는 것이 아닌 정렬된 리스트를 새로 만들어 준다.
- 어떠한 iterable 객체도 받을 수 있다. (ex. dict)
- sorted(iterable object, reverse=True)를 통해 역순 정렬이 가능하다.

```python
sample_list = [('classic', 1450), ('pop', 3100)]
new_list = sorted(sample_list, reverse=True)
# [('pop', 3100), ('classic', 1450)]
```

### Lambda

- sorted 함수의 매개변수로 key를 넣어줄 수 있는데, lambda를 통해 key 인자에 함수를 넘겨주면 해당 함수의 반환 값을 비교하여 정렬한다.

- 오름차순 정렬
  - sorted(iterable object, key = lambda x: x[0])
- 내림차순 정렬
  - sorted(iterable object, key = lambda x: x[0], reverse=True)
  - sorted(iterable object, key = lambda x: -x[0])

```python
sample_list = [[0, 500], [2, 150], [3, 800]]
new_list = sorted(sample_list, key=lambda item: item[1])
# [[2, 150], [0, 500], [3, 800]]	index = 1 의 순서대로 정렬 된 모습
```

#### ✌️숫자 뿐만아니라 문자열에 대해서도 인덱스 기준 정렬이 가능하다.

```python
sample_list = ["aycd", "azgh", "axwa"]
new_list = sorted(sample_list, key=lambda item: item[1])
# ['axwa', 'aycd', 'azgh']	index = 1 의 순서대로 정렬 된 모습
```

참고 블로그 : [aonee.log](https://velog.io/@aonee/Python-%EC%A0%95%EB%A0%AC-sort-sorted-reverse)

#### ✌️2개 이상의 원소를 가진 튜플 혹은 리스트 등을 기준에 따라 정렬할 때, 한 가지 기준으로 하는 것은 부정확한 결과를 낳을 수 있다.

<mark><strong>(항상 신경쓰도록 하자!!)<strong></mark>

```python
# 첫 번째 인덱스만 기준으로 둘 때
sample_list = [[4, 500], [2, 500], [3, 800]]
new_list = sorted(sample_list, key=lambda item: item[1])
print(new_list) # [[4, 500], [2, 500], [3, 800]]

# 첫 번째 인덱스를 기준으로 정렬한 후, 0번 째 인덱스로 나머지를 정렬하여줄 때
new_list = sorted(sample_list, key=lambda item: (item[1], item[0]))
print(new_list) # [[2, 500], [4, 500], [3, 800]]
```
