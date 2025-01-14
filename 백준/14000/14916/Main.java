import java.util.*;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int n = sc.nextInt();

		int answer = 0;
		for (int fiveWon = n / 5; fiveWon >= 0; fiveWon--) {
			int remainderN = n - (5 * fiveWon);
			if (remainderN % 2 == 0) {
				answer = fiveWon + (remainderN / 2);
				break;
			}
		}
		if (answer == 0) {
			System.out.println(-1);
		} else {
			System.out.println(answer);
		}
	}
}