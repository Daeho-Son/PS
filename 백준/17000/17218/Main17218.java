import java.util.*;

public class Main17218 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		String password1 = sc.next();
		String password2 = sc.next();
		String password = generatePassword(password1, password2);
		System.out.println(password);
	}

	private static String generatePassword(String password1, String password2) {
		int[][] arr2d = lcs(password1, password2);
		String password = backtracking(arr2d, password1, password2, password1.length(), password2.length());
		return password;
	}

	private static int[][] lcs(String password1, String password2) {
		int[][] arr2d = new int[password1.length() + 1][password2.length() + 1];
		for (int r = 0; r <= password1.length(); r++) {
			for (int c = 0; c <= password2.length(); c++) {
				if (r == 0 || c == 0) {
					arr2d[r][c] = 0;
					continue;
				}
				if (password1.charAt(r - 1) == password2.charAt(c - 1)) {
					arr2d[r][c] = arr2d[r - 1][c - 1] + 1;
				} else {
					arr2d[r][c] = Math.max(arr2d[r - 1][c], arr2d[r][c - 1]);
				}
			}
		}
		return arr2d;
	}

	private static String backtracking(int[][] arr2d, String p1, String p2, int r, int c) {
		if (r == 0 || c == 0) {
			return "";
		}
		if (arr2d[r - 1][c] == arr2d[r][c]) {
			return backtracking(arr2d, p1, p2, r - 1, c);
		} else if (arr2d[r][c - 1] == arr2d[r][c]) {
			return backtracking(arr2d, p1, p2, r, c - 1);
		} else {
			return backtracking(arr2d, p1, p2, r - 1, c - 1) + p1.charAt(r - 1);
		}
	}
}