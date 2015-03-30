#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import dbus

def pause():
  omxplayer_control = get_player()
  omxplayer_control.Action(dbus.Int32('16'))

def stop():
  omxplayer_control = get_player()
  omxplayer_control.Action(dbus.Int32('15'))

def vol_down():
  omxplayer_control = get_player()
  omxplayer_control.Action(dbus.Int32('17'))

def vol_up():
  omxplayer_control = get_player()
  omxplayer_control.Action(dbus.Int32('18'))

def get_player():
  with open('/tmp/omxplayerdbus.', 'r+') as f:
    omxplayerdbus = f.read().strip()

  bus = dbus.bus.BusConnection(omxplayerdbus)
  object = bus.get_object('org.mpris.MediaPlayer2.omxplayer','/org/mpris/MediaPlayer2', introspect=False)
  omxplayer_props = dbus.Interface(object,'org.freedesktop.DBus.Properties')
  omxplayer_control = dbus.Interface(object,'org.mpris.MediaPlayer2.Player')
  return omxplayer_control

