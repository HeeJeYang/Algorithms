// [BOJ] 14718. 용감한 용사 진수
// 실행 시간 : 00 ms
// 메모리 : 00 KB

import java.util.*;
import java.io.*;

class Solution {
    public static int N, K;
    public static int[][] enemy_status;
    public static int[] status;
    public static int answer = 3000000;
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());
        enemy_status = new int[3][N];
        status = new int[3];

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            enemy_status[0][i] = Integer.parseInt(st.nextToken());
            enemy_status[1][i] = Integer.parseInt(st.nextToken());
            enemy_status[2][i] = Integer.parseInt(st.nextToken());
        }

        dfs(0);

        System.out.println(answer);
    }

    public static void dfs(int cnt) {
        if (cnt == 3) {
            if (fight() >= K) {
                answer = Math.min(answer, status[0] + status[1] + status[2]);
            }
            return;
        }

        for (int i = 0; i < N; i++) {
            status[cnt] = enemy_status[cnt][i];
            dfs(cnt + 1);
        }
    }

    public static int fight() {
        int win_cnt = 0;
        for (int i = 0; i < N; i++) {
            boolean flag = true;
            for (int j = 0; j < 3; j++) {
                if (status[j] < enemy_status[j][i]) {
                    flag = false;
                    break;
                }
            }

            if (flag) {
                win_cnt += 1;
            }
        }

        return win_cnt;
    }
}