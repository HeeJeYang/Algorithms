// [Codetree] Corresponding Numbers and Characters
// 소요 시간 : 20분

import java.util.Scanner;
import java.util.HashMap;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int n = sc.nextInt();
        int m = sc.nextInt();
        HashMap<String, String> numToStr = new HashMap<>();
        HashMap<String, String> strToNum = new HashMap<>();

        for (int i = 1; i <= n; i++) {
            String word = sc.next();
            numToStr.put(Integer.toString(i), word);
            strToNum.put(word, Integer.toString(i));
        }

        for (int i = 0; i < m; i++) {
            String target = sc.next();
            if (numToStr.containsKey(target)) {
                System.out.println(numToStr.get(target));
            } else {
                System.out.println(strToNum.get(target));
            }
        }
    }
}