import com.sun.source.tree.Tree;

import java.io.*;
import java.util.*;

public class Main {
	private static StringTokenizer st = null;
	private static BufferedWriter bw = null;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		bw = new BufferedWriter(new OutputStreamWriter(System.out));

		st = new StringTokenizer(br.readLine());
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		int V = Integer.parseInt(st.nextToken());

		Map<Integer, Set<Integer>> map = new HashMap<>();
		map.putIfAbsent(V, new TreeSet<>());
		for (int i = 0; i < M; i++) {
			st = new StringTokenizer(br.readLine());
			int vx = Integer.parseInt(st.nextToken());
			int vy = Integer.parseInt(st.nextToken());
			map.computeIfAbsent(vx, k -> new TreeSet<>()).add(vy);
			map.computeIfAbsent(vy, k -> new TreeSet<>()).add(vx);

		}

		Set<Integer> visited = new HashSet<>(){};
		visited.add(V);
		bw.write(V + " ");
		dfs(map, visited, V);
		bw.write("\n");
		bfs(map, V);
		bw.write("\n");
		bw.flush();
	}

	private static void dfs(Map<Integer, Set<Integer>> map, Set<Integer> visited, int currentKey) throws IOException {
		if (visited.size() == map.keySet().size()) {
			return;
		}
		Set<Integer> values = map.get(currentKey);
		for (int value : values) {
			if (visited.contains(value)) {
				continue;
			}
			bw.write(value + " ");
			visited.add(value);
			dfs(map, visited, value);
		}
	}

	private static void bfs(Map<Integer, Set<Integer>> map, int startKey) throws IOException {
		Deque<Integer> deque = new ArrayDeque<>();
		deque.offerLast(startKey);
		Set<Integer> visited = new HashSet<>();
		while (!deque.isEmpty()) {
			int currentKey = deque.pollFirst();
			bw.write(currentKey + " ");
			visited.add(currentKey);
			Set<Integer> values = map.get(currentKey);
			for (int value : values) {
				if (visited.contains(value)) {
					continue;
				}
				if (deque.contains(value)) {
					continue;
				}
				deque.offerLast(value);
			}
		}
	}
}