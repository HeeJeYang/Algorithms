// [BOJ] 6131. 완전 제곱수
// 실행 시간 : 132 ms
// 메모리 : 14176 KB

import java.io.*;

// public 붙일 것
class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        int N = Integer.parseInt(br.readLine());
        int answer = 0;

        for (int B = 1; B <= 499; B++) {
            for (int A = B + 1; A <= 500; A++) {
                if (Math.pow(A, 2) - N == Math.pow(B, 2)) {
                    answer += 1;
                }
            }
        }

        System.out.println(answer);
    }
}
