public class BooleanApp {
    public static void main(String[] args) {
        System.out.println("One"); // string (유한히 많이 존재)
        System.out.println(1); // integer (무한히 많이 존재)

        System.out.println(true); // boolean (단 두 개)
        System.out.println(false);

        String foo = "Hello world";
        // String true = "Hello world";
        // true는 boolean으로 정해져있으므로 변수 이름으로 쓸 수 없다.
        // boolean data type
        // 이미 우리가 쓰는 컴퓨터 언어에서 '쓰임이 있는' 키워드들을 reserved word 라고 함.

        System.out.println(foo.contains("world")); // true
        System.out.println(foo.contains("nathan")); // false
    }
}
