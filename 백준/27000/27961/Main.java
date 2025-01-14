import java.util.*;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		long N = sc.nextLong();

		if (N == 0) {
			System.out.println(0);
		} else {
			int answer = 1;
			while (N > 1) {
				N = (N + 1) / 2;
				answer++;
			}
			System.out.println(answer);
		}
	}
}