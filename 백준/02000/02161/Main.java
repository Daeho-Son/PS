import java.nio.Buffer;
import java.util.*;
import java.io.*;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int N = Integer.parseInt(br.readLine());
		Deque<Integer> deque = new LinkedList<>();
		for (int i = 0; i < N; i++) {
			deque.offerLast(i + 1);
		}

		StringBuilder sb = new StringBuilder();
		while (deque.size() != 1) {
			sb.append(deque.pollFirst()).append(" ");
			deque.offerLast(deque.pollFirst());
		}
		sb.append(deque.pollFirst());
		System.out.println(sb);
	}
}