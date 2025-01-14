import java.util.*;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int N =  sc.nextInt();

		int[] scores = new int[N];
		for (int i = 0; i < N; i++) {
			scores[i] = sc.nextInt();
		}

		int answer = 0;
		for (int i = N - 2; i >= 0; i--) {
			int diff = 0;
			if (scores[i] >= scores[i + 1]) {
				diff = scores[i] - scores[i + 1] + 1;
			}
			answer += diff;
			scores[i] -= diff;
		}
		System.out.println(answer);
	}
}