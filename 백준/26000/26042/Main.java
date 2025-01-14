import java.util.*;
import java.io.*;

public class Main {


	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;

		int n = Integer.parseInt(br.readLine());

		int max = 0;
		int lastIndex = Integer.MAX_VALUE;
		Deque<Integer> deque = new LinkedList<>();
		for (int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			int type = Integer.parseInt(st.nextToken());
			if (type == 1) {
				deque.offerLast(Integer.parseInt(st.nextToken()));
				if (max < deque.size()) {
					max = deque.size();
					lastIndex = deque.peekLast();
				} else if (max == deque.size()) {
					lastIndex = Math.min(lastIndex, deque.peekLast());
				}
			} else if (type == 2) {
				deque.pollFirst();
			}
		}
		System.out.println(max + " " + lastIndex);
	}
}