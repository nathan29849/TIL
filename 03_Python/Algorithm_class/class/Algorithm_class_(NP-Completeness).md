# NP-Completeness

- 효율적인 알고리즘이 없는 문제.

## ⛳️ 문제의 종류

<img src="https://images.velog.io/images/nathan29849/post/43b05967-6c37-4627-82e9-2f50dce6681d/image.png" width="70%">

### 🎯 현실적인 시간

- 다항식 시간을 의미 `O(N^k)` (k : 상수)
  - 입력의 크기 N의 다항식으로 표시되는 시간
  - ex : 3n^k + 5n^k-1 + ...
- 비다항식 시간의 예
  - 지수시간 (`2^n`)
  - 계승시간 (`n!`)

### 🎯 Yes or No 문제와 최적화 문제

- Yes/No 문제

  - 예 : 그래프 G에서 해밀토니안(Hamiltonian) 경로(사이클)가 존재하는가?
  - 해밀토니안 경로(사이클) : 모든 정점을 한 번만 지나서 원점으로 돌아오는 경로(사이클)

- 최적화 문제

  - 예 : 에지에 가중치가 있는 그래프 G에서 길이가 가장 짧은 해밀토니안 경로(사이클)의 길이를 구하라
  - => `Traveling Salsman Problem`(TSP) ~ 아주 유명한 문제임.

- Yes/No 문제와 최적화 문제는 동전의 앞뒷면 같은 성격을 보인다.

<img src="https://images.velog.io/images/nathan29849/post/6e405d36-9bf4-45b8-aecf-a8b27937997a/image.png">

---

## ⛳️ NP-Complete 이론

- Yes/No의 대답을 요구하는 문제에 국한(Decision 문제에 국한)
  - 그렇지만 최적화 문제와도 밀접한 관계가 있다.
- 문제를 현실적인 시간에 풀 수 있는가에 관한 이론(polynomial time에 해결가능?)
- NP-Complete는 거대한 군을 이룸
  - 이 중 한 문제만 현실적인 시간안에 풀 수 있다면, 그 군에 속한 다른 모든 것도 저절로 풀린다는 논리적 연결관계를 갖고있다.
    (현실적인 시간안에 푸는 방법으로 바꿔서 풀기.. 같은)

### 🎯 현재까지의 연구결과

- 어떤 문제가 NP-Complete임이 확인되면,
  - 지금까지의 연구결과로는 이 문제를 현실적인 시간에 풀 수 있는 방법 없음.
- 그러나 이 사실이 아직 증명이 되지는 않음.
- 클레이 수학 연구소의 21세기 7대 백만불짜리 문제 중 하나
  - P = NP 문제

### 🎯 Poly-Time Reduction(다항식 시간 변환)

- 상황

  - 문제 B는 쉽다.
  - 문제 A는 Yes/No 대답이 일치하는 문제 B로 쉽게 변형된다.(변환해서 풀기 가능)
    <img src="https://images.velog.io/images/nathan29849/post/74e53e31-cdaa-460a-b313-a685239851a0/image.png" width="80%">

- 문제 A의 사례 𝞪(instance, 특정 사례)를 문제 B의 사례 𝛃로 바꾸되, 아래 성질을 만족하면 `polynomial-time reduction`(다항식 시간 변환)이라 하고, 이를 `𝞪 ≤ 𝗉𝛃` 로 표기한다.
  - (1) 변환은 다항식 시간에 이루어진다.
  - (2) 두 사례의 답은 일치한다.

<img src="https://images.velog.io/images/nathan29849/post/89a61945-0741-4aef-9908-4176e0dffb23/image.png" width="80%">

- 1. 문제 A를 다항식 시간에 문제 B로 변환한다.
- 2. 변환된 문제 B를 푼다.
- 3. 문제 B의 대답이 Yes이면, Yes, No면, No를 리턴한다.

**즉, 문제 B가 쉬운 문제라면 문제 A도 쉬운 문제이다. (둘다 다항식 시간 내 풀이 가능)**

### 🎯 P와 NP (Decision 문제에 대하여,,)

- P (Polynomial)
  - 다항식 시간에 Yes or No를 대답할 수 있으면 P
- NP (Nondeterministic Polynomial) ... Non-Polynomial의 준말아님 주의.

  - Yes 대답이 나오는 해를 제공했을 때,
    이것이 **Yes 대답을 내는 해라는 사실**을 다항식 시간에 확인해 줄수 있으면 NP
    (❗️❗️❗️매우 중요❗️❗️❗️)

- 어떤 문제가 NP임을 보이는 것은 대부분 아주 쉽다.
  - NP-Complete 증명에서 형식적으로 확인하고 넘어가는 정도

---

## ⛳️ NP-Complete/Hard

<img src="https://images.velog.io/images/nathan29849/post/258f9def-10d2-457c-99b7-be518cfa5235/image.png">

