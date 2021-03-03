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
```
