#!/usr/bin/env python3

import argparse
from funcs.init import init
from funcs.run import run

# argparse
parser = argparse.ArgumentParser(prog='DesktopStudio', description='A docker-based studio for your linux configs and enviroments', epilog='by s7lver')

parser.add_argument('action')
parser.add_argument('-s', '--script')                        # positional argument
parser.add_argument('-v', '--verbose', action='store_true')  # on/off flag

args = parser.parse_args()

if __name__ == "__main__":
    if args.action == "init":
        init()
    if args.action == "run":
        run(args.script)