import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


##Step 1: data preprocessing
df = pd.read_csv("movie_dataset.csv")
#print df.columns
##Select Features
features = ['keywords','cast','genres','director']

##Create a column in DF which combines all selected features
for feature in features:
    df[feature] = df[feature].fillna(' ')
    
def combine_features(row):
    try:
        return row['keywords']+" "+row['cast'] + " "+ row['genres']+ " "+ row['director']
    except:
        print "Error:" , row

df["combined_features"] = df.apply(combine_features,axis=1)
#print "Combined_features :\n",df["combined_features"].head()


##Create count matrix from this new combined column
cv = CountVectorizer()
count_matrix = cv.fit_transform(df["combined_features"]).toarray()

##Cosine Similarity based on the count_matrix
cosine_distance = cosine_similarity(count_matrix)
#print(type(cosine_distance[0]))

movie_user_likes = "Avatar"

##index of this movie from its title
index = df.original_title[df.original_title == movie_user_likes].index[0]
##list of similar movies in descending order of similarity score
similarity = np.sort(cosine_distance[index])[::-1]

##Printing titles of first 50 movies
index_movies = np.zeros((1,50))
for i in range(50):
    index_movies[0][i] = np.argmax((similarity[i] == cosine_distance[0]).astype(int))

for i in range(50):
    print df.loc[index_movies[0][i],'original_title']

