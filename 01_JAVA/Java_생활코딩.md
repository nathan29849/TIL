# JAVA

C, C++ 등의 기존 언어에서는 각 운영체제별로 서로 다른 코드를 만들고 별도로 컴파일 해야만 실행할 수 있었다.

하지만 JAVA는 하나의 JAVA 코드만 만들면 모든 운영체제에서 동일하게 실행이 가능하다.
<br/>

### JAVA 언어의 특징

1. 간결한 프로그래밍 문법 제공 (포인터 제거 및 가비지컬렉터를 통한 메모리 관리)
2. 뛰어난 이식성
3. 완전한 객체지향 언어
4. 멀티스레드 프로그래밍 지원 (복잡한 대용량 작업을 빠른 시간 내에 처리 가능)
5. 다양한 응용 프로그램 작성 가능
6. 많은 오픈 소스 라이브러리의 존재 (Apache Commons, Google Guava 등)
   <br/><br/>

### JAVA의 작동 원리

<img src="https://images.velog.io/images/nathan29849/post/77be93b3-2293-42ac-93e0-686e5ca15568/image.png" width="50%" >

- compile : 확장자가 .java인 파일을 기계가 이해할 수 있도록 전환하는 역할
  <br/><br/>

#### 같은 의미의 단어들

- 원인 : source, code, language
- 결과 : application, program

#### Code

```
public class HelloWorldApp { // 우리가 생성한 파일명과 클래스 명이 같아야 함.
    public static void main(String[] args) { // main 이라는 약속된 이름의 메소드를 찾아서 실행시킴
        System.out.println("Hello World!!");
    }
}
```

---

<br/>

## 데이터와 연산

- Number (+, -, \*, ...)
- String (length, substring, search, ...)
- etc

각각의 데이터마다 처리하는 방식(=연산 방식) 이 존재함.

### 숫자와 연산

```
public class Datatype {
   public static void main(String[] args) {
       // Operator(연산자)
       System.out.println(6 + 2); // 8
       System.out.println(6 - 2); // 4
       System.out.println(6 * 2); // 12
       System.out.println(6 / 2); // 3

       System.out.println(Math.PI); // 3.141592~~
       System.out.println(Math.floor(Math.PI)); // 3.0
       System.out.println(Math.ceil(Math.PI)); // 4.0
   }
}
```

### 문자열의 표현

```
public class StringApp {
    public static void main(String[] args){
        System.out.println("HelloWorld"); // String(문자열)
        System.out.println('H'); // Character(한 글자를 표현하는 데이터 타입)
        System.out.println("H"); // 이렇게 해도 String.
        // Java에서는 작은 따옴표가 특수한 데이터 타입을 가리킴.
        // String은 Character들이 모여있는 것

        System.out.println("Hello " +
                 "World"); // Hello World
        System.out.println("Hello \nWorld" ); // \n : new line을 의미함. (줄바꿈)
        System.out.println("Hello \"World\""); // escape
    }
}
```

---

<br/>

## 변수(VARIABLE)

수학에서는 그 값이 변할 수 있는 것을 변수라고 말함.

자바에서는 변수를 선언할 때 데이터 타입을 함께 작성하여야 한다.

- String은 Object라 Method가 존재하지만,
  int나 double은 Object가 아니라 Method가 존재하지 않는다.
  <br/>

### CASTING

데이터 타입을 다른 데이터 타입으로 바꾸어주는 역할을 함.

<img src="https://images.velog.io/images/nathan29849/post/32f1bcda-884a-490f-bb4a-ecf1a3eacd45/image.png" width="50%" >

```
public class Casting {
    public static void main(String[] args){

        double a = 1.1;
        double b = 1; // 손실이 없기 때문에 자동으로 CASTING 된 것이라 볼 수 있다.
        System.out.println(b); // b에 정수를 넣었지만 double로 선언했기에 자동으로 1.0 정수로 바뀐 것을 알 수 있음

        int c = (int) 1.1; // 손실이 생기므로 의도적으로 CASTING 해야 함.
        System.out.println(c);

        // java int to string
        String f = Integer.toString(1); // 1
        System.out.println(f.getClass()); // class java.lang.String
        // .getClass() : 어떤 데이터 타입인지 알려줌
    }
}
```

<br/>

### int : primitive 자료형(long, float, double 등등...)

- 산술 연산이 가능하다.
- null로 초기화 할 수 없다.

### Integer : Wrapper 클래스 => 한 객체를 의미

- Unboxing을 하지 않으면 산술 연산이 불가능 but, null 값을 처리 가능함
- null 값 처리가 용이하기 때문에 SQL과 연동할 경우에 처리를 원활하게 할 수 있음
- DB에서 자료형이 정수형이지만 null 값이 필요한 경우 VO(Value Object)에서 Integer를 사용할 수 있음.

#### int와 Integer간의 변환 : Boxing과 Unboxing이라고 함

- Boxing : Primitive 자료형 => Wrapper 클래스
- Unboxing : Wrapper 클래스 => Primitive 자료형

---

<br/>

## 입력과 출력

##### java popup input text swing

```
import javax.swing.*;
...
String id = JOptionPane.showInputDialog("Enter a ID");
```

이렇게 하면 팝업창에 아이디를 입력하는 창이 뜬다.
<br/><br/>

##### java string to double conversion

```
moodeLamp.setBright(Double.parseDouble(Bright));
```

Double.parseDouble(); 로써 바꿀 수 있다.

---

<br/>

### Arguments 설정하기

IntelliJ에서는 debug시 **Edit Configuration** 을 통해 arguments를 미리 설정해서 적용할 수 있다.

```
public class OKJavaGoInHomeInput {
    public static void main(String[] args){

    }
```

위에 있는 **args** 또한 변수이다.

- 이 **args**는 프로그램과 프로그램 사용자를 매개해주기 때문에 매개변수(parameter) 라고 하기도 한다.

- 위에서 **Edit Configuration**를 통해 설정했던 Argumets가 **args**를 통해 들어온다고 생각하면 된다.

- **args**가 여러개라면 앞에 있는 **String[ ]** 을 통해 문자열이라는 데이터 타입으로 들어온다.

참고 : IntelliJ에서는 **" "** 로 Argumets를 구분하여 준다.

---

<br/>

### Debug

1. pwd(print working derectory)를 통해 현재 내 위치를 파악하는 것이 중요
2. /usr/libexec/java_home 를 통해 java가 설치된 위치를 찾아낼 수 있음

```
javac Programming.java // 자바 파일을 컴파일하여 클래스 파일을 만듦
cat Programming.java // 자바 파일 내부의 코드를 터미널 창에 띄움
java Programming // 클래스 파일을 만든 뒤 Run 하는 명령어
java -cp ".:lib" OKJavaGoInHome.java
// 해당 java 파일과 import 해오는 패키지가 동일 디렉토리 레벨이 있지않은 경우
// class path 명령어를 통해 실행할 수 있다.
// 동일 디렉토리 레벨에 있으면 알아서 실행됨.

java OKJavaGoInHomeInput "JAVA APT 507" "7.0" // 이런 식으로 매개변수 넣어서 자바 클래스 파일을 실행할 수 있다.
```
