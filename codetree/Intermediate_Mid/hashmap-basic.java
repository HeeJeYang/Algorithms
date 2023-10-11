// [Codetree] Hashmap Basic
// 소요 시간 : 30분

import java.util.Scanner;
import java.util.HashMap;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        HashMap<Integer, Integer> storage = new HashMap<>();
        int n = sc.nextInt();

        for (int i = 0; i < n; i++) {
            String command = sc.next();
            int a = sc.nextInt();
            switch (command) {
                case "add":
                    int b = sc.nextInt();
                    storage.put(a, b);
                    break;
                case "remove":
                    storage.remove(a);
                    break;
                case "find":
                    if (storage.containsKey(a)) {
                        System.out.println(storage.get(a));
                    } else {
                    System.out.println("None");
                    }
                    break;
            }
        }
    }
}