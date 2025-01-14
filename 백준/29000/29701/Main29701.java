import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Scanner;

public class Main29701 {
	private static Map<String, String> wordByMorseCode = new HashMap<>() {{
		put(".-", "A");
		put("-...", "B");
		put("-.-.", "C");
		put("-..", "D");
		put(".", "E");
		put("..-.", "F");
		put("--.", "G");
		put("....", "H");
		put("..", "I");
		put(".---", "J");
		put("-.-", "K");
		put(".-..", "L");
		put("--", "M");
		put("-.", "N");
		put("---", "O");
		put(".--.", "P");
		put("--.-", "Q");
		put(".-.", "R");
		put("...", "S");
		put("-", "T");
		put("..-", "U");
		put("...-", "V");
		put(".--", "W");
		put("-..-", "X");
		put("-.--", "Y");
		put("--..", "Z");
		put(".----", "1");
		put("..---", "2");
		put("...--", "3");
		put("....-", "4");
		put(".....", "5");
		put("-....", "6");
		put("--...", "7");
		put("---..", "8");
		put("----.", "9");
		put("-----", "0");
		put("--..--", ",");
		put(".-.-.-", ".");
		put("..--..", "?");
		put("---...", ":");
		put("-....-", "-");
		put(".--.-.", "@");
	}};

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		StringBuilder sb = new StringBuilder();
		int N = sc.nextInt();
		for (int i = 0; i < N; i++) {
			String morseCode = sc.next();
			sb.append(wordByMorseCode.get(morseCode));
		}
		System.out.println(sb);
	}
}