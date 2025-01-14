import java.util.*;
import java.io.*;

public class Main02805 {

	private static int N;
	private static long M;
	private static long[] arr;
	private static long answer = 0;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		StringTokenizer st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken()); // 나무의 수
		M = Integer.parseInt(st.nextToken()); // 필요한 나무의 미터

		arr = new long[N];

		st = new StringTokenizer(br.readLine());
		for (int i = 0; i < N; i++) {
			arr[i] = Integer.parseInt(st.nextToken());
		}
		binarySearch(0, 1000000000);
		System.out.println(answer);
	}

	private static void binarySearch(long left, long right) {
		if (left > right) {
			return ;
		}
		long middle = (left + right) / 2;
		long sum = 0;
		for (int i = 0; i < N; i++) {
			if (middle >= arr[i]) {
				continue;
			}
			sum += arr[i] -  middle;
		}
		if (sum >= M) {
			answer = Math.max(answer, middle);
			binarySearch(middle + 1, right);
		} else {
			binarySearch(left, middle - 1);
		}
	}
}