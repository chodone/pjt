
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
