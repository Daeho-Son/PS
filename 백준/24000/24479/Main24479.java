import java.util.*;

public class Main24479 {

	private static Map<Integer, Set<Integer>> map;
	private static int[] visitedOrders;
	private static int order = 0;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int N = sc.nextInt();
		int M = sc.nextInt();
		int R = sc.nextInt();

		map = new HashMap<>();
		visitedOrders = new int[N + 1];

		for (int e = 1; e <= N; e++) {
			map.putIfAbsent(e, new HashSet<>());
		}
		for (int i = 0; i < M; i++) {
			int u = sc.nextInt();
			int v = sc.nextInt();
			map.get(u).add(v);
			map.get(v).add(u);
		}
		dfs(R);
		for (int edge = 1; edge <= N; edge++) {
			System.out.println(visitedOrders[edge]);
		}
	}

	private static void dfs(int R) {
		visitedOrders[R] = ++order;
		List<Integer> values = new ArrayList<>(map.get(R));
		if (values.size() == 0) {
			return;
		}
		Collections.sort(values);
		for (int value : values) {
			if (visitedOrders[value] != 0) {
				continue;
			}
			dfs(value);
		}
	}
}