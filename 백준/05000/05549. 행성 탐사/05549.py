import sys
input = sys.stdin.readline

tile = {'J': (1, 0, 0), 'O': (0, 1, 0), 'I': (0, 0, 1)}

def solution():
    m, n = map(int, input().split())
    k = int(input())
    planet_map = [[(0, 0, 0)] * (n + 1)]  # (J, O, I)
    planet_map.extend([(0, 0, 0)] for _ in range(m))
    for y in range(1, m + 1):
        for x, joi in enumerate(list(input().strip())):
            x += 1
            left_up = planet_map[y - 1][x - 1]
            left = planet_map[y][x - 1]
            up = planet_map[y - 1][x]
            current = tile.get(joi)
            j = up[0] + left[0] + current[0] - left_up[0]
            o = up[1] + left[1] + current[1] - left_up[1]
            i = up[2] + left[2] + current[2] - left_up[2]
            planet_map[y].append((j, o, i))
    for _ in range(k):
        a, b, c, d = map(lambda x: int(x), input().rstrip().split())
        j = planet_map[c][d][0] + planet_map[a-1][b-1][0] - planet_map[a-1][d][0] - planet_map[c][b - 1][0]
        o = planet_map[c][d][1] + planet_map[a-1][b-1][1] - planet_map[a-1][d][1] - planet_map[c][b - 1][1]
        i = planet_map[c][d][2] + planet_map[a-1][b-1][2] - planet_map[a-1][d][2] - planet_map[c][b - 1][2]
        print(j, o, i)


def main():
    solution()


if __name__ == '__main__':
    main()
