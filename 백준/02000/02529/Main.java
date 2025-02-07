import java.util.*;

public class Main {
    private static String answerMaxNumber = "0";
    private static String answerMinNumber = "999999999";

    private static int k = 0;
    private static char[] inequalitySigns = null;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        k = sc.nextInt();
        inequalitySigns = new char[k];
        for (int i = 0; i < k; i++) {
            inequalitySigns[i] = sc.next().charAt(0);
        }
        int[] base = new int[]{0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
        boolean[] visited = new boolean[10];
        StringBuilder sb = new StringBuilder();
        recursive(base, visited, sb, 0);
        System.out.println(answerMaxNumber);
        System.out.println(answerMinNumber);
    }

    private static void recursive(int[] base, boolean[] visited, StringBuilder target, int count) {
        if (count == k + 1) {
            if (isCorrect(target)) {
                if (target.toString().compareTo(answerMaxNumber) > 0) {
                    answerMaxNumber = target.toString();
                }
                if (target.toString().compareTo(answerMinNumber) < 0) {
                    answerMinNumber = target.toString();
                }
            }
            return;
        }

        for (int i = 0; i <= 9; i++) {
            if (visited[i]) {
                continue;
            }
            target.append(base[i]);
            visited[i] = true;
            recursive(base, visited, target, count + 1);
            target.deleteCharAt(target.length() - 1);
            visited[i] = false;
        }
    }

    private static boolean isCorrect(StringBuilder target) {
        for (int i = 0; i < k; i++) {
            if (inequalitySigns[i] == '<') {
                if (target.charAt(i) - '0' > target.charAt(i + 1) - '0') {
                    return false;
                }
            } else {
                if (target.charAt(i) - '0' < target.charAt(i + 1) - '0') {
                    return false;
                }
            }
        }
        return true;
    }
}