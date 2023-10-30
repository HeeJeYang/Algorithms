import java.util.*;
import java.io.*;

public class Main {
    public static StringTokenizer st;
    public static int F, S, G, U, D;
    public static boolean[] visited;
	public static void main(String args[]) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        st = br.readLine();
        F = Integer.parseInt(st.nextToken());
        S = Integer.parseInt(st.nextToken());
        G = Integer.parseInt(st.nextToken());
        U = Integer.parseInt(st.nextToken());
        D = Integer.parseInt(st.nextToken());
        visited = new boolean[F + 1];
        visited[0] = true;
        visited[S] = true;

        System.out.println(bfs());
	}

    public static String bfs() {
        Queue<Integer[]> q = new LinkedList<>();
        q.add({S, 0});

        while (!q.isEmpty()) {
            Integer[] qArr = q.poll();
            int floor = qArr[0];
            int cnt = qArr[1];

            if (cnt == G) {
                return cnt.toString();
            }

            int[] dFloors = new int[] {floor + U, floor - D};
            for (int dFloor: nFloors) {
                if (0 < dFloor <= F && !visited[dFloor]) {
                    visited[dFloor] = true;
                    q.add({dFloor, cnt + 1});
                }
            }
        }

        return "use the stairs";
    }
}