- 다음 성질을 만족하면 문제 L은 `NP-Hard`이다.

  - 모든 NP 문제가 L로 **다항식 시간에 변환가능** 하다.
  - L이 쉽게 풀리면 NP도 쉽게 풀린다.
  - BUT, A만큼 B가 풀기 어려워 NP-Hard라고 한다.

- 다음 두 성질을 만족하면 문제 L은 `NP-Complete` 이다.
  - 1.  L은 NP이다.
  - 2.  L은 NP-Hard이다.
  - NP에 속하는 모든 문제를 L로 변환하여 **해결할 수 있으면,** `NP-Complete`

> < 정리 >
> ✔︎ NP-Complete는 NP-Hard의 일부이므로 NP-Complete인 문제를 NP-Hard라고 불러도 맞다.
> ✔︎ NP-Complete의 성질 1)은 대부분 자명하므로, 핵심에 집중하기 위해 NP-Hard에 초점을 맞추자.

### 🎯 정리 1

- 문제 L이 다음의 성질을 만족해도 `NP-Hard`이다.
  - 알려진 임의의 `NP-Hard`문제인 A로부터, 문제 L로 다항식 시간안에 변환이 가능하다면, 문제 L도 `NP-Hard`문제이다.

<img src="https://images.velog.io/images/nathan29849/post/4d588576-ca11-47ee-b6e4-917f5267e626/image.png" width="80%">

- 만일 문제 L을 쉽게 풀 수 있다면, 문제 A도 쉽게 풀 수 있다.
  (A문제를 L문제로 바꿔 풀면 되니까!) => 이게 NP-Complete
- 그러므로 모든 NP 문제를 쉽게 풀 수 있다. (변환해서~.)

### 🎯 NP-Hard 증명의 예

- 해밀토니안 싸이클 문제가 `NP-Hard`임은 알고 있다고 가정한다.
- 이를 이용해서 TSP 문제(외판원 문제)가 `NP-Hard`임을 보일 수 있다.
- 해밀토니안 싸이클 문제의 instance(사례) A를 아래와 같이 TSP 문제의 instance B로 다항식 시간에 변환한다.

<img src="https://images.velog.io/images/nathan29849/post/8ea490ba-3ef6-4c58-9524-1c26926472a1/image.png">

### 🎯 직관과 배치되는 NP-Complete 문제의 예

- Shortest path (쉬운문제)

  - 그래프의 정점 s에서 t로 가는 shortest path는 간단히 구할 수 있다.
  - ex. Dijkstra, Prim, Kruskal Algorithm

- Longest path (어려운 문제)  
  ~~ 이 중 사이클이 없으면 쉬움(DAG:DFS & Dynamic Programming)

  - 그래프의 정점 s에서 t로 가는 longest path는 간단히 구할 수 없다.
  - `NP-Complete`

- 얼핏 비슷해 보이지만 위 두 문제의 난이도는 천지차이다! (지금까지의 연구결과)

---

---

- Longest Path 문제
  - 주어진 그래프에서 vertex s에서 t로 가는 길이 k 이상인 simple path가 존재하는가? (Decision 문제로 바꾸어 풀 수 있음)
- 두 점 사이 해밀토니안 경로(≠사이클) 문제 (사이클 아님!)
  - 주어진 그래프에서 정점 s에서 t에 이르는 해밀토니안 경로가 존재하는가?
  - `NP-Complete`라고 알려져 있음.
  - 위 문제로 변환하여 풀 수 있음!

<img src="https://images.velog.io/images/nathan29849/post/871c58b0-0df4-4d8b-83a8-54fe3c70468f/image.png">

- 두 점 사이 해밀토니안 경로 문제의 instance A로부터 Longest Path 문제의 instance B로 변환 (다항식 시간)

<img src="https://images.velog.io/images/nathan29849/post/92c1ff5b-74c2-4d8c-9006-b2e3951cdbc3/image.png">

---

## ⛳️ NP 이론의 유용성

- 어떤 문제가 `NP-Complete/Hard` 임이 확인이 되면,

  - 1.  쉬운 알고리즘을 찾으려는 헛된 노력은 일단 중지!(효율적 알고리즘 없음)
  - 2.  주어진 시간 예산 내에서,
        최대한 좋은 해를 찾는 알고리즘(heuristic) 개발에 집중!
        (최적해, 정확한 해에 가까운 해를 찾는데 노력을 기울이자)

- 만약 최적해를 찾고싶다면, 가지치기를 통한(Bounding function) Backtracking을 이용한다. 불가능하면 2)의 방법을 이용.

> 레오나드 레빈
> "때로는 어떤 것이 불가능하다는 사실이 유용할 때도 있다."

---

## ⛳️ 추가 내용

<img src="https://images.velog.io/images/nathan29849/post/3331baf7-78b9-4f64-8475-efd952a10e77/image.png">

<img src="https://images.velog.io/images/nathan29849/post/b39c7c36-f640-4000-b253-d4e865bcb834/image.png">

<img src="https://images.velog.io/images/nathan29849/post/1a6c9b09-41ed-4cdc-b368-591a556938a7/image.png" width="45%">
