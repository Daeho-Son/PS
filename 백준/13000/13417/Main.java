import java.util.*;
import java.io.*;

public class Main {
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int T = Integer.parseInt(br.readLine());

		StringBuilder answer = new StringBuilder();
		for (int t = 0; t < T; t++) {
			int N = Integer.parseInt(br.readLine());
			char[] arr = new char[N];
			StringTokenizer st = new StringTokenizer(br.readLine());
			for (int i = 0; i < N; i++) {
				arr[i] = st.nextToken().charAt(0);
			}
			answer.append(solution(arr, N) + "\n");
		}
		System.out.println(answer);
	}

	private static String solution(char[] arr, int N) {
		String answer = "";

		for (int i = 0; i < N; i++) {
			if ((answer + arr[i]).compareTo(arr[i] + answer) <= 0) {
				answer = answer + arr[i];
			} else {
				answer = arr[i] + answer;
			}
		}
		return answer;
	}
}