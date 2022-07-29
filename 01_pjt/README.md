# pjt 정리 

### problem_a
```python
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

```


> .key() 함수를 활용하여 for문을 돌리는 방법
 - .key()함수는 key값들을 literable한  객체로 반환


### problem_b

```python

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

```
> 
 - 처음에는 genres.json 인덱스를 활용하여 for문을 돌리려 했다 -> 복잡
 - movie.json에서 얻은 genre_ids를 먼저 뽑아내고 이 값들을 genres.json 안에서 맞는 값들을 찾는다.
 - 같은 값을 찾았을 때 더이상 찾지 않고 break문을 통해 탈출 -> 나중에 복잡한 알고리즘으로 가면 시간이 중요하므로 신경써야한다



### problem_c

```python
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


```

> 
 - 먼저 작성했더 코드는 problem_b에서 사용한 함수를 전혀 사용하지 않고 만들었다 -> 코드의 재사용성은 중요하므로 앞으로 꼭 생각하며 작성하자
 - 함수를 사용할때 어떤값이 리턴되고 이값을 어떻게 활용할건지 생각하며 코드를 짜자


### problem_d
``` python

import json




def max_revenue(movies):
    pass 
    # 여기에 코드를 작성합니다.
    max_revenue_list = [0,''] 
    for movie in movies:
        id = movie['id']
        newmovies_json = open(f'data/movies/{id}.json' , encoding= 'utf-8')
        newmovies_list = json.load(newmovies_json)
        if newmovies_list['revenue'] > max_revenue_list[0]:
            max_revenue_list[0] = newmovies_list['revenue']
            max_revenue_list[1] = newmovies_list['title']
    
    return max_revenue_list[1]

        
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)
    
    print(max_revenue(movies_list))

```


> 
 - json파일을 열고 그 안에 값들을 사용하기 위해서는 json.load를 반드시 써줘야한다.
 - 여러개의 파일을 열때는 for문을 통해 f''를 활용한다


### problem_e

```python
import json


def dec_movies(movies):
    # 여기에 코드를 작성합니다.
    dec_movie_list = []
    for movie in movies:
        id = movie['id']
        newmovies_json = open(f'data/movies/{id}.json' , encoding= 'utf-8')
        newmovies_list = json.load(newmovies_json)
    
        
            
        if newmovies_list['release_date'][5:7] == '12':    # value값이 str이므로 비교도 str과 해줘야한다
            dec_movie_list.append(movie['title'])
        
    return dec_movie_list

        

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)
    
    print(dec_movies(movies_list))


```

> 
 - 딕셔너리의 value값을 가져올때 그 값이 어떤 타입인지 확인하자
