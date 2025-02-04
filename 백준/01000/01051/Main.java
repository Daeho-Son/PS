import java.util.*;
import java.io.*;

public class Main {

    private static int N = 0;
    private static int M = 0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        int[][] arr2d = new int[N][M];
        for (int r = 0; r < N; r++) {
            String s = br.readLine();
            for (int c = 0; c < M; c++) {
                arr2d[r][c] = s.charAt(c) - '0';
            }
        }

        int answer = 1;
        int maxSize = Math.min(N, M);
        for (int r = 0; r < N; r++) {
            for (int c = 0; c < M; c++) {
                answer = Math.max(answer, getSquareCount(arr2d, r, c));
            }
        }
        System.out.println(answer);
    }

    public static int getSquareCount(int[][] arr2d, int r, int c) {
        int maxSquareSize = 1;
        int size = 1;
        while (true) {
            int nr = r + size;
            int nc = c + size;
            if (nr >= N || nc >= M) {
                break;
            }
            if (arr2d[r][c] == arr2d[r][nc] && arr2d[r][nc] == arr2d[nr][c] && arr2d[nr][c] == arr2d[nr][nc]) {
                maxSquareSize = Math.max(maxSquareSize, (int) Math.pow(size + 1, 2));
            }
            size++;
        }
        return maxSquareSize;
    }
}