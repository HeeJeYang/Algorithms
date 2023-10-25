// [Codetree] Lowest Points
// 소요 시간 : 20분

import java.util.*;
import java.io.*;

public class Main {
    public static StringTokenizer st;
    public static long answer = 0;
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        HashMap<Integer, Integer> positions = new HashMap<>();
        st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            if (positions.containsKey(x)) {
                positions.put(x, Math.min(positions.get(x), y));
            } else {
                positions.put(x, y);
            }
        }

        positions.forEach((key, value) -> {
            answer += value;
        });

        System.out.println(answer);
    }
}