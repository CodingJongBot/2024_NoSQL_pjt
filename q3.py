from sys import argv
from pymongo import MongoClient

client = MongoClient()
db = client.movielens

def q3(input_title: str):
    # TODO: 
    col_mv = db.ml_movies
    col_rat = db.ml_ratings
    col_tag = db.ml_tags
    
    result = list(col_mv.find({"title":input_title},{"movieId":1}))
    mv_ids = [x["movieId"] for x in result]

    all_ratings=[]
    for mv_id in mv_ids:
        all_ratings.extend(list(col_rat.find({"movieId":mv_id},{"rating":1})))
    q3_sol = round((sum([x["rating"] for x in all_ratings])/len(all_ratings)),3)
    
    _avg = q3_sol
    print('{:.3f}'.format(_avg))

if __name__ == '__main__':
    q3(argv[1])

