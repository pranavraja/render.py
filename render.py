#!/usr/bin/env python
import sys
import argparse

parser = argparse.ArgumentParser(description='Apply a format transform to stdin')
parser.add_argument('inputfile', nargs='?', type=argparse.FileType('r'), default=sys.stdin, help='Input string (default stdin)')
parser.add_argument('-f', '--format', help='Format string')
parser.add_argument('-d', '--delimiter', default='\t', help='Delimiter (default TAB)')
parser.add_argument('-s', '--skip-first', action='store_true', default=False, help='Skip the first line of input (default False)')
args = parser.parse_args()

if args.skip_first: args.inputfile.next()
for line in args.inputfile:
    if not args.format:
        sys.stdout.write(line)
        continue
    sys.stdout.write(args.format.format(*line.split(args.delimiter)))
