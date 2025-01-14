import java.util.*;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int n = sc.nextInt();
		Map<String, Boolean> entranceStatus = new HashMap<>();
		for (int i = 0; i < n; i++) {
			String name = sc.next();
			String status = sc.next();
			if (status.equals("enter")) {
				entranceStatus.put(name, true);
			} else {
				entranceStatus.put(name, false);
			}
		}

		List<String> answer = new ArrayList<>();
		for (Map.Entry<String, Boolean> entry : entranceStatus.entrySet()) {
			if (entry.getValue()) {
				answer.add(entry.getKey());
			}
		}

		Collections.sort(answer, Comparator.reverseOrder());
		for (String name : answer) {
			System.out.println(name);
		}
	}
}