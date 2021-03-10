public class LoopArray {
    public static void main(String[] args) {
        String[] users = new String[3];
        users[0] = "nathan";
        users[1] = "peter";
        users[2] = "smith";

        for(int i = 0; i < users.length; i++){
//            System.out.println("<li>"+users[i]+"</li>"); // index 활용
//            System.out.println("---");
            System.out.println(users[i]+ ",");
        }

    }
}
