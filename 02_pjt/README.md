## problem_a

```python

from pprint import pprint
import requests
key = '0569eeeb0a6e89e26256bbe455de8cbc'

def popular_count():
    
    # 여기에 코드를 작성합니다.
    URL = 'https://api.themoviedb.org/3/movie/popular'
    params = {
        'api_key' : '0569eeeb0a6e89e26256bbe455de8cbc',
        'language' : 'ko',
        'region' : 'KR'


    }
    
    response = requests.get(URL , params=params).json()

    return len(response['results'])

    


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20
```


## problem_b

```python

import requests
from pprint import pprint


def vote_average_movies():
    # 여기에 코드를 작성합니다.
    
    URL = 'https://api.themoviedb.org/3/movie/popular'
    params = {
        'api_key' : '0569eeeb0a6e89e26256bbe455de8cbc',
        'language' : 'ko',
        'region' : 'KR'


    }
    
    response = requests.get(URL , params=params).json()

    movie_lst = response['results']
    result = []

    for movie in movie_lst:
      if float(movie['vote_average']) >= 8.0:
        result.append(movie)     

    return result


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록중 vote_average가 8 이상인 영화목록 반환
    (주의) popular 영화목록의 경우 시기에 따라 아래 예시 출력과 차이가 있을 수 있음
    """
    pprint(vote_average_movies())
    """
    [{'adult': False,
      'backdrop_path': '/ocUp7DJBIc8VJgLEw1prcyK1dYv.jpg',
      'genre_ids': [28, 12, 878],
      'id': 634649,
      'original_language': 'en',
      'original_title': 'Spider-Man: No Way Home',
      'overview': '미스테리오의 계략으로 세상에 정체가 탄로난 스파이더맨 피터 파커는 하루 아침에 평범한 일상을 잃게 된다. 문제를 '
                  '해결하기 위해 닥터 스트레인지를 찾아가 도움을 청하지만 뜻하지 않게 멀티버스가 열리면서 각기 다른 차원의 '
                  '불청객들이 나타난다. 닥터 옥토퍼스를 비롯해 스파이더맨에게 깊은 원한을 가진 숙적들의 강력한 공격에 피터 파커는 '
                  '사상 최악의 위기를 맞게 되는데…',
      'popularity': 1842.592,
      'poster_path': '/voddFVdjUoAtfoZZp2RUmuZILDI.jpg',
      'release_date': '2021-12-15',
      'title': '스파이더맨: 노 웨이 홈',
      'video': False,
      'vote_average': 8.1,
      'vote_count': 13954},
    ..생략..,
    }]
    """

```

## problem_c

```python

import requests
from pprint import pprint


def ranking():
    # 여기에 코드를 작성합니다.
    URL = 'https://api.themoviedb.org/3/movie/popular'
    params = {
        'api_key' : '0569eeeb0a6e89e26256bbe455de8cbc',
        'language' : 'ko',
        'region' : 'KR'
    }
    
    response = requests.get(URL , params=params).json() 

    movie_lst = response['results']
    movie_lst.sort(key = lambda x : x['vote_average'], reverse=True)

    return movie_lst[:5]



# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록을 정렬하여 평점순으로 5개 영화 반환
    (주의) popular 영화목록의 경우 시기에 따라 아래 예시 출력과 차이가 있을 수 있음
    """
    pprint(ranking())
    """
    [{'adult': False,
      'backdrop_path': '/odJ4hx6g6vBt4lBWKFD1tI8WS4x.jpg',
      'genre_ids': [28, 18],
      'id': 361743,
      'original_language': 'en',
      'original_title': 'Top Gun: Maverick',
      'overview': '최고의 파일럿이자 전설적인 인물 매버릭은 자신이 졸업한 훈련학교 교관으로 발탁된다. 그의 명성을 모르던 팀원들은 '
                  '매버릭의 지시를 무시하지만 실전을 방불케 하는 상공 훈련에서 눈으로 봐도 믿기 힘든 전설적인 조종 실력에 모두가 '
                  '압도된다. 매버릭의 지휘 아래 견고한 팀워크를 쌓아가던 팀원들에게 국경을 뛰어넘는 위험한 임무가 주어지자 매버릭은 '
                  '자신이 가르친 동료들과 함께 마지막이 될지 모를 하늘 위 비행에 나서는데…',
      'popularity': 911.817,
      'poster_path': '/jMLiTgCo0vXJuwMzZGoNOUPfuj7.jpg',
      'release_date': '2022-06-22',
      'title': '탑건: 매버릭',
      'video': False,
      'vote_average': 8.4,
      'vote_count': 1463},
    ..생략..,
    }]
    """

```

