import java.util.*;

public class Main09933 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int N = sc.nextInt();

		Set<String> set = new HashSet<>();
		for (int i = 0; i < N; i++) {
			set.add(sc.next());
		}
		StringBuilder answer = new StringBuilder();
		for (String s : set) {
			StringBuilder sb = new StringBuilder(s);
			sb.reverse();
			if (set.contains(sb.toString())) {
				answer.append(s.length() + " " + sb.charAt(s.length() / 2));
				break;
			}
		}
		System.out.println(answer);
	}
}