import java.util.*;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

        long N = sc.nextLong();

        if (N == 0 || N == 1) {
            System.out.println(N);
            return;
        }
        int count = 0;
        while (N > 1) {
            N = (N + 1) / 2;
            count++;
        }
        System.out.println(count + 1);
	}
}