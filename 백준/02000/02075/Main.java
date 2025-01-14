import java.util.*;
import java.io.*;

class Node implements Comparable<Node> {
	int n;
	int r;
	int c;

	Node(int n, int r, int c) {
		this.n = n;
		this.r = r;
		this.c = c;
	}

	@Override
	public int compareTo(Node o) {
		return o.n - this.n;
	}
}

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = null;
		int N = Integer.parseInt(br.readLine());

		PriorityQueue<Node> pq = new PriorityQueue<>();

		int[][] arr2d = new int[N][N];
		for (int r = 0; r < N; r++) {
			st = new StringTokenizer(br.readLine());
			for (int c = 0; c < N; c++) {
				arr2d[r][c] = Integer.parseInt(st.nextToken());
				if (r == N - 1) {
					pq.offer(new Node(arr2d[r][c], r, c));
				}
			}
		}

		while (--N > 0) {
			Node current = pq.poll();
			if (current.r - 1 < 0) {
				continue;
			}
			pq.offer(new Node(arr2d[current.r - 1][current.c], current.r - 1, current.c));
		}
		System.out.println(pq.poll().n);
	}
}