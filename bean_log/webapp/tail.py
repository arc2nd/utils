#!/usr/bin/env python

import sys
import os

def tail(f, lines=20):
    total_lines_wanted = lines

    with open(f, 'r') as fp:
        BLOCK_SIZE = 1024
        fp.seek(0, 2)
        block_end_byte = fp.tell()
        lines_to_go = total_lines_wanted
        block_number = -1
        blocks = [] # blocks of size BLOCK_SIZE, in reverse order starting
                # from the end of the file
        while lines_to_go > 0 and block_end_byte > 0:
            if (block_end_byte - BLOCK_SIZE > 0):
                # read the last block we haven't yet read
                fp.seek(block_number*BLOCK_SIZE, 2)
                blocks.append(fp.read(BLOCK_SIZE))
            else:
                # file too small, start from begining
                fp.seek(0,0)
                # only read what was not read
                blocks.append(fp.read(block_end_byte))
            lines_found = blocks[-1].count('\n')
            lines_to_go -= lines_found
            block_end_byte -= BLOCK_SIZE
            block_number -= 1
        all_read_text = ''.join(reversed(blocks))
        return all_read_text.splitlines()[-total_lines_wanted:]
    #return '\n'.join(all_read_text.splitlines()[-total_lines_wanted:])


if __name__ == '__main__':
    log_path = '/data/roll.log'
    # file_read_from_tail('/data/roll.log', 7)
    for l in tail(log_path, 7):
        print(l)
