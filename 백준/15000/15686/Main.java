import java.util.*;
import java.io.*;

class Pos {
    int r;
    int c;

    public Pos(int r, int c) {
        this.r = r;
        this.c = c;
    }
}

public class Main {
    private static StringTokenizer st = null;
    private static int N = 0;
    private static int M = 0;
    private static int answer = Integer.MAX_VALUE;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        List<Pos> houses = new ArrayList<>();
        List<Pos> chickenStores = new ArrayList<>();
        for (int r = 0; r < N; r++) {
            st = new StringTokenizer(br.readLine());
            for (int c = 0; c < N; c++) {
                int type = Integer.parseInt(st.nextToken());
                if (type == 1) {
                    houses.add(new Pos(r, c));
                } else if (type == 2) {
                    chickenStores.add(new Pos(r, c));
                }
            }
        }
        boolean[] opened = new boolean[chickenStores.size()];
        getChickenDistanceOfCity(houses, chickenStores, opened, 0, 0);
        bw.write(answer + "\n");
        bw.flush();
        bw.close();
        br.close();
    }

    private static void getChickenDistanceOfCity(List<Pos> houses, List<Pos> chickenStores, boolean[] opened, int start, int count) {
        if (count == M) {
            int totalDistance = getTotalDistance(houses, chickenStores, opened);
            answer = Math.min(answer, totalDistance);
            return;
        }
        for (int i = start; i < chickenStores.size(); i++) {
            opened[i] = true;
            getChickenDistanceOfCity(houses, chickenStores, opened, i + 1, count + 1);
            opened[i] = false;
        }
    }

    private static int getTotalDistance(List<Pos> houses, List<Pos> chickenStores, boolean[] opened) {
        int totalDistance = 0;
        for (int i = 0; i < houses.size(); i++) {
            int minChickenDistance = Integer.MAX_VALUE;
            for (int j = 0; j < chickenStores.size(); j++) {
                if (opened[j]) {
                    minChickenDistance = Math.min(minChickenDistance, Math.abs(houses.get(i).r - chickenStores.get(j).r) + Math.abs(houses.get(i).c - chickenStores.get(j).c));
                }
            }
            totalDistance += minChickenDistance;
        }
        return totalDistance;
    }
}