public class OutputMethod {

    // return 값의 데이터 타입을 함수 선언시 적어주어야 한다.
    public static String a(){
        // ...
        return "a";
    }
    public static int one(){
        // ...
        return 1;

    }
    // void 라는 뜻은 return 값이 없다는 뜻
    public static void main(String[] args) {
        System.out.println(a());
        System.out.println(one());
    }
}
