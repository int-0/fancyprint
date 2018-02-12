#!/usr/bin/env python
#

def prepare(message):
    return str(message)

def get_size(message):
    message = message.splitlines()
    rows = len(message)
    columns = max([len(line) for line in message])
    return columns, rows
