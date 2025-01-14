import java.util.*;
import java.io.*;

class Pair {
	int r;
	int c;

	Pair(int r, int c) {
		this.r = r;
		this.c = c;
	}
}

public class Main02573 {

	private static StringTokenizer st;

	private static int[] dr = new int[]{0, 1, 0, -1};
	private static int[] dc = new int[]{-1, 0, 1, 0};


	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		st = new StringTokenizer(br.readLine());
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		int[][] arr2d = new int[N][M];
		for (int r = 0; r < N; r++) {
			st = new StringTokenizer(br.readLine());
			for (int c = 0; c < M; c++) {
				arr2d[r][c] = Integer.parseInt(st.nextToken());
			}
		}

		int answer = 0;
		for (int year = 1; year <= 10000; year++) {
			// 빙산 녹이면서 개수 세기
			int countIceberg = meltIcebergAndGetCountIceberg(arr2d, N, M);
			// 만약 빙산의 덩어리 개수가 2개 이상이면 종료
			if (countIceberg == 0) {
				break;
			}
			if (countIceberg >= 2) {
				answer = year - 1;
				break;
			}
		}
		System.out.println(answer);
	}

	private static void printMap(int[][] arr2d, int N, int M) {
		for (int r = 0; r < N; r++) {
			for (int c = 0; c < M; c++) {
				System.out.print(arr2d[r][c] + " ");
			}
			System.out.println();
		}
	}

	private static int meltIcebergAndGetCountIceberg(int[][] arr2d, int N, int M) {
		boolean[][] visited = new boolean[N][M];

		int count = 0;
		for (int r = 0; r < N; r++) {
			for (int c = 0; c < M; c++) {
				if (visited[r][c]) {
					continue;
				}
				if (arr2d[r][c] == 0) {
					continue;
				}
				bfs(arr2d, N, M, visited, new Pair(r, c));
				count++;
			}
		}
		return count;
	}

	private static boolean check(int[][] arr2d, int N, int M, int r, int c) {
		if (r < 0 || c < 0) {
			return false;
		}
		if (r >= N || c >= M) {
			return false;
		}
		return true;
	}

	private static void bfs(int[][] arr2d, int N, int M, boolean[][] visited, Pair start) {
		Queue<Pair> queue = new LinkedList<>();
		queue.offer(start);
		visited[start.r][start.c] = true;

		while (!queue.isEmpty()) {
			Pair current = queue.poll();

			for (int i = 0; i < 4; i++) {
				int nr = current.r + dr[i];
				int nc = current.c + dc[i];
				if (!check(arr2d, N, M, nr, nc)) {
					continue;
				}
				if (visited[nr][nc]) {
					continue;
				}
				if (!visited[nr][nc] && arr2d[nr][nc] == 0 && arr2d[current.r][current.c] > 0) {
					arr2d[current.r][current.c]--;
				}
				if (!visited[nr][nc] && arr2d[nr][nc] != 0) {
					queue.offer(new Pair(nr, nc));
					visited[nr][nc] = true;
				}
			}
		}
	}
}