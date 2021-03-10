public class ArrayApp {
    public static void main(String[] args) {
        // nathan, peter, smith
        // String users = "nathan, peter, smith"; // 너무 비효율적임 -> 배열을 사용하자.
        String[] users = new String[3]; // 담고자하는 배열의 크기를 지정함.
        users[0] = "nathan";
        users[1] = "peter";
        users[2] = "smith";

        System.out.println(users[1]);
        System.out.println(users.length); // 몇 개의 내용이 있단기보다는 크기가 얼마인 배열이다라고 생각

        int[] scores = {10, 100, 1000}; // 원소, Element
        System.out.println(scores[1]);
        System.out.println(scores.length);
    }
}
