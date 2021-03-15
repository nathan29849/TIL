## JAVA 기본

### JAVA 제어문

<구성>

- boolean data type
- comparison operator
- conditional statement
- looping statement

#### JAVA 조건문(Conditional statement)

```java
if (income > 10000.0) { // boolean type만이 if 문 괄호 안에 들어갈 수 있다.
    devidend1 = income * 0.5;
    devidend2 = income * 0.3;
    devidend3 = income * 0.2;
} else {
    devidend1 = income * 1;
    devidend2 = income * 0;
    devidend3 = income * 0;
}
```

### Java ==과 equals의 차이점

- Java에는 2가지로 데이터 타입을 구분지을 수 있음
  1. primitive : boolean, int, double, short, long, float, char ...
     - 더이상 쪼갤 수 없는 데이터 타입
  2. non primitive : String, Array, Data, File ...
     - 더 쪼갤 수 있는 데이터 타입
- **==** 라는 동등비교연산자는 저장된 장소까지 같은지 물어보는 개념이고, **equals( )** 는 내용만 같은지를 물어보는 개념이다. 그러나 문자열의 경우 같은 값으로 할당하면, 같은 장소에 저장되므로 **==** 으로도 비교가능토록 취급된다.
  따라서 아래의 그림을 참고하자.
  <img src ="https://images.velog.io/images/nathan29849/post/565220f4-89f5-464d-be1e-84d9b6d38ee9/image.png" width="77%">
  <br/>
- 이 경우에는 args[0]="nathan" 일지라도 `inputId == id`가 `false`가 되는데, 그 이유는 입력 값들이 서로 다른 곳에 저장이 되어 그렇다고 이해하면 된다.

```java
public class AuthApp {
    public static void main(String[] args) {
        System.out.println(args[0]);
        String id = "nathan";
        String inputId = args[0];

        String password = "1234";
        String input_Password = args[1];

        System.out.println("Hi");
        if (inputId == id){  // 예상과 달리 비교가 안됨
            if (input_Password.equals(password)){
                System.out.println("Master!");
            } else {
                System.out.println("Wrong password!");
            }
        }
        else {
            System.out.println("Who are you?");
        }
    }
}

```

**결론 : 가장 중요한 것은 데이터 타입을 일일이 확인하여 어떤 방법으로 취급할지 정하는 것이다.
이유 : 객체는 복합 데이터 타입이므로 한 눈에 비교하는 것이 쉽지 않기 때문이다. 객체들마다 정책이 다를 수 있다.**

#### JAVA 배열

- 파이썬과 달리 변수의 자료형이 배열 선언시 들어간다.
- Index와 Element로 구성되어 있다.

```java
public class ArrayApp {
    public static void main(String[] args) {
        // nathan, peter, smith
        // String users = "nathan, peter, smith"; // 너무 비효율적임 -> 배열을 사용하자.
        String[] users = new String[3]; // 담고자하는 배열의 크기를 지정함.
        users[0] = "nathan";
        users[1] = "peter";
        users[2] = "smith";

        System.out.println(users[1]); // Index
        System.out.println(users.length); // 몇 개의 내용이 있단기보다는 크기가 얼마인 배열이다라고 생각

        int[] scores = {10, 100, 1000}; // 원소, Element
        System.out.println(scores[1]);
        System.out.println(scores.length);
    }
}
```

#### JAVA 반복문

> **for 반복문의 소괄호 안에 들어갈 정보**  
> (1; 2; 3)
>
> 1. 초깃값 세팅 코드
> 2. 반복을 더 해야하는지를 체크하는 boolean 값
> 3. 반복이 진행될 때마다 실행되어야 하는 코드

```java
double[] dividendRates = new double[3];
dividendRates[0] = 0.5;
dividendRates[1] = 0.3;
dividendRates[2] = 0.2;
int i = 0;
while (i < dividendRates.length) {
    System.out.println("Devidend : "+ dividendRates[i]*income);
    i = i + 1;
// 1, 초깃값 세팅 코드, 2. 반복을 더 해야하는지를 체크하는 boolean 값, 3. 반복이 진행될 때마다 실행되어야 하는 코드
for(int k = 0; k < 3; k++) {
    System.out.println(4);
}
}
```

<br/>

### JAVA 메소드

- 메소드는 서로 연관된 코드를 모아 이름을 붙인 것. 코드를 깔끔하게 정리 가능
- 메소드를 만드는 단축키 : 수식을 드래그 한 후 option + command + M
- 또는 수식을 드래그 + 오른쪽 마우스 클릭 후 Refactor > Extract method 선택
  - Refactoring의 핵심적 역할을 하는 것은 Method이다

