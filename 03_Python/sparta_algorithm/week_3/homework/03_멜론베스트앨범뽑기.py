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


def get_melon_best_album(genre_array, play_array):
    # 구현해보세요!
    return []


print(get_melon_best_album(genres, plays))  # 결과로 [4, 1, 3, 0] 가 와야 합니다!