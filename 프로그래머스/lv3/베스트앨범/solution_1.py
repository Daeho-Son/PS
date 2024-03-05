def solution(genres, plays):
    best_album = []
    answer = []
    play_by_genre = dict()
    play_by_music_id = dict()

    for music_id, music in enumerate(zip(genres, plays)):
        genre, play = music
        play_by_genre[genre] = play_by_genre.get(genre, 0) + play
        play_by_music_id[music_id] = play

    sorted_genres = list(sorted(play_by_genre.keys(), key=lambda x: play_by_genre.get(x), reverse=True))

    best_album = [[] for _ in range(len(sorted_genres))]

    for music_id, music in enumerate(zip(genres, plays)):
        genre, play = music
        genre_index = sorted_genres.index(genre)
        best_album[genre_index].append(music_id)

    music_count = len(genres)
    for ids_by_genre in best_album:
        count = 0
        ids_by_genre.sort(key=lambda x: -play_by_music_id.get(x))
        for music_id in ids_by_genre:
            if count == 2:
                break
            answer.append(music_id)
            count += 1
    return answer
