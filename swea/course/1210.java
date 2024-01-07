// 1210. [S/W 문제해결 기본] 2일차 - Ladder1

package swea.course;

import java.util.*;
import java.io.*;

class Solution {
    public static int y, x;
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
                    if (matrix[i][j] == 2) {
                        y = i;
                        x = j;
                    }
                }
            }

            move();
            sb.append(x).append("\n");
        }

        System.out.println(sb);
    }

    public static void move() {
        while (y > 0) {
            if (x > 0 && matrix[y][x - 1] == 1) {
                moveHorizon(-1);
            } else if (x < 99 && matrix[y][x + 1] == 1) {
                moveHorizon(1);
            } else {
                y -= 1;
            }
        }
    }

    public static void moveHorizon(int pos) {
        while (x + pos >= 0 && x + pos < 100 && matrix[y][x + pos] == 1) {
            x += pos;
        }

        y -= 1;
    }
}
