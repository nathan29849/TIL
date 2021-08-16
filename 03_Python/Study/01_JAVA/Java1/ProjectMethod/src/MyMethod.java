import java.io.FileWriter;
import java.io.IOException;

public class MyMethod {
    public static void main(String[] args) throws IOException {
                            // 인자, argument : 함수 안으로 주입한 구체적인 값
        printTwoTimes("A", "-");
        System.out.println(twoTimes("a", "-"));
//        writeFileTwoTimes("B", "*");
        FileWriter fw = new FileWriter("output.txt");
        fw.write(twoTimes("a", "*"));
        fw.close();
    }
    public static String twoTimes(String text, String delimiter){
        String out = "";
        out = out + delimiter + "\n";
        out = out + text + "\n";
        out = out + text + "\n";
        return out; // return 으로 함수를 끝내면 변수로 그 함수의 return 값을 바꿀 수 있다.
    }

                                        // 매개변수, parameter : 메소드 바깥 쪽에서 안으로 흘려보내주는 변수.
    public static void printTwoTimes(String text, String delimiter) {
        System.out.println(delimiter);
        System.out.println(text);
        System.out.println(text);
    }
//    public static void writeFileTwoTimes(String text, String delimiter) throws IOException {
//        FileWriter fw = new FileWriter("output.txt");
//        fw.write(delimiter+"\n");
//        fw.write(text+"\n");
//        fw.write(text+"\n");
//        fw.close();
//
//    }
}
