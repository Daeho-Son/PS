import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int N = Integer.parseInt(br.readLine()); // 전체 케이스의 개수

		StringBuilder answer = new StringBuilder();
		for (int t = 1; t <= N; t++) {
			answer.append("Case #").append(t).append(": ");
			String str = br.readLine();
			String[] strArray = str.split(" ");
			for (int j = strArray.length - 1; j >= 0; j--) {
				answer.append(strArray[j] + " ");
			}
			answer.append("\n");
		}
		System.out.println(answer);
	}
}