import java.util.*;

public class Main25593 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int N = sc.nextInt();

		int min = Integer.MAX_VALUE;
		int max = Integer.MIN_VALUE;
		Map<String, Integer> workTimeByWorker = new HashMap<>();
		for (int week = 0; week < N; week++) {
			for (int timeTable = 0; timeTable < 4; timeTable++) {
				/**
				 * 0: 08:00 ~ 12:00
				 * 1: 12:00 ~ 18:00
				 * 2: 18:00 ~ 22:00
				 * 3: 22:00 ~ 08:00
				 */
				for (int day = 0; day < 7; day++) {
					String worker = sc.next();
					if (worker.equals("-")) {
						continue;
					}
					if (timeTable == 0) {
						workTimeByWorker.merge(worker, 4, Integer::sum);
					} else if (timeTable == 1) {
						workTimeByWorker.merge(worker, 6, Integer::sum);
					} else if (timeTable == 2) {
						workTimeByWorker.merge(worker, 4, Integer::sum);
					} else {
						workTimeByWorker.merge(worker, 10, Integer::sum);
					}
				}
			}
		}
		if (workTimeByWorker.size() == 0) {
			System.out.println("Yes");
			return;
		}
		for (Map.Entry<String, Integer> entry : workTimeByWorker.entrySet()) {
			max = Math.max(max, entry.getValue());
			min = Math.min(min, entry.getValue());
		}
		if (max - min <= 12) {
			System.out.println("Yes");
		} else {
			System.out.println("No");
		}
	}
}