public class AuthApp3 {
    public static void main(String[] args) {
//        String[] users = {"nathan", "peter", "smith"};
        String[][] users = {
                {"nathan", "1111"},
                {"peter", "2222"},
                {"smith", "3333"}
        }; // 배열 속 배열을 만드는 방법

        String inputId = args[0];
        String inputPass = args[1];

        boolean isLogined = false;
        for (int i = 0; i < users.length; i++){
            String[] current = users[i];
            if (
                    current[0].equals(inputId) &&
                            current[1].equals(inputPass)
            ) {
                isLogined = true;
                break; // break 가 속해있는 반복문을 끝냄.
            }
        }
        System.out.println("Hi,");
        if (isLogined){
            System.out.println("Master!!");
        } else {
            System.out.println("Who are you?");
        }
    }
}
