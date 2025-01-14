import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

class CustomSet {
	int b;
	StringBuilder sb;

	CustomSet(int size) {
		this.b = 0;
		this.sb = new StringBuilder();
	}

	private void executeNoArgumentCommand(String operator) {
		if (operator.equals("all")) {
			this.all();
		} else if (operator.equals("empty")) {
			this.empty();
		}
	}

	private void executeArgumentCommand(String operator, int arg) {
		if (operator.equals("add")) {
			this.add(arg);
		} else if (operator.equals("remove")) {
			this.remove(arg);
		} else if (operator.equals("check")) {
			this.check(arg);
		} else if (operator.equals("toggle")) {
			this.toggle(arg);
		}
	}

	public void execute(String input) {
		String[] commandAndArgument = input.split(" ");
		if (commandAndArgument.length == 1) {
			executeNoArgumentCommand(commandAndArgument[0]);
		} else {
			int argument = commandAndArgument[1].charAt(0) - '0';
			executeArgumentCommand(commandAndArgument[0], argument - 1);
		}
	}

	public void add(int x) {
		this.b |= 1 << x;
	}

	public void remove(int x) {
		this.b &= ~(1 << x);
	}

	public void check(int x) {
		if ((this.b & 1 << x) != 0) {
			sb.append(1 + "\n");
		} else {
			sb.append(0 + "\n");
		}
	}

	public void toggle(int x) {
		this.b ^= 1 << x;
	}

	public void all() {
		this.b = 2097151;
	}

	public void empty() {
		this.b = 0;
	}

	public void print() {
		System.out.println(sb);
	}
}

public class Main11723 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int m = Integer.parseInt(br.readLine());

		CustomSet s = new CustomSet(21);
		for (int i = 0; i < m; i++) {
			s.execute(br.readLine());
		}
		s.print();
	}
}