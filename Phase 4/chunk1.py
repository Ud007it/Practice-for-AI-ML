'''
    Chunk 1: Import argparse, create a parser, and get just python notevault.py view
    working — no subcommands yet, just prove you can run the script with an argument and have 
    Python see it. Look up argparse.ArgumentParser() and parser.parse_args(), print whatever it 
    returns, understand what you’re looking at before adding complexity.
'''

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("action")

args = parser.parse_args()
print(args)