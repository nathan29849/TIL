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
