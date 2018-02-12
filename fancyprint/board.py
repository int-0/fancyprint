#!/usr/bin/env python
#

import time
import random

import termtool
import messagetool

_FIRST_ASCII_ = 32
_CRYPT_ = [chr(i) for i in range(_FIRST_ASCII_, 100)]

def airport(message, switch_wait=0.05):
    message = messagetool.prepare(message)
    size = messagetool.get_size(message)

    current_char = [_FIRST_ASCII_] * len(message)
    # Dont play with special characters
    idx = 0
    for char in message:
        if ord(char) < _FIRST_ASCII_:
            current_char[idx] = ord(char)
        idx += 1

    termtool.show_cursor(False)
    termtool.clean_area(size)

    drawing_board = True
    while drawing_board:
        some_changes = False
        idx = 0
        for char in message:
            termtool.put(chr(current_char[idx]), flush=False)
            if current_char[idx] < ord(message[idx]):
                current_char[idx] += 1
                some_changes = True
            idx += 1
        termtool.put('\n')
        termtool.cursor_up(size[1])
        time.sleep(switch_wait)
        if not some_changes:
            drawing_board = False
    termtool.cursor_down(size[1])
    termtool.show_cursor(True)
    termtool.update_terminal()


def live_decrypt(message, switch_wait=0.05, max_tries=50, random_factor=2.0):
    message = messagetool.prepare(message)
    size = messagetool.get_size(message)

    char_try = [0] * len(message)

    termtool.show_cursor(False)
    termtool.clean_area(size)

    drawing_board = True
    while drawing_board:
        some_changes = False
        idx = 0
        for char in message:
            if (ord(char) < _FIRST_ASCII_) or (char_try[idx] > max_tries):
                termtool.put(char, flush=False)
            else:
                char_try[idx] += int(random_factor * random.random())
                termtool.put(random.choice(_CRYPT_), flush=False)
                some_changes = True
            idx += 1
        termtool.put('\n')
        termtool.cursor_up(size[1])
        time.sleep(switch_wait)
        if not some_changes:
            drawing_board = False
    termtool.cursor_down(size[1])
    termtool.show_cursor(True)
    termtool.update_terminal()
