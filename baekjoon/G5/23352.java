package baekjoon.G5;

// [BOJ] 23352. 방탈출
// 실행 시간 : 576 ms
// 메모리 : 165700 KB

import java.util.*;
import java.io.*;

class Main {
	public static class Node {
		int y, x;
		
		Node(int y, int x) {
			this.y = y;
			this.x = x;
		}
	}
	public static int N, M;
	public static int[] answer = new int[] {1, 0};
	public static int[][] direction = new int[][] { {-1, 0}, {0, -1}, {1, 0}, {0, 1} };
	public static int[][] rooms;
	public static StringTokenizer st;
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		
		st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		rooms = new int[N][M];
		
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < M; j++) {
				rooms[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				if (rooms[i][j] != 0) {
					bfs(i, j);
				}
			}
		}
		
		System.out.println(answer[1]);
	}
	
	public static void bfs(int sy, int sx) {
		Queue<Node> q = new ArrayDeque<>();
		q.add(new Node(sy, sx));
		int[][] visited = new int[N][M];
		visited[sy][sx] = 1;
		
		while (!q.isEmpty()) {
			Node node = q.poll();
			
			for (int[] dir: direction) {
				int dy = node.y + dir[0];
				int dx = node.x + dir[1];
				
				if (dy < 0 || dy >= N || dx < 0 || dx >= M) continue;
				if (rooms[dy][dx] == 0 || visited[dy][dx] != 0) continue;
				visited[dy][dx] = visited[node.y][node.x] + 1;
				q.add(new Node(dy, dx));
			}
		}
		
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				if (answer[0] < visited[i][j]) {
					answer[0] = visited[i][j];
					answer[1] = rooms[i][j] + rooms[sy][sx];
				} else if (answer[0] == visited[i][j]) {
					answer[1] = Math.max(answer[1], rooms[i][j] + rooms[sy][sx]);
				}
			}
		}
	}
}