Method를 통해 코드의 가독성을 높일 수 있고, 재사용이 가능하며, 유지보수의 편의성도 제공한다.

```java
public class MyMethod {
    public static void main(String[] args) {
                    // 인자, argument : 함수 안으로 주입한 구체적인 값
        printTwoTimes("A", "-");
        printTwoTimes("B", "*");
    }
                                // 매개변수, parameter : 메소드 바깥 쪽에서 안으로 흘려보내주는 변수.
    private static void printTwoTimes(String text, String delimiter) {
        System.out.println(delimiter);
        System.out.println(text);
        System.out.println(text);
    }
}
```

<br/>

- 메소드 괄호 ( ) 내의 변수들이 main method 안에서 지역변수로 선언이 되어있기 때문에 그냥 빼서는 안된다.
- main method 바깥의 AccountingMethodApp 클래스의 전역변수로 선언해주면 된다.

```java
public class AccountingMethodApp {
    public static double valueOfSupply = 10000.0; // 클래스 전역변수로 설정
    public static double vatRate = 0.1;
    public static void main(String[] args){

        double expenseRate = 0.3;
        double vat = getVAT();
        double total = valueOfSupply + getVAT();
    }
    private static double getVAT() {
    return valueOfSupply * vatRate;
    }
}
// public, protected, default, private  : 외부에서의 접근하는 방법에 따라 달리 쓰임.
//private : 같은 클래스 내에서만 사용 가능한 내부적인 메소드. public 은 그 반대임.
```

- 변수의 선언만 바깥에서 하고, main 함수 내에서 값을 지정해주어도 된다.
  <br/>

### 클래스

> static이 있는 것은 class method이다.
> static이 없는 것은 instance method이다.

- 예시

```java
class Print{
    public String delimiter;
    public void a(){
        System.out.println(this.delimiter);
        System.out.println("a");
        System.out.println("a");
    }

    public static void c(String delimiter){
        System.out.println(delimiter);
        System.out.println("c");
        System.out.println("c");
    }

}

public class StaticMethod {

    public static void main(String[] args) {
        Print.c("^^");   // class 소속일 때는 static을 넣어주어야한다.
        Print.c("$$");     // instance 소속과 class 소속은 static의 차이가 있다!

        // instance
        Print t1 = new Print();
        t1.delimiter = "-";     // 이렇게 하면 인자값을 줄 필요가 없게됨.
        t1.a(); // 이렇게 메소드가 인스턴스 소속일 때는 class method 의 static 을 빼주어야 한다.
}

```

- 서로 연관된 변수와 메소드를 그룹핑하여 이름을 붙인 것. (file로 치면 디렉토리의 역할)
- 구조를 결정하기 때문에 중요함.
- public class는 main method를 사용하는 곳에 사용한다고 생각하면 된다.
- 보통은 다른 클래스들을 만들면 따로 파일로 관리를 하여 준다. (한 파일 내에 있으면 복잡)

### 인스턴스

- 하나의 클래스를 복제해서 서로 다른 데이터의 값과 서로 같은 메소드를 가진 복제본.

```java
class Accounting {
    public double valueOfSupply;
    public double vatRate;
    public double expenseRate;
    public void print() {
        System.out.println("Value of supply : "+ valueOfSupply); // 전역변수라 그대로 변수로 써도 됨.
        System.out.println("VAT : "+ getVAT());
        System.out.println("Total : "+ getTotal());
        System.out.println("Expense : "+ getExpense());
        System.out.println("Income : "+ getIncome());
    }
    private  double getIncome()  {
        return valueOfSupply - getExpense();
    }
    private  double getExpense() {
        return valueOfSupply * expenseRate;
    }
    private  double getTotal() {
        return valueOfSupply + getVAT();
    }
    private  double getVAT() {
        return valueOfSupply * vatRate;
    }
}
```

```java
public class AccountingClassApp {
    public static void main(String[] args){
        // instance (이때는 static을 class 내부에서는 사용하면 안됨! )
        Accounting a1 = new Accounting();
        a1.valueOfSupply = 100000.0;
        a1.vatRate = 0.1;
        a1.expenseRate = 0.3;
        a1.print();

        Accounting a2 = new Accounting();
        a2.valueOfSupply = 100000.0;
        a2.vatRate = 0.4;
        a2.expenseRate = 0.2;
        a2.print();
    }
}
```
