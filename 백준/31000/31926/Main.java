import java.util.*;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int N = sc.nextInt();
		System.out.println(8 + log2(N) + 2);
	}

	private static int log2(int n) {
		return (int)(Math.log(n) / Math.log(2));
	}
}