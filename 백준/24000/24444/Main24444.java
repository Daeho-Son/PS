import java.util.*;

public class Main24444 {

	private static int N;
	private static int M;
	private static int R;
	private static Map<Integer, List<Integer>> map;
	private static int[] orders;
	private static int orderIndex = 0;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		N = sc.nextInt();
		M = sc.nextInt();
		R = sc.nextInt();

		map = new HashMap<>();
		orders = new int[N + 1];

		for (int i = 0; i < M; i++) {
			int u = sc.nextInt();
			int v = sc.nextInt();
			map.putIfAbsent(u, new ArrayList<>());
			map.putIfAbsent(v, new ArrayList<>());
			map.get(v).add(u);
			map.get(u).add(v);
		}
		bfs(R);
		for (int i = 1; i <= N; i++) {
			System.out.println(orders[i]);
		}
	}

	private static void bfs(int R) {
		boolean[] visited = new boolean[N + 1];
		Queue<Integer> queue = new LinkedList<>();
		queue.offer(R);
		visited[R] = true;
		orders[R] = ++orderIndex;
		while (!queue.isEmpty()) {
			int target = queue.poll();
			List<Integer> linked = map.get(target);
			Collections.sort(linked);
			for (int i = 0; i < linked.size(); i++) {
				if (visited[linked.get(i)]) {
					continue;
				}
				queue.offer(linked.get(i));
				visited[linked.get(i)] = true;
				orders[linked.get(i)] = ++orderIndex;
			}
		}
	}
}