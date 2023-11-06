// [BOJ] 17471. 게리맨더링
// 실행 시간 :  ms
// 메모리 :  KB

import java.util.*;
import java.io.*;

class Main {
	public static int N;
	public static int[] population;
	public static ArrayList<Integer>[] adjList;
    public static StringTokenizer st;
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        st = new StringTokenizer(st.nextToken());
        N = Integer.parseInt(st.nextToken());
        adjList = new ArrayList[N];
        for (int i = 0; i <= N; i++) {
        	adjList[i] = new ArrayList<>();
        }

        st = new StringTokenizer(st.nextToken());
        population = new int[N];
        for (int i = 0; i < N; i++) {
        	population[i] = Integer.parseInt(st.nextToken());
        }
        
        
    }
}