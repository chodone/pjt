import json
from pprint import pprint


def movie_info(movie):
    # 여기에 코드를 작성합니다.
    movie_dict = {}
    key_list = ['id' , 'title' , 'poster_path' , 'vote_average' , 'overview' , 'genre_ids']
    for key in movie.keys():
        if key in key_list:
            movie_dict[key] = movie[key]
    return movie_dict


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='utf-8')
    movie_dict = json.load(movie_json)
    
    pprint(movie_info(movie_dict))
