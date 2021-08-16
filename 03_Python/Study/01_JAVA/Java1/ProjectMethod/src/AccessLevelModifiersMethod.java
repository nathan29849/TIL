class Greeting{
    public static void hi(){
        // public, protected, default, private  : 외부에서의 접근하는 방법에 따라 달리 쓰임.
        //private : 같은 클래스 내에서만 사용 가능한 내부적인 메소드. public 은 그 반대임.
        System.out.println("Hi");
    }
}

public class AccessLevelModifiersMethod {
    public static void main(String[] args) {
        Greeting.hi();
    }
}
