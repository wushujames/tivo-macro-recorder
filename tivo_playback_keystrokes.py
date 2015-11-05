#!/usr/bin/python

import socket

tcd_keys = {
    'KEY_UP' : 'UP',
    'KEY_DOWN' : 'DOWN',
    'KEY_LEFT' : 'LEFT',
    'KEY_RIGHT' : 'RIGHT',
    'SELECT' : 'SELECT',
    't' : 'TIVO'
    }
    

def sendtcd(host, key):
    port = 31339

    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.connect((host, port))
    if key in tcd_keys:
        sock.send("IRCODE %s\r" % tcd_keys[key])
    
    sock.close()

import sys
import string
import time

if len(sys.argv) < 3:
    print "Usage: python tivo_playback_keystrokes.py <file-with-keystrokes> <tivo-ip-address>"
    sys.exit(1)

infile = sys.argv[1]
host = sys.argv[2]

f = open(infile)
for line in f:
    line = line.strip("\n")
    (waittime, key) = string.split(line, " ", 1)
    time.sleep(int(waittime))
    sendtcd(host, key)
