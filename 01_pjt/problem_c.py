import json
from pprint import pprint

def movie_info_1(movie, genres):
    # 여기에 코드를 작성합니다.
    movie_dict = {}
    key_list = ['id' , 'title' , 'poster_path' , 'vote_average' , 'overview' ]
    for key in movie.keys():
        if key in key_list:
            movie_dict[key] = movie[key]
    
    
    genre_name_list = []

    
    for movie_genre in movie['genre_ids']:
        for genre in genres:
            if movie_genre == genre['id']:
                genre_name_list.append(genre['name'])
                break


    movie_dict['genre_names'] = genre_name_list
    return movie_dict



def movie_info(movies,genres):

    new_movie_list = []
    for movie in movies:
        
        new_movie_list.append(movie_info_1(movie,genres))

    
    return new_movie_list


'''

def movie_info(movies, genres):
    # 여기에 코드를 작성합니다.
    new_movies_list = []
    
    
    key_list = ['id' , 'title' , 'poster_path' , 'vote_average' , 'overview' , 'genre_ids']
    
    
    for idx in range(len(movies)):
        movie_dict = {}
        for key in movies[idx].keys():
            if key in key_list:
                movie_dict[key] = movies[idx][key]
    
        genre_name_list = []
        for id in movie_dict['genre_ids']:
            for idx in range(len(genres)):
                if genres[idx]['id'] == id:
                    genre_name_list.append(genres[idx]['name'])
        movie_dict['genre_ids'] = genre_name_list

            

    
        new_movies_list.append(movie_dict)
        
    return new_movies_list
'''

    
        



    
    
    
    
    
        
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='utf-8')
    genres_list = json.load(genres_json)

    
    pprint(movie_info(movies_list, genres_list))
