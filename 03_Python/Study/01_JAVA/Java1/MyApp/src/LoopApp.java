public class LoopApp {
    public static void main(String[] args) {
        System.out.println(1);

        int i = 0; // 반복문의 counting 을 위해 쓰는 변수
        while(i < 3){
            System.out.println(2);
            System.out.println(3);
            i++; // i = i + 1;
        }
        // 1, 초깃값 세팅 코드, 2. 반복을 더 해야하는지를 체크하는 boolean 값, 3. 반복이 진행될 때마다 실행되어야 하는 코드
        for(int k = 0; k < 3; k++) {
            System.out.println(4);
        }
    }
}
