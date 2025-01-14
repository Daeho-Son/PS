import java.util.*;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int N = sc.nextInt();
		int Hcenti = sc.nextInt();
		int T = sc.nextInt();

		PriorityQueue<Integer> pq = new PriorityQueue<>(new Comparator<Integer>(){
			@Override
			public int compare(Integer n1, Integer n2) {
				return n2 - n1;
			}
		});
		for (int i = 0; i < N; i++) {
			int H = sc.nextInt();
			pq.offer(H);
		}

		int count = 0;
		while (T-- > 0) {
			if (pq.peek() < Hcenti) {
				break;
			}
			int H = pq.poll();
			if (H == 1) {
				pq.offer(H);
			} else {
				pq.offer(H / 2);
			}
			count++;
		}

		if (Hcenti <= pq.peek()) {
			System.out.println("NO");
			System.out.println(pq.peek());
		} else {
			System.out.println("YES");
			System.out.println(count);
		}
	}
}