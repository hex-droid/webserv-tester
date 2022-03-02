import os, sys
sys.path.insert(1, '/Users/ztaouil/Projects/webserv-tester/tests/all.py')
import utils
import config
import all

def main():
	[f() for f in all.tests]

if __name__ == '__main__':
    main()
