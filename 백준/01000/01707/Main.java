import java.util.*;
import java.io.*;

public class Main {
    private static BufferedReader br = null;

    public static void main(String[] args) throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        int K = Integer.parseInt(br.readLine());
        for (int i = 0; i < K; i++) {
            System.out.println(runTest() ? "YES" : "NO");
        }
    }

    private static boolean runTest() throws IOException {
        StringTokenizer st = new StringTokenizer(br.readLine());
        int V = Integer.parseInt(st.nextToken());
        int E = Integer.parseInt(st.nextToken());
        Map<Integer, Set<Integer>> map = new HashMap<>();
        for (int i = 0; i < E; i++) {
            st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            map.computeIfAbsent(u, k -> new HashSet<>()).add(v);
            map.computeIfAbsent(v, k -> new HashSet<>()).add(u);
        }

        // 방문 여부 및 색상 배열 초기화
        int[] nodesColor = new int[V + 1];
        boolean[] isVisited = new boolean[V + 1];

        // 연결되지 않은 그래프의 모든 컴포넌트 체크
        for (int i = 1; i <= V; i++) {
            if (!isVisited[i]) {
                if (!isBipartite(map, i, nodesColor, isVisited)) {
                    return false;
                }
            }
        }
        return true;
    }

    private static boolean isBipartite(Map<Integer, Set<Integer>> map, int start, int[] nodesColor, boolean[] isVisited) {
        Deque<Integer> deque = new ArrayDeque<>();
        deque.offerLast(start);
        nodesColor[start] = 1;
        isVisited[start] = true;

        while (!deque.isEmpty()) {
            int u = deque.pollFirst();
            for (int v : map.getOrDefault(u, Collections.emptySet())) {
                if (!isVisited[v]) {
                    nodesColor[v] = -nodesColor[u];
                    isVisited[v] = true;
                    deque.offerLast(v);
                } else if (nodesColor[v] == nodesColor[u]) {
                    return false;
                }
            }
        }
        return true;
    }
}
