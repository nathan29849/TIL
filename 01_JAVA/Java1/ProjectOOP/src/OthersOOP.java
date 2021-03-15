import java.io.FileWriter;
import java.io.IOException;

public class OthersOOP {
    public static void main(String[] args) throws IOException {
        // class : System, Math, FileWriter
        // instance : f1, f2
        System.out.println(Math.PI);    // Math 라는 클래스에 PI 라는 변수가 있는 것.
        System.out.println(Math.floor(1.1)); // Math 라는 클래스에 floor 라는 메소드
        // 코드가 많아짐에 따라서 서로 연관된 같은 주제를 가지고 있는 변수와 메소드를 그룹핑한 껍데기가 "클래스"

        FileWriter f1 = new FileWriter("data.txt");
        f1.write("Hello");
        f1.write(" Java");
        f1.close();

        FileWriter f2 = new FileWriter("data2.txt");
        f2.write("Hello");
        f2.write(" Java2");
        f2.close();
    }
}
