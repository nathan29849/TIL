public class AuthApp {
    public static void main(String[] args) {
        System.out.println(args[0]);
        String id = "nathan";
        String inputId = args[0];

        String password = "1234";
        String input_Password = args[1];

        System.out.println("Hi");
//        if (inputId == id){  // 예상과 달리 비교가 안됨 -> 아마 주소값이 다른 String이라서 그런가?
//        if (inputId.equals(id)){
//            if (input_Password.equals(password)){
//                System.out.println("Master!");
//            } else {
//                System.out.println("Wrong password!");
//            }
//        }
//        else {
//            System.out.println("Who are you?");
//        }
        if (inputId.equals(id) && input_Password.equals(password)) {
            System.out.println("Master!");
        }
        else if (!input_Password.equals(password)){
            System.out.println("Wrong password!");
        }
    }
}
