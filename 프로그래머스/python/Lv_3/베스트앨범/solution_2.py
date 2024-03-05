def solution(genres, plays):
    play_by_genre = dict()
    play_by_music_id = dict()
    music_ids_by_genre = dict()

    for genre in set(genres):
        play_by_genre[genre] = 0
        music_ids_by_genre[genre] = []

    for music_id, (genre, play) in enumerate(zip(genres, plays)):
        play_by_genre[genre] += play
        play_by_music_id[music_id] = play
        music_ids_by_genre[genre].append(music_id)

    sorted_genres = list(sorted(play_by_genre.keys(), key=lambda x: play_by_genre.get(x), reverse=True))
    best_album = []
    for genre_index, genre in enumerate(sorted_genres):
        music_ids = music_ids_by_genre.get(genre)
        music_ids.sort(key=lambda x: -play_by_music_id.get(x))
        best_album += music_ids[:2]
    return best_album
