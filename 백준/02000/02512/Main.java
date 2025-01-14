import java.util.*;

public class Main {

	private static int N = 0;			// N: 지방의 수
	private static int[] arr = null;	// arr: 각 지방의 예산요청
	private static int M = 0;			// M: 총 예산

	private static int answer = 0;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		N = sc.nextInt();
		arr = new int[N];
		int sum = 0;
		int max = 0;
		for (int i = 0; i < N; i++) {
			arr[i] = sc.nextInt();
			sum += arr[i];
			max = Math.max(max, arr[i]);
		}
		M = sc.nextInt();

		if (sum <= M) {
			System.out.println(max);
		} else {
			binarySearch(0, M);
			System.out.println(answer);
		}
	}

	private static void binarySearch(int left, int right) {
		if (left > right) {
			return;
		}
		int middle = (left + right) / 2;
		int totalPrice = 0;
		for (int i = 0; i < N; i++) {
			totalPrice += Math.min(arr[i], middle);
		}
		if (totalPrice > M) {
			binarySearch(left, middle - 1);
		} else {
			answer = middle;
			binarySearch(middle + 1, right);
		}
	}
}