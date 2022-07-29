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
