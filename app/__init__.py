#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from flask import Flask, url_for

app = Flask(__name__)
from app import server
