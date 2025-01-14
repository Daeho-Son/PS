import java.util.*;
import java.io.*;

public class Main18352 {

	private static List<Integer> listAnswer = new ArrayList<>();

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		Scanner sc = new Scanner(System.in);

		StringTokenizer st = new StringTokenizer(br.readLine());
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		int K = Integer.parseInt(st.nextToken());
		int X = Integer.parseInt(st.nextToken());

		Map<Integer, List<Integer>> graph = new HashMap();
		for (int i = 0; i < M; i++) {
			st = new StringTokenizer(br.readLine());
			int u = Integer.parseInt(st.nextToken());
			int v = Integer.parseInt(st.nextToken());
			graph.computeIfAbsent(u, k -> new ArrayList<>()).add(v);
		}

		boolean[] visited = new boolean[N + 1];
		int[] distance = new int[N + 1];
		bfs(graph, visited, distance, X, K);
		if (listAnswer.size() == 0) {
			System.out.println(-1);
		} else {
			Collections.sort(listAnswer);
			for (int cityNumber : listAnswer) {
				System.out.println(cityNumber);
			}
		}
	}

	private static void bfs(Map<Integer, List<Integer>> graph, boolean[] visited, int[] distance, int X, int K) {
		Queue<Integer> queue = new LinkedList<>();
		queue.offer(X);
		visited[X] = true;

		while (!queue.isEmpty()) {
			int current = queue.poll();
			if (distance[current] == K) {
				listAnswer.add(current);
			}
			if (!graph.containsKey(current)) {
				continue;
			}
			for (int to : graph.get(current)) {
				if (visited[to]) {
					continue;
				}
				visited[to] = true;
				distance[to] = distance[current] + 1;
				queue.offer(to);
			}
		}
	}
}