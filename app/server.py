#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import os
import sys
reload(sys)
sys.setdefaultencoding('utf8')

from app import app, movies, omxplayer_control, youtube
from flask import render_template, redirect, url_for, request, send_from_directory
from datetime import datetime

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                            'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/')
def index():
    data = {
        'playing': omxplayer_control.is_playing(),
        'paused': omxplayer_control.is_paused()
    }
    return render_template('index.html', **data)

@app.route('/movies')
def get_movies():
    data = {
        'movies': movies.find_movies()
    }
    return render_template('get_movies.html', **data)

@app.route('/regen_movies')
def regen_movies():
    movies.generate_json()
    return redirect(url_for('index'))

@app.route('/play/<int:movie_id>')
def play(movie_id):
    movies.play_movie(movie_id)
    return redirect(url_for('index'))

@app.route('/pause')
def pause():
    omxplayer_control.pause()
    return redirect(url_for('index'))

@app.route('/stop')
def stop():
    omxplayer_control.stop()
    return redirect(url_for('index'))

@app.route('/vol_down')
def vol_down():
    omxplayer_control.vol_down()
    return redirect(url_for('index'))

@app.route('/vol_up')
def vol_up():
    omxplayer_control.vol_up()
    return redirect(url_for('index'))

@app.route('/youtube', methods=['GET', 'POST'])
def youtube_it():
    if request.method == 'POST':
        youtube.play(request.form['url'])
        return redirect(url_for('index'))

    return render_template('youtube.html')
