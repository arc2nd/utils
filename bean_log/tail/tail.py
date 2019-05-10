#!/usr/bin/env python

import sys
import os
import platform


def find_offsets(infile):
    offsets = []
    while 1:
        offset = infile.tell()
        if not infile.readline():
            break
        offsets.append(offset)
    return offsets


def make_tail(log_path, lines):
    tail_str = []
    if os.path.exists(log_path): 
        with open(log_path, 'r') as fp:
            offsets = find_offsets(fp)
            tail_offsets = offsets[0-lines:]
            for entry in tail_offsets:
                fp.seek(entry)
                tail_str.append(fp.readline())
    return tail_str


if __name__ == '__main__':
    log_path = '/data/roll.log'
    # file_read_from_tail('/data/roll.log', 7)
    for l in make_tail(log_path, 7):
        print(l)
