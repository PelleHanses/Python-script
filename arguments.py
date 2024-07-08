#!/usr/bin/python3
'''
arguments.py

A function that handle arguments.
This file stops if not all required arguments are given, with an explanation.
You could also get the help screen by typing:
    ./arguments.py --help

The function can be included in other scripts like this:
    from arguments import main
    args = main()

'''

import argparse

def main():
    parser = argparse.ArgumentParser(description='Rip audio CD to MP3 files with metadata.')
    parser.add_argument('--title', type=str, required=True, help='Title of the tracks.')
    parser.add_argument('--artist', type=str, required=True, help='Artist name')
    parser.add_argument('--album', type=str, required=True, help='Album name')
    parser.add_argument("--output_dir", type=str, required=True, help="The output directory for processed mp3 files.")
    parser.add_argument("--verbose", type=int, default=0, help="Optional. Show more info. (0/1/2)")


    args = parser.parse_args()

    args.amy = args.amy.upper()
    return args


### Start
if __name__ == "__main__":
    args = main()
