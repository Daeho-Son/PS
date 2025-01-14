import java.util.*;
import java.io.*;

class Coordinate {
	int h;
	int r;
	int c;
	int grownDay;

	Coordinate(int h, int r, int c) {
		this.h = h;
		this.r = r;
		this.c = c;
		this.grownDay = 0;
	}

	Coordinate(int h, int r, int c, int grownDay) {
		this.h = h;
		this.r = r;
		this.c = c;
		this.grownDay = grownDay;
	}
}

public class Main {

	private static StringTokenizer st;

	private static final int DIRECTION_COUNT = 6;

	private static final int[] dh = new int[] {0, 0, 0, 0, 1, -1};
	private static final int[] dr = new int[] {-1, 0, 1, 0, 0, 0};
	private static final int[] dc = new int[] {0, 1, 0, -1, 0, 0};

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		st = new StringTokenizer(br.readLine());
		int M = Integer.parseInt(st.nextToken()); // column
		int N = Integer.parseInt(st.nextToken()); // row
		int H = Integer.parseInt(st.nextToken()); // height

		int[][][] arr3d = new int[H][N][M];
		Queue<Coordinate> grownTomatoes = new LinkedList<>();
		for (int h = 0; h < H; h++) {
			for (int r = 0; r < N; r++) {
				st = new StringTokenizer(br.readLine());
				for (int c = 0; c < M; c++) {
					int tomatoStatus = Integer.parseInt(st.nextToken());
					arr3d[h][r][c] = tomatoStatus;
					if (tomatoStatus == 1) {
						grownTomatoes.add(new Coordinate(h, r, c));
					}
				}
			}
		}

		int totalAllGrownDay = tomatoesGrownAndGetAllGrownDay(arr3d, grownTomatoes, H, N, M);
		if (hasNonGrownTomato(arr3d, H, N, M)) {
			System.out.println("-1");
		} else {
			System.out.println(totalAllGrownDay);
		}

	}

	private static boolean hasNonGrownTomato(int[][][] arr3d, int H, int N, int M) {
		for (int h = 0; h < H; h++) {
			for (int r = 0; r < N; r++) {
				for (int c = 0; c < M; c++) {
					if (arr3d[h][r][c] == 0) {
						return true;
					}
				}
			}
		}
		return false;
	}

	private static int tomatoesGrownAndGetAllGrownDay(int[][][] arr3d, Queue<Coordinate> grownTomatoes, int H, int N, int M) {
		int totalGrownDay = 0;

		while (!grownTomatoes.isEmpty()) {
			Coordinate current = grownTomatoes.poll();

			for (int d = 0; d < DIRECTION_COUNT; d++) { // 익은 토마토가 주변에 있는지 확인한다.
				int nh = current.h + dh[d];
				int nr = current.r + dr[d];
				int nc = current.c + dc[d];
				totalGrownDay = current.grownDay;
				if (!check(H, N, M, nh, nr, nc)) { // 유효한 좌표인가?
					continue;
				}
				if (arr3d[nh][nr][nc] == 0) { // 익은 토마토인가?
					grownTomatoes.add(new Coordinate(nh, nr, nc, current.grownDay + 1));
					arr3d[nh][nr][nc] = 1;
				}
			}
		}
		return totalGrownDay;
	}

	private static boolean check(int H, int N, int M, int h, int r, int c) {
		if (h < 0 || r < 0 || c < 0) {
			return false;
		}
		if (h >= H || r >= N || c >= M) {
			return false;
		}
		return true;
	}

	private static void print(int[][][] arr3d) {
		for (int h = 0; h < arr3d.length; h++) {
			for (int r = 0; r < arr3d[0].length; r++) {
				for (int c = 0; c < arr3d[0][0].length; c++) {
					System.out.print(arr3d[h][r][c] + " ");
				}
				System.out.println();
			}
			System.out.println();
		}
	}
}