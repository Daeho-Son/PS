import java.util.*;

public class Main {
    private static final int MAX_BOARD_SIZE = 19;
    private static final int[][] board = new int[MAX_BOARD_SIZE][MAX_BOARD_SIZE];
    private static final int[] dr = new int[]{-1, 0, 1, 1};
    private static final int[] dc = new int[]{1, 1, 1, 0};

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        for (int r = 0; r < MAX_BOARD_SIZE; r++) {
            for (int c = 0; c < MAX_BOARD_SIZE; c++) {
                board[r][c] = sc.nextInt();
            }
        }

        for (int r = 0; r < MAX_BOARD_SIZE; r++) {
            for (int c = 0; c < MAX_BOARD_SIZE; c++) {
                if (board[r][c] == 0) {
                    continue;
                }
                if (isFive(r, c)) {
                    System.out.println(board[r][c]);
                    System.out.println((r + 1) + " " + (c + 1));
                    return;
                }
            }
        }
        System.out.println(0);
    }

    /* (r, c)
        - 오른쪽 위 탐색 (-1, + 1)
        - 오른쪽 탐색 (0, + 1)
        - 오른쪽 아래 탐색 (+1, +1)
        - 아래 탐색 (+1, 0)
     */
    private static boolean isFive(int r, int c) {
        for (int i = 0; i < dr.length; i++) {
            int nr = r;
            int nc = c;
            int count = 1;
            for (int step = 0; step < 5; step++) {
                nr += dr[i];
                nc += dc[i];
                if (!validate(nr, nc)) {
                    break;
                }
                if (board[r][c] != board[nr][nc]) {
                    break;
                }
                count++;
            }
            if (validate(r - dr[i], c - dc[i]) && board[r - dr[i]][c - dc[i]] == board[r][c]) {
                continue;
            }
            if (count == 5) {
                return true;
            }
        }
        return false;
    }

    private static boolean validate(int r, int c) {
        return !(r < 0 || c < 0 || r >= MAX_BOARD_SIZE || c >= MAX_BOARD_SIZE);
    }
}