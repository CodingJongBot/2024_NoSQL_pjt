from sys import argv
from pymongo import MongoClient

client = MongoClient()
db = client.movielens

def q4(input_userid: int):
    # TODO:
    col_mv = db.ml_movies
    col_rat = db.ml_ratings
    col_tag = db.ml_tags

    user_mvs=list(col_rat.find({"userId":input_userid},{"movieId":1,"rating":1}))
    num_mvs=len(user_mvs)
    bias_sum=0

    for user_mv in user_mvs :
        mid = user_mv["movieId"]
        urat = user_mv["rating"]

        result = list(col_rat.find({"movieId":mid},{"rating":1}))
        total_rat = [x["rating"] for x in result]
        mu_rat = sum(total_rat)/len(total_rat)
        bias_sum += (urat - mu_rat)

    q4_sol = bias_sum/num_mvs

    bias =q4_sol
    print('{:.3f}'.format(bias))

if __name__ == '__main__':
    q4(int(argv[1]))

