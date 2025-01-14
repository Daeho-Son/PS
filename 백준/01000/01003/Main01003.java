import java.util.*;

public class Main01003 {

	private static int[] dp = new int[41];
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		dp[0] = 0;
		dp[1] = 1;
		int t = sc.nextInt();
		for (int i = 0; i < t; i++) {
			int n = sc.nextInt();
			if (n == 0) {
				System.out.println(1 + " " + 0);
				continue;
			}
			fibonacci(n);
			System.out.println(dp[n - 1] + " " + dp[n]);
		}
	}

	private static int fibonacci(int n) {
		if (n == 0 || n == 1) {
			return n;
		}
		if (dp[n] != 0) {
			return dp[n];
		}
		dp[n] = fibonacci(n - 1) + fibonacci(n - 2);
		return dp[n];
	}
}