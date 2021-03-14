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
}
