import java.util.*;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		char[] str = sc.next().toCharArray();
		for (int i = 0; i < str.length; i++) {
			if ('a' <= str[i] && str[i] <= 'z') {
				str[i] = (char)(str[i] - ('a' - 'A'));
			} else {
				str[i] = (char)(str[i] + ('a' - 'A'));
			}
		}

		System.out.println(String.valueOf(str));
	}
}