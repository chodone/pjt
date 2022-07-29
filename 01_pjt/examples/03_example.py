# open 및 json 모듈 사용예시
from pprint import pprint
import json


movie = open('sample.json', encoding='utf-8')
movie_detail = json.load(movie)

pprint(movie_detail)
