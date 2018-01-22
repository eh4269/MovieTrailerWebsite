#!/usr/bin/python
# -*- coding: utf-8 -*-

''' Define Movie class and backend code to get attributes '''

import webbrowser

# change name of imported class to avoid conflict with our class

import tmdbsimple as tmdb

# tmdb API key from https://www.themoviedb.org/

tmdb.API_KEY = 'd61b563be061ff37040e0c4bb3146582'


class MyMovies(object):

    def __init__(self, movie_ID):
        movie = tmdb.Movies(movie_ID)

# Get details from the TMDB API wrapper tmdbsimple Movie Class

        response = movie.info()
        self.title = movie.title
        self.tagline = movie.tagline

# Get details from the TMDB API wrapper tmdbsimple Videos Class

        response = movie.videos()
        youtubeurl = 'https://www.youtube.com/watch?v='
        self.key = movie.results[0]['key']
        self.trailer_youtube_url = youtubeurl + self.key

# Get details from the TMDB API wrapper tmdbsimple Image Class

        response = movie.images()
        posterimageurl = 'https://image.tmdb.org/t/p/original'
        posterimagepath = movie.posters[0]['file_path']
        self.poster_image_url = posterimageurl + posterimagepath

# Get details from the TMDB API wrapper tmdbsimple release_dates Class

        response = movie.release_dates()
        self.release_year = movie.release_date


                
                

