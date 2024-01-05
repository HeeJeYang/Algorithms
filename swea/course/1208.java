// 1208. [S/W 문제해결 기본] 1일차 - Flatten

package swea.course;

import java.util.*;
import java.io.*;

class Solution {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        for (int tc = 1; tc <= 10; tc++) {
            sb.append("#").append(tc).append(" ");
            int dump = Integer.parseInt(br.readLine());
            int[] heights = new int[101];
            
            StringTokenizer st = new StringTokenizer(br.readLine());
            int height = Integer.parseInt(st.nextToken());
            heights[height] += 1;

            int left = 1;
            int right = 100;

            while (heights[left] == 0) {
                left += 1;
            }
            while (heights[right] == 0) {
                right -= 1;
            }


            for (int i = 0; i < dump; i++) {
                heights[left] -= 1;
                heights[left + 1] += 1;
                while (left <= 100 && heights[left] == 0) {
                    left += 1;
                }
                
                heights[right] -= 1;
                heights[right - 1] += 1;
                while (right >= 1 && heights[right] == 0) {
                    right -= 1;
                }

                if (left == right) {
                    sb.append(0);
                    break;
                } else if (left > right) {
                    sb.append(1);
                    break;
                }
            }
            sb.append(right - left).append("\n");
        }

        System.out.println(sb);
    }
}
