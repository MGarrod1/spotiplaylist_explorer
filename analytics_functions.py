"""

Functions used for processing data obtained
from the Spotify API using spotipy.

Matthew Garrod

"""

import ast
import operator
import numpy as np


def data_frame_to_dict(df):
	
	"""

	convert pandas data frame to a dictionary

	Parameters
	-----------

	df : pandas dataframe

	Returns
	-----------

	data_dict : dict

	"""
	column_nums = np.asarray(df.columns[0:])
	matrix = df.as_matrix()

	matrix_transpose = np.transpose(matrix)
	data_dict = {}

	for k in range(len(column_nums)):
		data_dict[column_nums[k]] = matrix_transpose[k]

	return data_dict



def normalize(list_vals):
	return [(i - min(list_vals)) / (max(list_vals) - min(list_vals)) for i in list_vals]


def dict_to_feature_vectors(audio_feat_dict):
	feature_vectors = []
	column_headers = []
	for key, value in audio_feat_dict.items():
		if isinstance(value[0], float):
			column_headers.append(key)
			normalized = normalize(list(value))
			feature_vectors.append(normalized)

	return column_headers, feature_vectors



def make_genres_categorical(data_dict, return_genre_list=False):
	"""

	Adds an extra key to the dictionary for each genre contained
	in the dataset

	Parameters
	------------

	data_dict : dict

	Dictionary containing 'genres' as a key.
	-Expect data_dict['genres'] to be a list of strings
	or a list of lists of strings in the case of multiple
	artists.

	Returns
	-------------

	data_dict : dict

	dictionary with extra keys for each genre
	e.g if 'rock' is a genre there will now be
	a new value: data_dict['rock'] = [ 0 , 0 , 1, ..., 0 ]
	which takes a value of 1 for tracks which posses that genre.


	"""
	all_genres = []
	for k in range(len(data_dict['genres'])):

		gen_list = ast.literal_eval(data_dict['genres'][k])

		# Some artists are assigned no genre:
		if len(gen_list) == 0:
			gen_list.append('None')

		# For multiple artists genres is a list of lists:
		if isinstance(gen_list[0], list):
			gen_list = []
			for list_element in gen_list:
				ast.literal_eval(list_element)
				gen_list = np.concatenate((gen_list, list_element))

		#Add the genre if it has not been previously included:
		for genre in gen_list:
			if genre not in data_dict.keys():
				data_dict[genre] = np.zeros(len(data_dict['genres']))
				data_dict[genre][k] = 1
				all_genres.append(genre)
			else:
				data_dict[genre][k] = 1

	if return_genre_list == False:
		return data_dict
	else:
		return data_dict, all_genres



def make_playlists_categorical(data_dict, return_playlist_list=False):

	"""


	Adds an extra key to the dictionary for each playlist contained
	in the dataset

	Parameters
	------------

	data_dict : dict

	Returns
	-------------

	data_dict : dict

	"""


	all_playlists = []
	for k in range(len(data_dict['playlist'])):

		playlist = data_dict['playlist'][k]

		if playlist not in data_dict.keys():
			data_dict[playlist] = np.zeros(len(data_dict['playlist']))
			data_dict[playlist][k] = 1
			all_playlists.append(playlist)
		else:
			data_dict[playlist][k] = 1

	if return_playlist_list == False:
		return data_dict
	else:
		return data_dict, all_playlists



def get_top_genres(data_dict,all_genres,threshold=0.2) :

	"""
	Screen out genres which are uncommon.

	By default we screen out genres which
	occur less than threshold*MAX_GEN where
	MAX_GEN is the most commonly occuring
	genre.


	Parameters
	------------

	data_dict : dict

	all_genres : list

	list of strings containing all of the
	genres within the dataset

	threshold : float (optional)

	sets the threshold for screening out rare genres


	Returns
	------------

	selected_genres : list

	list of strings containing the most commonly
	occuring genres.

	"""

	genre_counts = []
	for genre in all_genres:
		genre_counts.append(np.sum(data_dict[genre]))

	sorted_list = sorted(zip(all_genres, genre_counts), key=operator.itemgetter(1))
	
	selected_genres = []
	for k in sorted_list:
		if k[1] > int( max(genre_counts)*threshold ):
			selected_genres.append(k[0])

	return selected_genres