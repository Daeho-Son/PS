import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String stringA = sc.next();
        String stringB = sc.next();
        int[][] arr2d = new int[stringA.length() + 1][stringB.length() + 1];

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
        System.out.println(answer);
    }
}