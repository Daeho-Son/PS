import java.io.*;
import java.util.*;

/**
 * # 목표
 * <p>두 용액을 혼합한 특성값이 0에 가장 가까운 용액 만들기
 * <p>
 * # 조건
 * <p>용액의 수 N: 2 ~ 100,000
 * <p>특성값: -1,000,000,000 ~ 1,000,000,000
 */
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        int[] arr = new int[N];

        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(arr);
        int min = Integer.MAX_VALUE;
        int answer1 = Integer.MAX_VALUE;
        int answer2 = Integer.MAX_VALUE;
        for (int i = 0; i < N - 1; i++) {
            int current = arr[i];
            int target = binarySearch(arr, i + 1, N - 1, current);
            if (min > Math.abs(current + target)) {
                answer1 = current;
                answer2 = target;
                min = Math.abs(current + target);
            }
        }
        System.out.println(answer1 + " " + answer2);
    }

    private static int binarySearch(int[] arr, int start, int end, int base) {
        int target = Integer.MAX_VALUE;
        int closestSum = Integer.MAX_VALUE;
        while (start <= end) {
            int mid = (start + end) / 2;
            int sum = base + arr[mid];
            if (Math.abs(sum) < closestSum) {
                closestSum = Math.abs(sum);
                target = arr[mid];
            }
            if (sum < 0) {
                start = mid + 1;
            } else {
                end = mid - 1;
            }
        }
        return target;
    }
}