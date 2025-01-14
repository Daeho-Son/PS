import java.util.*;

public class Main02644 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int n = sc.nextInt(); // 전체 사람의 수
		int a = sc.nextInt(); // 촌수를 계산해야하는 사람 A
		int b = sc.nextInt(); // 촌수를 계산해야하는 사람 B
		int m = sc.nextInt(); // 부모 자식들 간의 관계의 개수

		List<Integer>[] graph = new ArrayList[n + 1];
		for (int i = 0; i <= n; i++) {
			graph[i] = new ArrayList<>();
		}

		for (int i = 0; i < m; i++) {
			int x = sc.nextInt(); // y의 부모
			int y = sc.nextInt(); // x의 자식
			graph[y].add(x);
			graph[x].add(y);
		}
		int answer = bfs(graph, a, b);
		System.out.println(answer);
	}

	private static int bfs(List<Integer>[] graph, int start, int target) {
		boolean[] visited = new boolean[graph.length];
		Queue<Integer> queue = new LinkedList<>();
		int[] distance = new int[graph.length];

		queue.offer(start);
		visited[start] = true;
		while (!queue.isEmpty()) {
			int current = queue.poll();
			if (current == target) {
				return distance[current];
			}
			for (int neighbor : graph[current]) {
				if (visited[neighbor]) {
					continue;
				}
				queue.offer(neighbor);
				distance[neighbor] = distance[current] + 1;
				visited[neighbor] = true;
			}
		}
		return -1;
	}
}