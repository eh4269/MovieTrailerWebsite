#!/usr/bin/python
# -*- coding: utf-8 -*-

''' Define movies to be included on site '''

import media
import fresh_tomatoes

# Add movies in this section by looking up ID (id in url example https://www.themoviedb.org/movie/1891-the-empire-strikes-back)

Infinity_War = media.MyMovies(299536)

Avengers = media.MyMovies(24428)

Pirates = media.MyMovies(58)

Starwars = media.MyMovies(11)

IronMan = media.MyMovies(1726)

lastjedi = media.MyMovies(181808)

movies = [
    Starwars,
    Infinity_War,
    IronMan,
    Avengers,
    lastjedi,
    Pirates,
    ]

# Generate html website

fresh_tomatoes.open_movies_page(movies)


