'''
    Chunk 2: Add subparsers — this is the actual new concept. argparse supports “subcommands”
    (add, view, delete, search) the same way git has git add vs git commit. Look up 
    parser.add_subparsers(). Get it so python notevault.py add and python notevault.py view are at
    least recognized as different commands, even before they do anything.
'''
import argparse

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(dest="command")

subparsers.add_parser("add")
subparsers.add_parser("view")

args = parser.parse_args()
print(args)