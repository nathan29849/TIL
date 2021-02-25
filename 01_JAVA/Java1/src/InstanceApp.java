import java.io.IOException;
import java.io.PrintWriter;


public class InstanceApp {
    public static void main(String[] args) throws IOException{
        PrintWriter p1 = new PrintWriter("result1.txt"); // 인스턴스 만들
        p1.write("Hello 112\n");
        p1.write("Was as");
        p1.close();

        PrintWriter p2 = new PrintWriter("result2.txt");
        p2.write("Hello 2");
        p2.close();

        System.out.println(p1.toString());
        p2.toString();
        p2.write("Hello 2");

    }
}
