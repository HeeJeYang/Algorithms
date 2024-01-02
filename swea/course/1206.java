package swea.course;

import java.util.*;
import java.io.*;

class Solution {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        
        for (int tc = 1; tc <= 10; tc++) {
            int N = Integer.parseInt(br.readLine());
            int[] heights = new int[N];
            StringTokenizer st = new StringTokenizer(br.readLine());

            for (int i = 0; i < N; i++) {
                heights[i] = Integer.parseInt(st.nextToken());
            }

            int answer = 0;
            for (int i = 2; i < N - 2; i++) {
                int maxHeightBySide = Math.max(Math.max(heights[i - 2], heights[i - 1]), Math.max(heights[i + 1], heights[i + 2]));
                if (heights[i] > maxHeightBySide) {
                    answer += heights[i] - maxHeightBySide;
                }
            }

            sb.append("#" + tc + " ").append(answer).append("\n");
        }

        System.out.println(sb);
    }
}
