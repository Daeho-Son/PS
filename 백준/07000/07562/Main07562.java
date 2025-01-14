import java.util.*;

class Coordinate {
	int x;
	int y;

	Coordinate(int x, int y) {
		this.x = x;
		this.y = y;
	}

	boolean isSamePosition(Coordinate coordinate) {
		if (this.x == coordinate.x && this.y == coordinate.y) {
			return true;
		}
		return false;
	}
}

public class Main07562 {
	private static int[] dx = new int[] {1, 2, 2, 1, -1, -2, -2, -1};
	private static int[] dy = new int[] {-2, -1, 1, 2, 2, 1, -1, -2};

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int numberOfTestCase = sc.nextInt();
		for (int t = 0; t < numberOfTestCase; t++) {
			int boardSize = sc.nextInt();
			int[][] board = new int[boardSize][boardSize];
			boolean[][] visited = new boolean[boardSize][boardSize];

			int fromX = sc.nextInt();
			int fromY = sc.nextInt();
			Coordinate from = new Coordinate(fromX, fromY);
			int toX = sc.nextInt();
			int toY = sc.nextInt();
			Coordinate to = new Coordinate(toX, toY);
			int answer = bfs(board, boardSize, visited, from, to);
			System.out.println(answer);
		}
	}

	private static int bfs(int[][] board, int boardSize, boolean[][] visited, Coordinate from, Coordinate to) {
		Queue<Coordinate> queue = new LinkedList<>();
		queue.offer(from);
		visited[from.y][from.x] = true;

		while (!queue.isEmpty()) {
			Coordinate current = queue.poll();
			int movedCount = board[current.y][current.x];
			if (current.y == to.y && current.x == to.x) {
				break;
			}
			for (int i = 0; i < 8; i++) {
				int nx = current.x + dx[i];
				int ny = current.y + dy[i];
				if (!isValid(boardSize, nx, ny) || visited[ny][nx]) {
					continue;
				}
				visited[ny][nx] = true;
				board[ny][nx] = movedCount + 1;
				queue.offer(new Coordinate(nx, ny));
			}
		}
		return board[to.y][to.x];
	}

	private static boolean isValid(int maxSize, int x, int y) {
		if (x < 0 || y < 0) {
			return false;
		}
		if (x >= maxSize || y >= maxSize) {
			return false;
		}
		return true;
	}
}