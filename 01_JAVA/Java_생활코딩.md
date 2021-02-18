# JAVA

C, C++ 등의 기존 언어에서는 각 운영체제별로 서로 다른 코드를 만들고 별도로 컴파일 해야만 실행할 수 있었다.

하지만 JAVA는 하나의 JAVA 코드만 만들면 모든 운영체제에서 동일하게 실행이 가능하다.

### JAVA 언어의 특징

- 1. 간결한 프로그래밍 문법 제공 (포인터 제거 및 가비지컬렉터를 통한 메모리 관리)
- 2. 뛰어난 이식성
- 3. 완전한 객체지향 언어
- 4. 멀티스레드 프로그래밍 지원 (복잡한 대용량 작업을 빠른 시간 내에 처리 가능)
- 5. 다양한 응용 프로그램 작성 가능
- 6. 많은 오픈 소스 라이브러리의 존재 (Apache Commons, Google Guava 등)

### JAVA의 작동 원리

![](https://images.velog.io/images/nathan29849/post/77be93b3-2293-42ac-93e0-686e5ca15568/image.png){: width="30%" height="30%"}

- 원인 : source, code, language
- 결과 : application, program

```
public class HelloWorldApp { // 우리가 생성한 파일명과 클래스 명이 같아야 함.
    public static void main(String[] args) { // main 이라는 약속된 이름의 메소드를 찾아서 실행시킴
        System.out.println("Hello World!!");
    }
}
```
