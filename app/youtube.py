#!/usr/bin/env python2

import subprocess

def play(url):
  subprocess.Popen('omxplayer -z "$(youtube-dl -g "%s")"' % url, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
