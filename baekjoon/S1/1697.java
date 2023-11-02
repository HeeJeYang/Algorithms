package baekjoon.S1;

import java.util.*;
import java.io.*;

class Main {
    public static final int MAX_N = 100000;
    public static boolean[] v = new boolean[MAX_N + 1];
    public static int N, K;
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());
        v[N] = true;

        bfs();
    }

    public static void bfs() {
        Queue<int[]> q = new LinkedList<>();
        q.add(new int[] {N, 0});

        while (!q.isEmpty()) {
            int[] arr = q.poll();
            int dot = arr[0];
            int cnt = arr[1];

            if (dot == K) {
                System.out.println(cnt);
                return;
            }

            if (dot - 1 >= 0 && !v[dot - 1]) {
                v[dot - 1] = true;
                q.add(new int[] {dot - 1, cnt + 1});
            }

            if (dot + 1 <= MAX_N && !v[dot + 1]) {
                v[dot + 1] = true;
                q.add(new int[] {dot + 1, cnt + 1});
            }

            if (dot * 2 <= MAX_N && !v[dot * 2]) {
                v[dot * 2] = true;
                q.add(new int[] {dot * 2, cnt + 1});
            }
        }
    }
}
