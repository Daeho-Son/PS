import java.math.BigDecimal;
import java.util.*;

public class Main01072 {

	private static int answer = 0;
	private static int x;
	private static int y;
	private static int z;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		x = sc.nextInt();
		y = sc.nextInt();
		z = getWinRate(x, y);

		if (getWinRate(x, y) == getWinRate(x + x, y + x)) {
			System.out.println(-1);
			return;
		}
		binarySearch(0, x);
		System.out.println(answer);
	}

	private static void binarySearch(int start, int end) {
		if (start == end) {
			answer = start;
			return;
		}
		int middle = (start + end) / 2;
		if (getWinRate(x + middle, y + middle) == z) {
			binarySearch(middle + 1, end);
		} else {
			binarySearch(start, middle);
		}
	}

	private static int getWinRate(int countTotalGame, int countWinGame) {
		return (int) (((long) countWinGame * 100) / (long) countTotalGame);
	}
}