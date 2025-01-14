import java.util.*;

class Music {
	int titleLength;
	String title;
	char[] notes;

	Music(int titleLength, String title, char[] notes) {
		this.titleLength = titleLength;
		this.title = title;
		this.notes = notes;
	}

	public boolean startsWith(char[] b) {
		for (int i = 0; i < b.length; i++) {
			if (notes[i] != b[i]) {
				return false;
			}
		}
		return true;
	}

	@Override
	public String toString() {
		StringBuilder sb = new StringBuilder();

		sb.append("title length: " + titleLength + "\n");
		sb.append("title: " + title + "\n");
		sb.append("notes: ");
		for (int i = 0; i < notes.length; i++) {
			sb.append(notes[i] + " ");
		}
		sb.append("\n");
		return sb.toString();
	}
}

public class Main31562 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int N = sc.nextInt();
		int M = sc.nextInt();

		Music[] musics = new Music[N];
		for (int i = 0; i < N; i++) {
			int titleLength = sc.nextInt();
			String title = sc.next();
			char[] notes = new char[7];
			for (int j = 0; j < 7; j++) {
				notes[j] = sc.next().charAt(0);
			}
			musics[i] = new Music(titleLength, title, notes);
		}

		StringBuilder sb = new StringBuilder();
		for (int i = 0; i < M; i++) {
			char[] b = new char[3];
			for (int j = 0; j < 3; j++) {
				b[j] = sc.next().charAt(0);
			}
			List<String> titles = new ArrayList<>();
			for (int j = 0; j < musics.length; j++) {
				if (musics[j].startsWith(b)) {
					titles.add(musics[j].title);
				}
			}
			if (titles.size() == 0) {
				sb.append("!\n");
			} else if (titles.size() == 1) {
				sb.append(titles.get(0) + "\n");
			} else {
				sb.append("?\n");
			}
		}
		System.out.println(sb);
	}
}