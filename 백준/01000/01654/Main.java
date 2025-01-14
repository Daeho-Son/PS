import java.io.*;
import java.util.StringTokenizer;

public class Main {
    private static StringTokenizer st = null;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        st = new StringTokenizer(br.readLine());
        int K = Integer.parseInt(st.nextToken());
        int N = Integer.parseInt(st.nextToken());

        int max = 0;
        int[] lengthOfLanCables = new int[K];
        for (int i = 0; i < K; i++) {
            int length = Integer.parseInt(br.readLine());
            max = Math.max(max, length);
            lengthOfLanCables[i] = length;
        }
        long answer = binarySearch(lengthOfLanCables, 1, max, N);
        System.out.println(answer);
    }

    private static long binarySearch(int[] lengthOfLanCables, long start, long end, int targetCount) {
        long answer = 0;
        while (start <= end) {
            long mid = (start + end) / 2;
            long count = 0;
            for (int i = 0; i < lengthOfLanCables.length; i++) {
                count += lengthOfLanCables[i] / mid;
            }
            if (count >= targetCount) {
                answer = mid;
                start = mid + 1;
            } else {
                end = mid - 1;
            }
        }
        return answer;
    }
}