// 1204. [S/W 문제해결 기본] 1일차 - 최빈수 구하기

package swea.course;

import java.util.*;
import java.io.*;

class Solution {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int T = Integer.parseInt(br.readLine());
        
        for (int i = 0; i < T; i++) {
            int tc = Integer.parseInt(br.readLine());
            StringTokenizer st = new StringTokenizer(br.readLine());
            int[] c = new int[101];

            for (int j = 0; j < 1000; j++) {
                int score = Integer.parseInt(st.nextToken());
                c[score] += 1;
            }

            int answer = 100;
            for (int score = 99; score >= 0; score--) {
                if (c[answer] < c[score]) {
                    answer = score;
                }
            }

            sb.append("#" + tc + " ").append(answer).append("\n");
        }

        System.out.println(sb);
    }
}