## Comparing Playlists

Using Spotify’s API (via Spotipy) I have downloaded data about 1590 songs from 25 playlists across a range of genres. Each track includes details about the artists and their corresponding genres as well as a set of “audio features.” These features include: energy, danceability, loudness and several others deduced from audio analysis at Spotify.

The associated jupyter notebook includes two interactive plots:

1. PCA - in the first visualization we use PCA (link) to reduce the dimension of the feature set down to 2 dimensions for visualization purposes. We tend to see different genres and playlists clustering together in this space.

2. Different features - in this visualization the user has the ability to choose which features appear on the x and y axis. This allows us to qualitatively explore the degree to which features may be correlated with each other. 

This analysis was partly inspired by that at the following blog post: https://medium.com/cuepoint/visualizing-hundreds-of-my-favorite-songs-on-spotify-fe50c94b8af3

Data: the data was scraped using the web API on 18/03/19

## Dependencies
-pandas
-sklearn
-seaborn

