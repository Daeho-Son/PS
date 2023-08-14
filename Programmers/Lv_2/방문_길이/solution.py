MAP_SIZE = 5


def is_valid_pos(pos):
    pos_x, pos_y = pos
    if -MAP_SIZE <= pos_x <= MAP_SIZE and -MAP_SIZE <= pos_y <= MAP_SIZE:
        return True
    return False


def solution(dirs):
    answer = 0
    moves_dict = {'U': (0, 1), 'D': (0, -1), 'R': (1, 0), 'L': (-1, 0)}
    current_pos = [0, 0]
    visited = set()
    for d in dirs:
        current_x, current_y = current_pos
        move_x, move_y = moves_dict[d]
        moved_pos = [current_x + move_x, current_y + move_y]
        if is_valid_pos(moved_pos):
            if (tuple(current_pos), tuple(moved_pos)) not in visited:
                visited.add((tuple(current_pos), tuple(moved_pos)))
                visited.add((tuple(moved_pos), tuple(current_pos)))
                answer += 1
            current_pos = moved_pos
    return answer
