import java.util.*;

public class Main11047 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int N = sc.nextInt();
		int K = sc.nextInt();
		int[] coinValues = new int[N];

		for (int i = 0; i < N; i++) {
			coinValues[i] = sc.nextInt();
		}

		int answer = 0;
		for (int i = N - 1; i >= 0; i--) {
			answer += K / coinValues[i];
			K %= coinValues[i];
		}
		System.out.println(answer);
	}
}