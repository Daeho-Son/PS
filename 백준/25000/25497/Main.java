import java.util.*;

public class Main {
	private static int countSkillUsed = 0;
	private static int commandR = 0;
	private static int commandK = 0;


	public static void main(String[] args) {
		/**
		 * 1 ~ 9: 연계 없이 사용할 수 있는 기술
		 * L: R의 사전 기술
		 * S: K의 사전 기술
		 */
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		String commands = sc.next();

		for (int i = 0; i < N; i++) {
			char command = commands.charAt(i);
			if (command == 'L') {
				commandR++;
			} else if (command == 'S') {
				commandK++;
			} else if (command == 'R') {
				if (commandR == 0) {
					break;
				}
				countSkillUsed++;
				commandR--;
			} else if (command == 'K') {
				if (commandK == 0) {
					break;
				}
				countSkillUsed++;
				commandK--;
			} else {
				countSkillUsed++;
			}
		}
		System.out.println(countSkillUsed);
	}
}