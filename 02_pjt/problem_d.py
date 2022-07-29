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
