import json
from pprint import pprint


def movie_info(movie, genres):
    # 여기에 코드를 작성합니다.
    movie_dict = {}
    key_list = ['id' , 'title' , 'poster_path' , 'vote_average' , 'overview' ]
    for key in movie.keys():
        if key in key_list:
            movie_dict[key] = movie[key]
    
    
    genre_name_list = []

    # for id in movie_dict['genre_ids']:
    #     for idx in range(len(genres)):
    #         if genres[idx]['id'] == id:
    #             genre_name_list.append(genres[idx]['name'])
    
    for movie_genre in movie['genre_ids']:
        for genre in genres:
            if movie_genre == genre['id']:
                genre_name_list.append(genre['name'])
                break    #  시간 단축


    movie_dict['genre_names'] = genre_name_list
    return movie_dict



        

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='utf-8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='utf-8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))
