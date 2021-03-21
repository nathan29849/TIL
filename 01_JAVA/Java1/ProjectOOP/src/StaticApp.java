class Foo{
    public static String classVar = "I class Var";
    public String instanceVar = "I instance Var";
    public static void classMethod(){
        System.out.println(classVar);   // OK
//        System.out.println(instanceVar); // Error
    }
}

public class StaticApp {
    public static void main(String[] args) {
        System.out.println(Foo.classVar);   // mainmethod 내에서는 외부 class를 통해서는 당연히 클래스 변수에 접근 가능
        // System.out.println(Foo.instanceVar); // instance 변수에는 접근 불가

        Foo f1 = new Foo();
        Foo f2 = new Foo();
        System.out.println("--------");

        f1.classMethod();   // I class Var
        Foo.classMethod(); // I class Var
        System.out.println("--------");

        f1.classVar = "Changed by f1";
        System.out.println(f1.classVar);    // Changed by f1
        System.out.println(f2.classVar);    // Changed by f1
        System.out.println(Foo.classVar);   // Changed by f1
        System.out.println("--------");

        f2.instanceVar = "Changed by f2";
        System.out.println(f2.instanceVar);  // Changed by f1
        System.out.println(f1.instanceVar); // I instance Var
    }
}
