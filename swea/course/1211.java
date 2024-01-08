// 1211. [S/W 문제해결 기본] 2일차 - Ladder2

package swea.course;

import java.util.*;
import java.io.*;

class Solution {
    public static int y = 0;
    public static int x = 0;
    public static int[][] matrix;
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        StringTokenizer st;

        for (int tc = 0; tc < 10; tc++) {
            int tcNum = Integer.parseInt(br.readLine());
            sb.append("#").append(tcNum).append(" ");

            matrix = new int[100][100];

            for (int i = 0; i < 100; i++) {
                st = new StringTokenizer(br.readLine());

                for (int j = 0; j < 100; j++) {
                    matrix[i][j] = Integer.parseInt(st.nextToken());
                }
            }

            int minStep = 10000;
            int answer = -1;
            for (int i = 0; i < 100; i++) {
                if (matrix[y][i] == 1) {
                    x = i;
                    int step = move();
                    if (minStep >= step) {
                        minStep = step;
                        answer = i;
                    }
                    
                    y = 0;
                }
            }

            sb.append(answer).append("\n");
        }

        System.out.println(sb);
    }

    public static int move() {
        int step = 0;

        while (y < 99) {
            if (x > 0 && matrix[y][x - 1] == 1) {
                step += moveHorizon(-1);
            } else if (x < 99 && matrix[y][x + 1] == 1) {
                step += moveHorizon(1);
            } else {
                y += 1;
                step += 1;
            }
        }
        return step;
    }

    public static int moveHorizon(int pos) {
        int step = 0;

        while (x + pos >= 0 && x + pos < 100 && matrix[y][x + pos] == 1) {
            x += pos;
            step += 1;
        }

        y += 1;
        return step + 1;
    }
}
