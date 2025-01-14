import java.util.*;

public class Main01874 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int countOfNumber = sc.nextInt();
		Queue<Integer> targetSequence = new LinkedList<>();
		for (int i = 0; i < countOfNumber; i++) {
			targetSequence.offer(sc.nextInt());
		}

		Stack<Integer> stack = new Stack<>();
		StringBuilder stringBuilder = new StringBuilder();
		for (int i = 1; i <= countOfNumber; i++) {
			stack.push(i);
			stringBuilder.append("+\n");
			while (!stack.isEmpty() && (stack.peek().equals(targetSequence.peek()))) {
				stack.pop();
				targetSequence.poll();
				stringBuilder.append("-\n");
			}
		}
		if (!targetSequence.isEmpty()) {
			System.out.println("NO");
		} else {
			System.out.println(stringBuilder.toString());
		}
	}
}