## problem_d

```python

import requests
from pprint import pprint


def recommendation(title):
    
    # 여기에 코드를 작성합니다.  
    BASE_URL1 = 'https://api.themoviedb.org/3'
    path1 = '/search/movie'
    params1 = {
        'api_key' : '0569eeeb0a6e89e26256bbe455de8cbc',
        'language' : 'ko',
        'region' : 'KR',
        'query' : title
    }
    response = requests.get(BASE_URL1 + path1 , params=params1).json()
    movie_lst = response['results']
    movie_id = 0

    if not movie_lst:
        return None
    else:
        movie_id = movie_lst[0]['id']
    
    
    BASE_URL2 = 'https://api.themoviedb.org/3'
    path2 = f'/movie/{movie_id}/recommendations'
    params2 = {
        'api_key' : '0569eeeb0a6e89e26256bbe455de8cbc',
        'language' : 'ko',
        'region' : 'KR',
        
    }
    response1 = requests.get(BASE_URL2 + path2 , params=params2).json()
    
    recom_movie_lst =  response1['results']
    result = []
    for recom_movie in recom_movie_lst:
        result.append(recom_movie['title'])

    return result

    
    

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화의 id를 기반으로 추천 영화 목록 구성
    추천 영화가 없을 경우 []를 반환
    영화 id 검색에 실패할 경우 None을 반환
    (주의) 추천 영화의 경우 아래 예시 출력과 차이가 있을 수 있음
    """
    pprint(recommendation('기생충'))
    #['조커', '1917', '조조 래빗', ..생략.., '살인의 추억', '펄프 픽션']
    pprint(recommendation('그래비티'))
    # []
    pprint(recommendation('검색할 수 없는 영화'))
    # None



```

## problem_e

```python

import requests
from pprint import pprint


def credits(title):
    
    # 여기에 코드를 작성합니다.
    BASE_URL = 'https://api.themoviedb.org/3'
    path1 = '/search/movie'
    params1 = {
        'api_key' : '0569eeeb0a6e89e26256bbe455de8cbc',
        'language' : 'ko',
        'region' : 'KR',
        'query' : title
    }
    response = requests.get(BASE_URL + path1 , params=params1).json()
    movie_lst = response['results']
    movie_id = 0

    if not movie_lst:
        return None
    else:
        movie_id = movie_lst[0]['id']  

    
    # credit
    path2 = f'/movie/{movie_id}/credits'
    params1 = {
        'api_key' : '0569eeeb0a6e89e26256bbe455de8cbc',
        'language' : 'ko',
        'region' : 'KR',
    }
    response2 = requests.get(BASE_URL + path2 , params=params1).json()
    
    casts = response2['cast']
    crews = response2['crew']
    cast_list = []
    directing_list = []
    
    for cast in casts:
        if cast['cast_id'] < 10:
            cast_list.append(cast['name'])
        
        # if cast['known_for_department'] == "Directing":
        #     directing_list.append(cast['name'])

    for crew in crews:
        if crew['department'] == "Directing":
            directing_list.append(crew['name'])

    result ={}
    result['cast'] = cast_list
    result['directing'] = directing_list

    return result

    


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화 id를 통해 영화 상세정보를 검색하여 주연배우 목록(cast)과 스태프(crew) 중 연출진 목록을 반환
    영화 id 검색에 실패할 경우 None을 반환
    """
    pprint(credits('기생충'))
    # {'cast': ['Song Kang-ho', 'Lee Sun-kyun', ..., 'Jang Hye-jin'], 'crew': ['Bong Joon-ho', 'Park Hyun-cheol', ..., 'Yoon Young-woo']}
    pprint(credits('검색할 수 없는 영화'))
    # None

```

