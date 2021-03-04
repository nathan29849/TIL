## JAVA 기본

### JAVA 조건문

```
if (income > 10000.0) {
    devidend1 = income * 0.5;
    devidend2 = income * 0.3;
    devidend3 = income * 0.2;
} else {
    devidend1 = income * 1;
    devidend2 = income * 0;
    devidend3 = income * 0;
}
```

### JAVA 배열

- 파이썬과 달리 변수의 자료형이 배열 선언시 들어간다.

```
double[] devidendRates = new double[3];
devidendRates[0] = 0.5;
devidendRates[1] = 0.3;
devidendRates[2] = 0.2;

double devidend1 = income * devidendRates[0];
double devidend2 = income * devidendRates[1];
double devidend3 = income * devidendRates[2];
```

### JAVA 반복문

```
double[] dividendRates = new double[3];
dividendRates[0] = 0.5;
dividendRates[1] = 0.3;
dividendRates[2] = 0.2;
int i = 0;
while (i < dividendRates.length) {
    System.out.println("Devidend : "+ dividendRates[i]*income);
    i = i + 1;
}
```

### JAVA 메소드

- 메소드는 서로 연관된 코드를 모아 이름을 붙인 것. 코드를 깔끔하게 정리 가능
- 메소드를 만드는 단축키 : 수식을 드래그 한 후 option + command + M
- 또는 수식을 드래그 + 오른쪽 마우스 클릭 후 Refactor > Extract method 선택

```
double valueOfSupply = Double.parseDouble(args[0]); // Replace 단축키 : command + r
double vatRate = 0.1; // variable 설정 단축키 :  option + command + v
double vat = getVAT(valueOfSupply, vatRate);
}

private static double getVAT(double valueOfSupply, double vatRate) {
return valueOfSupply * vatRate;
}
```

<br/>

- 메소드 괄호 ( ) 내의 변수들이 main method 안에서 지역변수로 선언이 되어있기 때문에 그냥 빼서는 안된다.
- main method 바깥의 AccountingMethodApp 클래스의 전역변수로 선언해주면 된다.

```
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
```

- 변수의 선언만 바깥에서 하고, main 함수 내에서 값을 지정해주어도 된다.
