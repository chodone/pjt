import json


def dec_movies(movies):
    # 여기에 코드를 작성합니다.
    dec_movie_list = []
    for movie in movies:
        id = movie['id']
        newmovies_json = open(f'data/movies/{id}.json' , encoding= 'utf-8')
        newmovies_list = json.load(newmovies_json)
    
        
            
        if newmovies_list['release_date'][5:7] == '12':
            dec_movie_list.append(movie['title'])
        
    return dec_movie_list

        

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)
    
    print(dec_movies(movies_list))
