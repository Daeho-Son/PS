import java.util.*;

public class Main01260 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int n = sc.nextInt();
		int m = sc.nextInt();
		int v = sc.nextInt();

		Map<Integer, PriorityQueue<Integer>> edgeConnection = new HashMap<>();
		for (int i = 0; i < m; i++) {
			int startEdge = sc.nextInt();
			int endEdge = sc.nextInt();
			edgeConnection.putIfAbsent(startEdge, new PriorityQueue<>());
			edgeConnection.putIfAbsent(endEdge, new PriorityQueue<>());
			edgeConnection.get(startEdge).add(endEdge);
			edgeConnection.get(endEdge).add(startEdge);
		}

		dfs(edgeConnection, new HashSet<>(Arrays.asList(v)), v, n);
		System.out.println();
		bfs(edgeConnection, v);
	}

	private static void dfs(Map<Integer, PriorityQueue<Integer>> edgeConnection, Set<Integer> visited, int startEdge, int keyCount) {
		System.out.print(startEdge + " ");
		if (visited.size() == keyCount) {
			return;
		}
		if (!edgeConnection.containsKey(startEdge)) {
			return;
		}
		PriorityQueue<Integer> pq = new PriorityQueue<>(edgeConnection.get(startEdge));
		while (!pq.isEmpty()) {
			int edge = pq.poll();
			if (visited.contains(edge)) {
				continue;
			}
			visited.add(edge);
			dfs(edgeConnection, visited, edge, keyCount);
		}
	}

	private static void bfs(Map<Integer, PriorityQueue<Integer>> edgeConnection, int v) {
		Deque<Integer> queue = new ArrayDeque<>();
		queue.add(v);
		Set<Integer> visited = new HashSet<>();
		while (!queue.isEmpty()) {
			int startEdge = queue.poll();
			System.out.print(startEdge + " ");
			if (!edgeConnection.containsKey(startEdge)) {
				continue;
			}
			PriorityQueue<Integer> pq = new PriorityQueue<>(edgeConnection.get(startEdge));
			visited.add(startEdge);
			while (!pq.isEmpty()) {
				int edge = pq.poll();
				if (visited.contains(edge)) {
					continue;
				}
				visited.add(edge);
				queue.add(edge);
			}
		}
	}
}