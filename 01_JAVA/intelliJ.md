# IntelliJ Debug

- Breakpoint를 우클릭하면 조건(condition)을 걸어 실행할 수 있다.
  (특정 값이 들어올 때만 실행하고 싶을 때 유용할 듯)

### button

- #### resume : option + commmand + r

  (다음 breakpoint로 이동)

- #### step over : F8

  (현재 break 된 파일에서 다음 라인으로 이동)

- #### step into : F7
  (현재 break 된 라인에서 실행하고 있는 라인으로 이동한다.)
- #### force step into : option + shift + F7

  (skip이 필요할 때는 step into로,
  전부 확인이 필요하면 force step into로 이동하면서 디버깅 하면 됨.)

- #### step out : shift + F8

  (현재 break 된 라인에서 호출한 곳으로 이동한다. step into에서 빠져나올 때 씀)

- #### drop frame

  (call stack을 거슬러 올라감)
  (step out은 해당 라인이 실행된 후 돌아가지만, drop frame은 해당 라인이 실행되기 전에 돌아간다.)

- #### run to cursor : option + F9

  (포커스 되어있는 라인으로 이동), 단발성으로 break를 걸고싶을 때 사용

- #### Evaluate (option + F8 ) vs Watch : 기능은 동일
  - Evaluate
    - Evaluate를 클릭하면 팝업이 하나 등장하는데, 여기서 확인하고 싶은 코드를 입력하고 실행시키면 결과를 바로 확인할 수 있음
    - 모든 코드를 사용할 수 없고, 현재 라인에서 사용가능한 코드들만 실행 가능
      <br/><br/>
  - Watch
    - watches에서는 마음껏 디버깅 코드를 작성해 볼 수 있다.
    - 단순한 변수값부터 시작해서 Autowired된 코드까지 전부 사용가능하다.
    - 해당 라인에서 가능한 모든 값, 메소드를 사용할 수 있다.

\*\* 단, Evaluate의 경우 코드를 계속 수동 실행해야하지만, Watch의 경우 삭제하지 않는한, break line이 실행될때마다 자동 실행된다.

- #### call stack
  디버깅 화면의 좌측 하단에는 해당 break line에 오기까지의 call stack 이 출력된다.
  이를 통해 이전에 어떤 값들이 넘어 온것인지, 이전에 다른 연산을 했으면 어떻게 값이 바뀔지를 모두 확인할 수 있다.
  (특히 Spring과 같은 프레임워크에서 어떻게 코드가 실행되고 값이 변경되는지 확인할때 굉장히 유용하게 사용된다.)
