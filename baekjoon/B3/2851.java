// [BOJ] 2851. 슈퍼 마리오
// 실행 시간 : 124 ms
// 메모리 : 14048 KB

import java.io.*;

// public 붙일 것
class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int sum_score = 0;
        int answer = 0;

        for (int i = 0; i < 10; i++) {
            sum_score += Integer.parseInt(br.readLine());
            
            if (Math.abs(100 - answer) > Math.abs(100 - sum_score)) {
                answer = sum_score;
            } else if (Math.abs(100 - answer) == Math.abs(100 - sum_score) && sum_score > answer) {
                answer = sum_score;
            }

        }
        System.out.println(answer);
    }
}
