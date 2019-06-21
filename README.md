# Movie-Recommendation-System

<b>Implemented a recommendation system for movies using content based filtering.</b>

In content based filtering, we suggest movies based on the content that the user prefers and then finding out similar movies using techniques like <b><i>cosine distance</b></i> and <b><i>Euclidean distance</b></i>.

We have used cosine angle method to estimate the similarity between the two documents as it has its own advantages over Euclidean distance for avoiding false positives associated with uneven documents.

<b>Libraries used:-</b>

* pandas
* numpy
* sklearn.feature_extraction 
* sklearn.pairwise

Features considered	: <u>keywords,cast,genres,director</u>

The provided dataset contains lots of other features as well. So, if one wants to use other features, feel free to do so.
