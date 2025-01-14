import java.util.*;
import java.io.*;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int N = Integer.parseInt(br.readLine());
		StringTokenizer st = new StringTokenizer(br.readLine());

		int[] arr = new int[201];
		for (int i = 0; i < N; i++) {
			int key = Integer.parseInt(st.nextToken());
			arr[key + 100]++;
		}
		int v = Integer.parseInt(br.readLine());
		System.out.println(arr[v + 100]);
	}
}