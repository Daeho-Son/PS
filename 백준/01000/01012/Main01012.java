import java.util.*;

public class Main01012 {

	private static int[] dr = {0, -1, 0, 1};
	private static int[] dc = {-1, 0, 1, 0};

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int testcase = sc.nextInt();

		for (int t = 0; t < testcase; t++) {
			int column = sc.nextInt();
			int row = sc.nextInt();
			int countOfCabbage = sc.nextInt();
			boolean[][] arr2d = new boolean[row][column];
			for (int k = 0; k < countOfCabbage; k++) {
				int c = sc.nextInt();
				int r = sc.nextInt();
				arr2d[r][c] = true;
			}
			int answer = calculate(arr2d);
			System.out.println(answer);
		}
	}

	private static int calculate(boolean[][] arr2d) {
		int result = 0;
		int row = arr2d.length;
		int column = arr2d[0].length;
		boolean[][] visited = new boolean[row][column];
		for (int r = 0; r < row; r++) {
			for (int c = 0; c < column; c++) {
				if (visited[r][c] || !arr2d[r][c]) {
					continue;
				}
				search(arr2d, visited, r, c);
				result++;
			}
		}
		return result;
	}

	private static void search(boolean[][] arr2d, boolean[][] visited, int r, int c) {
		visited[r][c] = true;
		for (int i = 0; i < dr.length; i++) {
			int nr = r + dr[i];
			int nc = c + dc[i];
			if (!valid(arr2d.length, arr2d[0].length, nr, nc)) {
				continue;
			}
			if (!visited[nr][nc] && arr2d[nr][nc]) {
				search(arr2d, visited, nr, nc);
			}
		}
	}

	private static boolean valid(int row, int column, int nr, int nc) {
		if (nr < 0 || nc < 0 || nr >= row || nc >= column) {
			return false;
		}
		return true;
	}
}