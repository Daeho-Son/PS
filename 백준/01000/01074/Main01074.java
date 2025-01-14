import java.util.*;

public class Main01074 {

	private static int answer = 0;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int boardSize = (int) Math.pow(2, sc.nextInt());
		int targetRow = sc.nextInt();
		int targetColumn = sc.nextInt();
		drawZ(boardSize, 0, 0, targetRow, targetColumn, 0);
		System.out.println(answer);
	}

	private static void drawZ(int boardSize, int drawR, int drawC, int targetR, int targetC, int number) {
		if (boardSize == 1) {
			answer = number;
			return;
		}
		for (int row = 0; row < boardSize; row += (boardSize / 2)) {
			if (!(row + drawR <= targetR && targetR < row + drawR + (boardSize / 2))) {
				number += Math.pow(boardSize, 2) / 2;
				continue;
			}
			for (int column = 0; column < boardSize; column += (boardSize / 2)) {
				if (column + drawC <= targetC && targetC < column + drawC + (boardSize / 2)) {
					drawZ(boardSize / 2, row + drawR, column + drawC, targetR, targetC, number);
				}
				number += Math.pow(boardSize, 2) / 4;
			}
		}
	}
}
