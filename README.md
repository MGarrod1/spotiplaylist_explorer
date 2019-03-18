## Comparing Playlists

Using Spotify’s API (via Spotipy) I have downloaded data about 1590 songs from 25 playlists across a range of genres. Each track includes details about the artists and their corresponding genres as well as a set of “audio features.” These features include: energy, danceability, loudness and several others deduced from audio analysis at Spotify.

The associated jupyter notebook includes two interactive plots:

1. PCA - in the first visualization we use [PCA](https://en.wikipedia.org/wiki/Principal_component_analysis) to reduce the dimension of the feature set down to 2 dimensions for visualization purposes. 

We tend to see different genres and playlists clustering together in this space. In the images below we see that the "chilled jazz" and "kickass metal" playlists occupy disjoint regions in the feature space - this is what we might expect!

![](https://github.com/MGarrod1/spotiplaylist_explorer/blob/master/Figures/spotipy_pca_example_1.png)

![](https://github.com/MGarrod1/spotiplaylist_explorer/blob/master/Figures/spotipy_pca_example_2.png)


2. Different features - in this visualization the user has the ability to choose which features appear on the x and y axis. This allows us to qualitatively explore the degree to which features may be correlated with each other. 

The image below illustrates that tracks made by artists within the 'funk rock' genre tend to be relatively energetic.

![](https://github.com/MGarrod1/spotiplaylist_explorer/blob/master/Figures/spotipy_features_example_1.png)

This analysis was partly inspired by that at the following blog post: https://medium.com/cuepoint/visualizing-hundreds-of-my-favorite-songs-on-spotify-fe50c94b8af3

Data: the data was scraped using the Spotify web API via [Spotipy](https://spotipy.readthedocs.io/en/latest/) on 18/03/19

## Dependencies: 
-  pandas
-  sklearn
-  seaborn


