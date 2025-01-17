import java.io.*;
import java.util.Arrays;
import java.util.StringTokenizer;
import java.util.stream.IntStream;
import java.util.stream.Stream;

public class Main {
    private static StringTokenizer st = null;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int[] arr = new int[N];
        int M = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }
        int start = Arrays.stream(arr).max().orElse(0);
        System.out.println(start);
        int end = Arrays.stream(arr).sum();
        int answer = binarySearch(arr, start, end, M);
        System.out.println(answer);
    }

    private static int binarySearch(int[] arr, int start, int end, int targetCount) {
        while (start <= end) {
            int cumulatedSum = 0;
            int count = 1;
            int middle = (start + end) / 2;

            for (int i = 0; i < arr.length; i++) {
                if (cumulatedSum + arr[i] > middle) {
                    cumulatedSum = 0;
                    count++;
                }
                cumulatedSum += arr[i];
            }
            if (count > targetCount) {
                start = middle + 1;
            } else {
                end = middle - 1;
            }
        }
        return start;
    }
}