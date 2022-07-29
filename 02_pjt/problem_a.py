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
