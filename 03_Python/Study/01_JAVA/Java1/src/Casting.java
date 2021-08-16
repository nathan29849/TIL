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
