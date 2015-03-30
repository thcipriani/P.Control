#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import os
from glob import glob
import subprocess

# TODO. This is awful
def findMovies():
    movies = []
    movies.extend(glob('/home/pi/Media/*/*.mkv'))
    movies.extend(glob('/home/pi/Media/*.mkv'))
    movies.extend(glob('/home/pi/Media/*/*.mp4'))
    movies.extend(glob('/home/pi/Media/*.mp4'))
    movies.extend(glob('/home/pi/Media/*/*.avi'))
    movies.extend(glob('/home/pi/Media/*.avi'))

    return movies

def getMovies():
    movies = findMovies()
    names = []

    for name in movies:
        names.append(os.path.basename(name))

    names.sort()
    return names

def getMoviePath(movie):
    movies = findMovies()

    for name in movies:
        if movie == os.path.basename(name):
            return name

def playMovie(movie):
    print movie
    path = getMoviePath(movie)
    print path
    subprocess.Popen('omxplayer -z "%s"' % path, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

