import java.util.*;

public class Main {

    private static long[][] dp = null;
    private static final int MOD = 1000000000;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int K = sc.nextInt();

        dp = new long[K + 1][N + 1];
        f(K, N);
        System.out.println(dp[K][N]);
    }

    private static long f(int k, int n) {
        if (k == 1 || n == 0) {
            dp[k][n] = 1;
            return dp[k][n];
        }
        if (dp[k][n] != 0) {
            return dp[k][n];
        }
        dp[k][n] = (f(k - 1, n) + f(k, n - 1)) % MOD;
        return dp[k][n];
    }
}