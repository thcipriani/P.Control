#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import dbus
import os

playing = ['Playing', 'Paused']

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

def is_paused():
    try:
        props = get_props()
        return props.PlaybackStatus() == 'Paused'
    except dbus.DBusException:
        return False
    except IOError:
        return False

def is_playing():
    try:
        props = get_props()
        return props.PlaybackStatus() in playing
    except dbus.DBusException:
        return False
    except IOError:
        return False

def get_dbus():
    user = os.getenv('USER', '')
    with open('/tmp/omxplayerdbus.%s' % user, 'r+') as f:
        omxplayerdbus = f.read().strip()

    bus = dbus.bus.BusConnection(omxplayerdbus)
    object = bus.get_object('org.mpris.MediaPlayer2.omxplayer','/org/mpris/MediaPlayer2', introspect=False)
    omxplayer_props = dbus.Interface(object,'org.freedesktop.DBus.Properties')
    omxplayer_control = dbus.Interface(object,'org.mpris.MediaPlayer2.Player')
    return (omxplayer_props, omxplayer_control)


def get_player():
    _, omxplayer_control = get_dbus()
    return omxplayer_control

def get_props():
    omxplayer_props, _ = get_dbus()
    return omxplayer_props
