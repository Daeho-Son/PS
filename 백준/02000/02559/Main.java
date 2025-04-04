import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        int[] prefixSum = new int[n];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            int inputNumber = Integer.parseInt(st.nextToken());
            if (i == 0) {
                prefixSum[i] = inputNumber;
            } else {
                prefixSum[i] = prefixSum[i - 1] + inputNumber;
            }
        }
        int answer = Integer.MIN_VALUE;
        for (int i = k - 1; i < n; i++) {
            if (i - k < 0) {
                answer = Math.max(answer, prefixSum[i]);
            } else {
                answer = Math.max(answer, prefixSum[i] - prefixSum[i - k]);
            }
        }
        System.out.println(answer);
    }
}