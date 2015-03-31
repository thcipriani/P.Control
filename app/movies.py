#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import os
import json
import io
from glob import glob
import subprocess

movie_json_file = '/tmp/movies.json'
movie_path = '/home/pi/Media'

def generate_json():
    matches = []
    count = 0
    match_file = movie_json_file
    for root, dirnames, filenames in os.walk(movie_path):
        for name in filenames:
            if name.endswith('mkv') or name.endswith('mp4') or name.endswith('avi'):
                matches.append({
                    'id': count,
                    'name': name.decode('utf-8'),
                    'path': os.path.join(root, name).decode('utf-8')
                })
                count += 1

    with io.open(match_file, 'w', encoding='utf-8') as f:
        f.write(unicode(json.dumps(matches, indent=4, ensure_ascii=False)))

def find_movies():
    try:
        with open(movie_json_file, 'r+') as f:
            movies = json.loads(f.read())
    except IOError:
        generate_json()
        with open(movie_json_file, 'r+') as f:
            movies = json.loads(f.read())

    return movies

def get_movie_path(movie_id):
    movies = find_movies()

    for name in movies:
        if name['id'] == movie_id:
            return name['path']

def play_movie(movie_id):
    path = get_movie_path(movie_id)
    subprocess.Popen('/usr/local/bin/play "%s"' % path, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

if __name__ == '__main__':
    generate_json()
