import java.util.*;

public class Main11399 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int N = sc.nextInt();
		int[] arr = new int[N];
		for (int i = 0; i < N; i++) {
			arr[i] = sc.nextInt();
		}

		Arrays.sort(arr);
		int answer = 0;
		int prev = 0;
		for (int i = 0; i < N; i++) {
			answer += prev + arr[i];
			prev = prev + arr[i];
		}
		System.out.println(answer);
	}
}
