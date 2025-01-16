import java.io.*;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    private static StringTokenizer st = null;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        int[] dots = new int[N];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            dots[i] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(dots);
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int start = Integer.parseInt(st.nextToken());
            int end = Integer.parseInt(st.nextToken());

            int countBeforeStart = 0;
            if (start > 1) {
                countBeforeStart = binarySearch(dots, 0, N - 1, start - 1) + 1;
            }
            int countUntilEnd = binarySearch(dots, 0, N - 1, end) + 1;
            int countOfLineSegment = countUntilEnd - countBeforeStart;
            bw.write(countOfLineSegment + "\n");
        }
        bw.flush();
    }

    private static int binarySearch(int[] dots, int start, int end, int target) {
//        System.out.println("[binarySearch] " + target);
        int middle = 0;
        while (start <= end) {
            middle = (start + end) / 2;
//            System.out.println("middle: " + middle);
            if (dots[middle] <= target) {
                start = middle + 1;
            } else {
                end = middle - 1;
            }
        }
//        System.out.println("return: " + (start + end) / 2);
        return end;
    }
}