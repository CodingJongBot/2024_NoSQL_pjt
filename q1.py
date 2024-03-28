from pymongo import MongoClient
import pprint

client = MongoClient()
db = client.movielens

def q1():
    col_mv = db.ml_movies
    col_rat = db.ml_ratings
    col_tag = db.ml_tags

    #remove past indexes
    col_mv.drop_indexes()
    col_rat.drop_indexes()
    col_tag.drop_indexes()

    #no index
    pprint.pprint(col_tag.find({"tag":"italian western"}).explain()['executionStats'])
    '''
    {'allPlansExecution': [],
    'executionStages': {'advanced': 23,
                        'direction': 'forward',
                        'docsExamined': 1093360,
                        'executionTimeMillisEstimate': 6,
                        'filter': {'tag': {'$eq': 'italian western'}},
                        'isEOF': 1,
                        'nReturned': 23,
                        'needTime': 1093338,
                        'needYield': 0,
                        'restoreState': 8541,
                        'saveState': 8541,
                        'stage': 'COLLSCAN',
                        'works': 1093362},
    'executionSuccess': True,
    'executionTimeMillis': 1158,
    'nReturned': 23,
    'totalDocsExamined': 1093360,
    'totalKeysExamined': 0}
    '''

    # col_mv.find()
    # col_rat.find()
    # create index
    # tag collection:tag  
    # Q2의 경우 tag collection에서 tag 검색을 통해 movieId list를 찾아냄
    # Q2: tag로 movieId 찾기 -> movieId로 title set 찾기
    col_tag.create_index({"tag":1})#1 is ASC


    # movie collection: title,movieId (compound ASC, ASC) 
    # Q3에서 movie collection에서 title을 통해 movieId를 찾아내고 Q2에서 movieId list에 맞는 title을 찾아냄.
    # Q3: title로 movieId찾기 -> movieId로 전체 rating 찾아서 계산
    col_mv.create_index({"title":1,"movieId":1})


    # rating collection: movieId,userId
    # Q4에서 userId를 통해 movieId와 rating을 찾아내고 rating collection에서 movieId를 사용해 해당 영화의 전체 평점평균을 계산한다.
    # Q4: userId로 movieId,rating 찾기 -> movieId로 전체 rating 찾아서 계산
    col_rat.create_index({"movieId":1,"userId":1})




    #with index
    pprint.pprint(col_tag.find({"tag":"italian western"}).explain()['executionStats'])

    # col_mv.find()
    # col_rat.find()
    '''
    {'allPlansExecution': [],
    'executionStages': {'advanced': 23,
                        'direction': 'forward',
                        'docsExamined': 1093360,
                        'executionTimeMillisEstimate': 6,
                        'filter': {'tag': {'$eq': 'italian western'}},
                        'isEOF': 1,
                        'nReturned': 23,
                        'needTime': 1093338,
                        'needYield': 0,
                        'restoreState': 8541,
                        'saveState': 8541,
                        'stage': 'COLLSCAN',
                        'works': 1093362},
    'executionSuccess': True,
    'executionTimeMillis': 1158,
    'nReturned': 23,
    'totalDocsExamined': 1093360,
    'totalKeysExamined': 0}
    {'allPlansExecution': [],
    'executionStages': {'advanced': 23,
                        'alreadyHasObj': 0,
                        'docsExamined': 23,
                        'executionTimeMillisEstimate': 0,
                        'inputStage': {'advanced': 23,
                                        'direction': 'forward',
                                        'dupsDropped': 0,
                                        'dupsTested': 0,
                                        'executionTimeMillisEstimate': 0,
                                        'indexBounds': {'tag': ['["italian '
                                                                'western", '
                                                                '"italian '
                                                                'western"]']},
                                        'indexName': 'tag_1',
                                        'indexVersion': 2,
                                        'isEOF': 1,
                                        'isMultiKey': False,
                                        'isPartial': False,
                                        'isSparse': False,
                                        'isUnique': False,
                                        'keyPattern': {'tag': 1},
                                        'keysExamined': 23,
                                        'multiKeyPaths': {'tag': []},
                                        'nReturned': 23,
                                        'needTime': 0,
                                        'needYield': 0,
                                        'restoreState': 0,
                                        'saveState': 0,
                                        'seeks': 1,
                                        'stage': 'IXSCAN',
                                        'works': 24},
                        'isEOF': 1,
                        'nReturned': 23,
                        'needTime': 0,
                        'needYield': 0,
                        'restoreState': 0,
                        'saveState': 0,
                        'stage': 'FETCH',
                        'works': 24},
    'executionSuccess': True,
    'executionTimeMillis': 5,
    'nReturned': 23,
    'totalDocsExamined': 23,
    'totalKeysExamined': 23}
    '''

if __name__ == '__main__':
    q1()

