import java.util.*;
import java.io.*;

public class Main17219 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		StringTokenizer st = new StringTokenizer(br.readLine());
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());

		Map<String, String> map = new HashMap<>();
		for (int i = 0; i < N; i++) {
			String[] siteAndPassword = br.readLine().split(" ");
			map.put(siteAndPassword[0], siteAndPassword[1]);
		}

		StringBuilder sb = new StringBuilder();
		for (int i = 0; i < M; i++) {
			String site = br.readLine();
			sb.append(map.get(site) + "\n");
		}
		System.out.println(sb);
	}
}