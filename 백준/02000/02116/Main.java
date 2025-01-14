import java.util.*;
import java.io.*;

class Dice {
	int A;
	int B;
	int C;
	int D;
	int E;
	int F;


	private int[] sides = null;
	private int front = 0;
	private int top = 0;
	private int bottom = 0;


	Dice(int A, int B, int C, int D, int E, int F) {
		this.A = A;
		this.B = B;
		this.C = C;
		this.D = D;
		this.E = E;
		this.F = F;
	}

	public void setTop(char c) {
		if (c == 'A') {
			this.top = this.A;
			sides = new int[]{this.C, this.D, this.E, this.B};
			this.bottom = this.F;
		} else if (c == 'B') {
			this.top = this.B;
			sides = new int[] {this.C, this.A, this.E, this.F};
			this.bottom = this.D;
		} else if (c == 'C') {
			this.top = this.C;
			sides = new int[] {this.A, this.B, this.F, this.D};
			this.bottom = this.E;
		} else if (c == 'D') {
			this.top = this.D;
			sides = new int[] {this.C, this.F, this.E, this.A};
			this.bottom = this.B;
		} else if (c == 'E') {
			this.top = this.E;
			sides = new int[] {this.D, this.F, this.B, this.A};
			this.bottom = this.C;
		} else if (c == 'F'){
			this.top = this.F;
			sides = new int[] {this.C, this.B, this.E, this.D};
			this.bottom = this.A;
		}
	}

	public int getFront() {
		return this.front;
	}

	public void roll() {
		this.front = (this.front + 1) % 4;
	}
}

public class Main {
	public static void main(String[] args) throws IOException {
		Scanner sc = new Scanner(System.in);
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		StringTokenizer st = null;
		int N = Integer.parseInt(br.readLine());

		Dice[] dices = new Dice[N];
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			int A = Integer.parseInt(st.nextToken());
			int B = Integer.parseInt(st.nextToken());
			int C = Integer.parseInt(st.nextToken());
			int D = Integer.parseInt(st.nextToken());
			int E = Integer.parseInt(st.nextToken());
			int F = Integer.parseInt(st.nextToken());
			dices[i] = new Dice(A, B, C, D, E, F);
		}
	}
}