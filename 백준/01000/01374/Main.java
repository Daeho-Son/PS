import java.sql.Time;
import java.util.*;
import java.io.*;

class Timeline implements Comparable<Timeline> {
	int courseIndex;
	int start;
	int end;

	Timeline(int courseIndex, int start, int end) {
		this.courseIndex = courseIndex;
		this.start = start;
		this.end = end;
	}

	@Override
	public int compareTo(Timeline o) {
		return this.start - o.start;
	}

	@Override
	public String toString() {
		StringBuilder sb = new StringBuilder();
		sb.append("courseIndex: ").append(this.courseIndex + "\n");
		sb.append("start: ").append(this.start + "\n");
		sb.append("end: ").append(this.end + "\n");
		return sb.toString();
	}
}

public class Main {

	private static StringTokenizer st;
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int N = Integer.parseInt(br.readLine());
		PriorityQueue<Timeline> timelines = new PriorityQueue<>();
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			int courseIndex = Integer.parseInt(st.nextToken());
			int start = Integer.parseInt(st.nextToken());
			int end = Integer.parseInt(st.nextToken());
			timelines.offer(new Timeline(courseIndex, start, end));
		}

		int countOfClassRoom = 0;
		int[] coursesEndTime = new int[100000];
		while (!timelines.isEmpty()) {
			Timeline current = timelines.poll();
			for (int i = 0; i < 100000; i++) {
				if (coursesEndTime[i] == 0) {
					coursesEndTime[i] = current.end;
					countOfClassRoom++;
					break;
				}
				if (coursesEndTime[i] <= current.start) {
					coursesEndTime[i] = current.end;
					break;
				}
			}
		}
		System.out.println(countOfClassRoom);
	}
}