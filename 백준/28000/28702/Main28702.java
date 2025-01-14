import java.math.BigDecimal;
import java.util.*;

import javax.print.attribute.standard.NumberUpSupported;

public class Main28702 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int currentNumber = 0;
		for (int i = 0; i < 3; i++) {
			String str = sc.next();
			if (isNumeric(str)) {
				currentNumber = Integer.parseInt(str);
			} else {
				currentNumber++;
			}
		}
		String fizzBuzz = getFizzBuzz(currentNumber + 1);
		System.out.println(fizzBuzz);
	}

	private static boolean isNumeric(String str) {
		return str.chars().allMatch(Character::isDigit);
	}

	private static String getFizzBuzz(int n) {
		if (n % 3 == 0 && n % 5 == 0) {
			return "FizzBuzz";
		} else if (n % 3 == 0 && n % 5 != 0) {
			return "Fizz";
		} else if (n % 3 != 0 && n % 5 == 0) {
			return "Buzz";
		} else {
			return String.valueOf(n);
		}
	}
}