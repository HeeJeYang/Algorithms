import java.util.*;
import java.io.*;

public class Main {
    public static final int MAX_N = 1000;
    public static HashMap<Integer, Integer> numbers = new HashMap<>();
    public static int[] arr = new int[MAX_N];
    public static StringTokenizer st;
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        int ans = 0;

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
            numbers.put(arr[i], numbers.getOrDefault(arr[i], 0) + 1);
        }

        for (int i = 0; i < n; i++) {
            if (!numbers.containsKey(arr[i])) {
                numbers.put(arr[i], -1);
            } else {
                numbers.put(arr[i], numbers.get(arr[i]) - 1);
            }

            for (int j = 0; j < i; j++) {
                if (numbers.containsKey(k - arr[i] - arr[j])) {
                    ans += numbers.get(k - arr[i] - arr[j]);
                }
            }
        }

        System.out.println(ans);
    }
}