import java.util.*;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int N = sc.nextInt();
		int answer = 1;
		while (N > 0) {
			answer *= N;
			N--;
		}
		System.out.println(answer);
	}
}