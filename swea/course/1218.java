// 1218. [S/W 문제해결 기본] 4일차 - 괄호 짝짓기

package swea.course;

import java.util.*;
import java.io.*;

class Solution {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        HashMap<Character, Character> coupleBrackets = new HashMap<>();
        coupleBrackets.put(')', '(');
        coupleBrackets.put('}', '{');
        coupleBrackets.put(']', '[');
        coupleBrackets.put('>', '<');

        for (int tc = 1; tc <= 10; tc++) {
            sb.append("#").append(tc).append(" ");
            int N = Integer.parseInt(br.readLine());
            Stack<Character> s = new Stack<>();
            String brackets = br.readLine();
            for (int i = 0; i < N; i++) {
                char bracket = brackets.charAt(i);

                if (coupleBrackets.values().contains(bracket)) {
                    s.add(bracket);
                } else {
                    if (s.peek() == coupleBrackets.get(bracket)) {
                        s.pop();
                    } else {
                        break;
                    }
                }

            }

            if (s.isEmpty()) sb.append(1);
            else sb.append(0);
            sb.append("\n");
        }

        System.out.println(sb);
    }
}
