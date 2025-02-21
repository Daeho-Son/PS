import java.util.*;

public class Main {

    private static String stringA = null;
    private static String stringB = null;
    private static int[][] arr2d = null;
    private static Set<String> lcs = null;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        stringA = sc.next();
        stringB = sc.next();
        arr2d = new int[stringA.length() + 1][stringB.length() + 1];

        int answer = 0;
        for (int i = 0; i <= stringA.length(); i++) {
            for (int j = 0; j <= stringB.length(); j++) {
                if (i == 0 || j == 0) {
                    arr2d[i][j] = 0;
                } else if (stringA.charAt(i - 1) == stringB.charAt(j - 1)) {
                    arr2d[i][j] = arr2d[i - 1][j - 1] + 1;
                } else {
                    arr2d[i][j] = Math.max(arr2d[i - 1][j], arr2d[i][j - 1]);
                }
                answer = Math.max(answer, arr2d[i][j]);
            }
        }

        lcs = new HashSet<>();
        backtracking(stringA.length(), stringB.length(), new StringBuilder());
        for (String s: lcs) {
            System.out.print(s + " ");
        }
        System.out.println();
        System.out.println(answer);
    }

    private static void backtracking(int i, int j, StringBuilder current) {
        if (i == 0 || j == 0) {
            lcs.add(current.reverse().toString());
            current.reverse();
            return;
        }
        if (stringA.charAt(i - 1) == stringB.charAt(j - 1)) {
            current.append(stringA.charAt(i - 1));
            backtracking(i - 1, j - 1, current);
            current.deleteCharAt(current.length() - 1);
        } else {
            if (arr2d[i - 1][j] == arr2d[i][j]) {
                backtracking(i - 1, j, current);
            }
            if (arr2d[i][j - 1] == arr2d[i][j]) {
                backtracking(i, j - 1, current);
            }
        }
    }
}