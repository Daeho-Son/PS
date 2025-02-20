import java.util.*;
import java.io.*;

public class Main {
    private static final BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    private static final int[] dp = new int[41];
    private static final int[] oneCounts = new int[41];
    private static final int[] zeroCounts = new int[41];

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        dp[1] = 1;
        zeroCounts[0] = 1;
        zeroCounts[1] = 0;
        oneCounts[1] = 1;
        int T = Integer.parseInt(br.readLine());
        for (int step = 0; step < T; step++) {
            int N = Integer.parseInt(br.readLine());
            runTest(N);
        }
        bw.flush();
        br.close();
        bw.close();
    }

    private static void runTest(int N) throws IOException {
        if (N == 0) {
            bw.write(1 + " " + 0 + "\n");
            return;
        }
        if (dp[N] != 0) {
            bw.write(zeroCounts[N] + " " + oneCounts[N] + "\n");
            return;
        }
        fibonacci(N);
        bw.write(zeroCounts[N] + " " + oneCounts[N] + "\n");
    }

    private static int fibonacci(int N) {
        if (N <= 0) {
            return 0;
        }
        if (dp[N] != 0) {
            return dp[N];
        }
        dp[N] = fibonacci(N - 1) + fibonacci(N - 2);
        oneCounts[N] = oneCounts[N - 1] + oneCounts[N - 2];
        zeroCounts[N] = zeroCounts[N - 1] + zeroCounts[N - 2];
        return dp[N];
    }
}