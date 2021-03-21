class Cal {
    public int sum(int v1, int v2) {
        return v1 + v2;
    }
    // Overloading
    public int sum(int v1, int v2, int v3) {
        return this.sum(v1, v2) + v3;
    }
}
class Cal3 extends Cal {    // Cal class 를 확장해서 Cal class 가 가지고있던 모든 변수와 메소드를 상받게 된다는 말.
    public int minus(int v1, int v2) {
        return v1 - v2;
    }
    public int sum(int v1, int v2) {   // 상속받아  메소드도 수정이 가능함. -> 이를 Overriding 이라고 한다.
        System.out.println("Cal3");
        return super.sum(v1, v2);
    }
}
class newCal {
    int v1, v2;
    newCal(int v1, int v2){ // 클래스의 인스턴스가 만들어질 때 반드시 해야하는 일이 생성자 안에 들어가 있다.
        System.out.println("newCal init!");
        this.v1 = v1;
        this.v2 = v2;
    }
    public int sum(){
        return this.v1+v2;
    }
}
class newCal3 extends newCal{ // 따라서 자식 클래스도 생성자의 일을 똑같이 수행해야 한다. -> 반드시 생성자를 실행시키도록 강제하고 있는 것이다.
    newCal3(int v1, int v2) {
        super(v1, v2); // 여기서 super 는 부모 클래스이다. -> 즉 부모 클래스의 생성자이다.
        System.out.println("newCal3 init!");
    }
    public int minus(){
        return this.v1-v2;
    }

}

public class InheritanceApp {
    public static void main(String[] args) {
        newCal c= new newCal(11, 3);
        newCal3 c3 = new newCal3(2, 4);
        System.out.println(c3.sum()); // 6
        System.out.println(c3.minus()); // -2

    }
}
