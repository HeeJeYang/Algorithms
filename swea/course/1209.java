// 1209. [S/W 문제해결 기본] 2일차 - Sum

package swea.course;

import java.util.*;
import java.io.*;

class Solution {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        StringTokenizer st;

        
        for (int tc = 1; tc <= 10; tc++) {
            int tcNum = Integer.parseInt(br.readLine());
            sb.append("#").append(tcNum).append(" ");
            int[] sumRow = new int[100];
            int[] sumCol = new int[100];
            int diagon1 = 0;
            int diagon2 = 0;

            for (int i = 0; i < 100; i++) {
                st = new StringTokenizer(br.readLine());

                for (int j = 0; j < 100; j++) {
                    int num = Integer.parseInt(st.nextToken());
                    sumRow[i] += num;
                    sumCol[j] += num;

                    if (i == j) diagon1 += num;
                    if (i == 99 - j) diagon2 += num;
                }
            }

            int answer = Math.max(diagon1, diagon2);
            for (int i = 0; i < 100; i++) {
                answer = Math.max(answer, Math.max(sumRow[i], sumCol[i]));
            }

            sb.append(answer).append("\n");
        }
        
        System.out.println(sb);
    }
}