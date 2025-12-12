import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
def Get_Recommendation(Target_user,n,m):

    movies = pd.read_csv('dataset/u.item' , sep='|' , header=None , encoding='latin-1', usecols=[0,1] , names=['Item Id' , 'Title'])

    column_name = ["User Id","Item Id","Rating","TimeStamp"]
    rating = pd.read_csv('dataset/u.data' , sep='\t' ,names=column_name)


    user_rating_matrix = rating.pivot(index='User Id' , columns='Item Id' , values='Rating')
    user_rating_matrix_filled = user_rating_matrix.fillna(0)


    user_similarity = cosine_similarity(user_rating_matrix_filled)

    user_simmilarity_df = pd.DataFrame(user_similarity, index=user_rating_matrix_filled.index , columns=user_rating_matrix_filled.index)

    similar_user= user_simmilarity_df[Target_user].sort_values(ascending=False)
    most_similar_user = similar_user.index[1:n]


    unrated_movies_of_target_user = user_rating_matrix.loc[Target_user][user_rating_matrix.loc[Target_user].isna()].index

    predict_rating = {}

    for movie in unrated_movies_of_target_user:

        movie_rating = user_rating_matrix.loc[most_similar_user,movie]
        similarity = similar_user[most_similar_user]

        mask = movie_rating.notna()

        numerator = (movie_rating[mask]*similarity[mask]).sum()
        denominator= similarity[mask].sum()

        predicted_rating = numerator/denominator if denominator !=0 else 0

        predict_rating[movie] = predicted_rating


    recommendation = sorted(predict_rating.items() , key=lambda x: x[1], reverse=True)[:m]
    final_output = [(movies[movies['Item Id'] == movie_id]['Title'].values[0], rating) for movie_id, rating in recommendation]


    print(final_output)

while(True):
    x = input("Press any Key to enter Else type EXIT to exit: ")
    if(x == "EXIT"):
        break
    else:
        Target_user = int(input("Enter ID of Target user: "))
        n = int(input("From how many user you want to recommendation: "))
        x = int(input("How many movies you want: "))

        Get_Recommendation(Target_user , n,x)


