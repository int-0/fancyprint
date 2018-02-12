#!/usr/bin/env python
#

import time
import random

import termtool
import messagetool


DEFAULT_CURSOR = unichr(0x2588)


def typing(message,
           per_char_wait=0.01, random_factor=0.5, endline_wait=0.7,
           emulated_cursor=DEFAULT_CURSOR):
    message = messagetool.prepare(message)
    size = messagetool.get_size(message)
    termtool.show_cursor(False)
    termtool.clean_area(size)
    for line in message.splitlines():
        for char in line:
            time.sleep(per_char_wait + (random.random() * random_factor))
            termtool.put('%s%s' % (char, emulated_cursor))
            termtool.cursor_left(len(emulated_cursor))
        termtool.put(emulated_cursor)
        time.sleep(endline_wait)
        termtool.cursor_left(len(emulated_cursor))
        termtool.put(' \n')
    termtool.show_cursor(True)
    termtool.update_terminal()


def human_type(message):
    typing(message, per_char_wait=0.05, random_factor=0.4, endline_wait=0.8)

def computer_type(message):
    typing(message, per_char_wait=0.05, random_factor=0, endline_wait=0.5)
    
