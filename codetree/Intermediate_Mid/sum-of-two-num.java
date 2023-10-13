// [Codetree] Sum of Two Num
// 소요 시간 : 40분

import java.util.Scanner;
import java.util.HashMap;

public class Main {
    public static int answer = 0;
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int k =sc.nextInt();
        HashMap<Integer, Integer> numbers = new HashMap<>();

        for (int i = 0; i < n; i++) {
            int number = sc.nextInt();
            numbers.put(number, numbers.getOrDefault(number, 0) + 1);
        }

        numbers.forEach((key, value) -> {
            if (numbers.containsKey(k - key)) {
                if (key == k - key) {
                    answer += value * (value - 1);
                } else {
                    answer += value * numbers.get(k - key);
                }
            }
        });
        
        System.out.println(answer / 2);
    }
}