def solution(genres, plays):
    answer = []

    music_by_genre = {genre: [] for genre in set(genres)}
    for music_id, (genre, play) in enumerate(zip(genres, plays)):
        music_by_genre[genre].append([music_id, play])

    sorted_genres = sorted(music_by_genre.keys(), key=lambda x: sum(map(lambda y: y[1], music_by_genre.get(x))), reverse=True)
    for genre in sorted_genres:
        sorted_music = sorted(music_by_genre.get(genre), key=lambda x: -x[1])
        answer += list(map(lambda x: x[0], sorted_music))[:2]
    return answer
