import java.io.BufferedOutputStream;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.math.BigDecimal;
import java.util.*;

public class Main01620 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		StringTokenizer st = new StringTokenizer(br.readLine());
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());

		Map<Integer, String> pocketmonNameByNumber = new HashMap<>();
		Map<String, Integer> pocketmonNumberByName = new HashMap<>();
		for (int i = 1; i <= N; i++) {
			String name = br.readLine();
			pocketmonNameByNumber.put(i, name);
			pocketmonNumberByName.put(name, i);
		}

		StringBuilder sb = new StringBuilder();
		for (int i = 0; i < M; i++) {
			String input = br.readLine();
			if (Character.isDigit(input.charAt(0))) {
				sb.append(pocketmonNameByNumber.get(Integer.parseInt(input)) + "\n");
			} else {
				sb.append(pocketmonNumberByName.get(input) + "\n");
			}
		}
		bw.write(sb.toString());
		bw.flush();
	}
}