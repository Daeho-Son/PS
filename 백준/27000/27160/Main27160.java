import java.util.*;

public class Main27160 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		Map<String, Integer> countByCard = new HashMap<>() {{
			put("STRAWBERRY", 0);
			put("BANANA", 0);
			put("LIME", 0);
			put("PLUM", 0);
		}};

		int N = sc.nextInt();

		for (int i = 0; i < N; i++) {
			String card = sc.next();
			int count = sc.nextInt();
			countByCard.merge(card, count, Integer::sum);
		}

		String answer = "NO";
		for (Map.Entry<String, Integer> entry : countByCard.entrySet()) {
			if (entry.getValue() == 5) {
				answer = "YES";
			}
		}
		System.out.println(answer);
	}
}