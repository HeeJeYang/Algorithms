// 1217. [S/W 문제해결 기본] 4일차 - 거듭 제곱

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
            st = new StringTokenizer(br.readLine());
            int N = Integer.parseInt(st.nextToken());
            int M = Integer.parseInt(st.nextToken());

            sb.append(power(N, M, 1)).append("\n");
        }

        System.out.println(sb);
    }

    public static int power(int N, int M, int total) {
        if (M == 0) return total;

        return power(N, M - 1, total * N);
    }
}
