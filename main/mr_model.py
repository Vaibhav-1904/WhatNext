# Content-Based Movie Recommendations System
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from imdb import IMDb

###### helper functions. Use them when needed #######

def get_title_from_index(index):
	df = pd.read_csv('main/movie_dataset_IMDB.csv')
	return df[df.index == index]["title"].values[0]

def get_index_from_title(title):
	df = pd.read_csv('main/movie_dataset_IMDB.csv')
	return int(df[df.title == title]["index"].values[0])

def combine_features(row):
	try:
		return row['keywords'] + " " + row['cast'] + " " + row['genres'] + " " + row['director']
	except:
		print("Error : ", row)

def create_model():
	df = pd.read_csv('main/movie_dataset_IMDB.csv')
	features = ['genres', 'cast', 'director', 'keywords']

	for i in features:
		df[i] = df[i].fillna('')

	df["combined_features"] = df.apply(combine_features, axis=1)

	cv = CountVectorizer()
	count_matrix = cv.fit_transform(df["combined_features"])

	cosine_simi = cosine_similarity(count_matrix)

	return (cosine_simi, df)


def getRecommendations(name):
	ia = IMDb()
	search = ia.search_movie(name)
	movie_index = search[0].movieID
	movie = ia.get_movie(movie_index)

	# movies = ia.search_movie(name)
	# movie = movies[0]
	# index = get_index_from_title(movie.title)

	df, cosine_simi = create_model()
	similar_movies = list(enumerate(cosine_simi[movie_index]))
	sorted_similar_movies = sorted(similar_movies, key=lambda x:x[1], reverse = True)# lambda x[1] specifies the similarity value in 'similar_movies'

	j = 0
	for i in sorted_similar_movies:
		movieName = get_title_from_index(i[0])
		search = ia.search_movie(movieName)
		if search == []:
			continue
		movie_index = search[0].movieID
		movie = ia.get_movie(movie_index)

		print(movie['title'])
		print(movie['cover url'])

		j = j + 1
		if j > 10:
			break

	return sorted_similar_movies

	# i = 0
	# for element in sorted_similar_movies:
	# 	print(get_title_from_index(element[0]))
	# 	i=i+1
	# 	if i>50:
	# 		break

	