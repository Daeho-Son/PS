import java.util.*;
import java.io.*;

public class Main25195 {

	private static String answer = "Yes";

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		StringTokenizer st = new StringTokenizer(br.readLine());
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());

		Map<Integer, List<Integer>> graph = new HashMap<>();
		for (int i = 0; i < M; i++) {
			st = new StringTokenizer(br.readLine());
			int u = Integer.parseInt(st.nextToken());
			int v = Integer.parseInt(st.nextToken());
			graph.computeIfAbsent(u, k -> new ArrayList<>()).add(v);
		}

		int S = Integer.parseInt(br.readLine());
		boolean[] gomgoms = new boolean[N + 1];
		st = new StringTokenizer(br.readLine());
		for (int i = 0; i < S; i++) {
			gomgoms[Integer.parseInt(st.nextToken())] = true;
		}
		dfs(graph, 1, gomgoms, false);
		System.out.println(answer);
	}

	private static void dfs(Map<Integer, List<Integer>> graph, int current, boolean[] gomgoms, boolean meet) {
		if (gomgoms[current]) {
			return;
		}
		if (!graph.containsKey(current)) {
			if (meet == false) {
				answer = "yes";
			}
			return;
		}
		for (int n : graph.get(current)) {
			dfs(graph, n, gomgoms, meet);
		}
	}
}