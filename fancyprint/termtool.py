#!/usr/bin/env python
#

import os
import sys
import fcntl
import struct
import termios

def cursor_up(count):
    sys.stdout.write('\033[%sA' % count)

def cursor_down(count):
    sys.stdout.write('\033[%sB' % count)

def cursor_right(count):
    sys.stdout.write('\033[%sC' % count)

def cursor_left(count):
    sys.stdout.write('\033[%sD' % count)

def show_cursor(show):
    sys.stdout.write('\033[?25%s' % ('h' if show else 'l'))
    
def get_terminal_size():
    '''Implemented only for posix (for now)'''
    assert(os.name == 'posix')
    try:
        fd = os.open(os.ctermid(), os.O_RDONLY)
        height, width = struct.unpack(
            'hh',
            fcntl.ioctl(fd, termios.TIOCGWINSZ, '1234'))
        os.close(fd)
        return width, height
    except Exception as e:
        logging.error('Cannot get terminal size: %s' % e)
    return None, None

def put(chars, flush=True):
    sys.stdout.write(chars)
    if flush:
        sys.stdout.flush()

def clean_area(size):
    width, height = size
    for row in range(height):
        put('\n')
    cursor_up(height)
    
def update_terminal():
    sys.stdout.flush()
