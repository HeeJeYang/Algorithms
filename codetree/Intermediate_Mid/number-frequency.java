// [Codetree] number-frequency
// 소요 시간: 15분

import java.util.Scanner;
import java.util.HashMap;

public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        HashMap<Integer, Integer> numbers = new HashMap<>();

        for (int i = 0; i < n; i++) {
            int number = sc.nextInt();
            numbers.put(number, numbers.getOrDefault(number, 0) + 1);
        }

        for (int i = 0; i < m; i++) {
            int target = sc.nextInt();
            System.out.print(numbers.getOrDefault(target, 0) + " ");
        }
    }
}