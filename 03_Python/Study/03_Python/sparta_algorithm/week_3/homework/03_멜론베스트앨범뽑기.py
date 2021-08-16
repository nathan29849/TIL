# Q. 멜론에서 장르 별로 가장 많이 재생된 노래를 "두 개씩 모아" 베스트 앨범을 출시하려 한다.
# 노래는 인덱스 구분하며, 노래를 수록하는 기준은 다음과 같다.

# 속한 노래가 많이 재생된 장르를 먼저 수록한다.
# 장르 내에서 많이 재생된 노래를 먼저 수록한다.
# 장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록한다. (앞의 인덱스를 넣으라는 말)

# 노래의 장르를 나타내는 문자열 배열 genres와
# 노래별 재생 횟수를 나타내는 정수 배열 plays가 주어질 때,

# 베스트 앨범에 들어갈 노래의 인덱스를 순서대로 반환하시오.

# genres = ["classic", "pop", "classic", "classic", "pop"]
# plays = [500, 600, 150, 800, 2500]    pop 3100, classic 1450
# # 결과로 [4, 1, 3, 0] 가 와야 합니다! # pop 2곡, classic 2곡


genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]

# 장르별(key로 우선 재생된 횟수(value)를 저장해야한다. -> 딕셔너리가 가장 유용하다고 생각해야 함.
def get_melon_best_album(genre_array, play_array):
    # 나의 풀이
    # music_dict = dict()
    # genre_dict = dict()
    # for i in range(len(genre_array)):
    #     music_dict[play_array[i]] = genre_array[i]
    #     genre_dict[genre_array[i]] = 0

    # for k, v in music_dict.items():
    #     genre_dict[v] += k
    
    # 26~ 31 line 을 아래와 같이 줄일수도 있음.
    # 장르 별로 곡의 정보(index, 재생횟수)를 배열로 묶어 저장한다.
    genre_total_play_dict = dict()
    genre_index_play_array_dict = {}
    n = len(genre_array)
    for i in range(n):
        genre = genre_array[i]
        play = play_array[i]
        if genre not in genre_total_play_dict:
            genre_total_play_dict[genre] = play
            genre_index_play_array_dict[genre] = [[i, play]]
        else:
            genre_total_play_dict[genre] += play
            genre_index_play_array_dict[genre].append([i, play])
    print(genre_total_play_dict)
    print(genre_index_play_array_dict)
    # value값을 기준으로 배열
    print(genre_index_play_array_dict.items())
    print(genre_total_play_dict.items())
    sorted_genre_play_array = sorted(genre_total_play_dict.items(), key=lambda item: item[1], reverse=True)
    # sorted_genre_play_array = sorted(genre_total_play_dict.items(), key=lambda item: -item[1])
    print(sorted_genre_play_array)
    result = []
    for genre, _value in sorted_genre_play_array:
        index_play_array = genre_index_play_array_dict[genre]
        # print(index_play_array) # 아직은 정렬이 되어있지 않은 모습
        sorted_index_play_array = sorted(index_play_array, key=lambda x: x[1], reverse=True)
        print(sorted_index_play_array)
        for i in range(len(sorted_index_play_array)):
            if i > 1:   # 2개씩만 넣기 위해서 
                break
            result.append(sorted_index_play_array[i][0])
    
    return result


# sorted 함수 : 맨 앞에 배열을 받고, 키라는 람다함수를 받는다.
# sorted(a.items(), key=lambda item: item[1])
# lambda 함수란, 특정 인자를 받아서 어떤 값으로 돌려줄건지 간단한 수식으로 표현하는 방법

print(get_melon_best_album(genres, plays))  # 결과로 [4, 1, 3, 0] 가 와야 합니다!