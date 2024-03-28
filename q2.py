from sys import argv
from pymongo import MongoClient

client = MongoClient()
db = client.movielens

def q2(input_tag: str):
    # TODO: 
    col_mv = db.ml_movies
    col_rat = db.ml_ratings
    col_tag = db.ml_tags

    result = list(col_tag.find({"tag":input_tag},{"movieId":1}))
    mvs_id_tag = [x['movieId'] for x in result]
    titles=[]
    for mv_id in mvs_id_tag:
        titles.extend(list(col_mv.find({"movieId":mv_id},{"title":1})))
    q2_sol = sorted(set([x['title'] for x in titles]))
    for sol in q2_sol:
        print(sol)

if __name__ == '__main__':
    q2(argv[1])

