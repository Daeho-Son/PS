import java.util.*;

public class Main11561 {

	private static long answer = 1L;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int t = sc.nextInt();
		for (int i = 0; i < t; i++) {
			long n = sc.nextLong();
			answer = 1L;
			binarySearch(n, 0L, (long) Math.sqrt(2 * n));
			System.out.println(answer);
		}
	}

	private static void binarySearch(long n, long left, long right) {
		if (left > right) {
			return;
		}
		long middle = (left + right) / 2;
		if ((middle * (middle + 1)) / 2 > n) {
			binarySearch(n, 0L, middle - 1);
		} else {
			answer = Math.max(answer, middle);
			binarySearch(n, middle + 1, right);
		}
	}
}