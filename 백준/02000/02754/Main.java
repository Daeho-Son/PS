import java.util.*;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		Map<String, Float> score = new HashMap<>() {{
			put("A+", 4.3F);
			put("A0", 4.0F);
			put("A-", 3.7F);
			put("B+", 3.3F);
			put("B0", 3.0F);
			put("B-", 2.7F);
			put("C+", 2.3F);
			put("C0", 2.0F);
			put("C-", 1.7F);
			put("D+", 1.3F);
			put("D0", 1.0F);
			put("D-", 0.7F);
			put("F", 0.0F);
		}};

		String str = sc.next();
		System.out.println(score.get(str));
	}
}