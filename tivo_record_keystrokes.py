#!/usr/bin/python

import curses
import curses.ascii
import curses.wrapper
import datetime
import socket

#stdscr = curses.initscr()
#curses.cbreak()
#stdscr.keypad(1)

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
if len(sys.argv) < 2:
    print "Usage: tivo_record_keystrokes.py <tivo-ip-address>"
    sys.exit(1)

host = sys.argv[1]

captured = []
def doit(stdscr):
    #    curses.echo()
    while 1:
        start = datetime.datetime.utcnow()
        c = stdscr.getch()
        end = datetime.datetime.utcnow()

        if c == ord('q'): break  # Exit the while()
        delta = end - start + datetime.timedelta(seconds = 1)
#        print curses.ascii.ascii(c)
#        print c
        key = curses.keyname(c)
        if key == ' ':
            key = 'SELECT'
        print str(delta) + " " + key + "\r"
        captured.append((str(delta.seconds), key))
#        print curses.unctrl(c)
        curses.doupdate()
        sendtcd(host, key)

    
curses.wrapper(doit)

for i,key in captured:
    print i, key


