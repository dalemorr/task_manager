import argparse
import sqlite3
import sys

DB_NAME = 'task_manager'
IN_DEBUG_MODE = False
DESCRIPTION = 'example description'

def runQuery(outfilename, infile):
    query = infile.read()

    if not isValid(query):
        print('invalid query')
        return

    if IN_DEBUG_MODE:
        print(query)
        return
    
    connection = sqlite3.connect(f'./{outfilename}')
    cursor = connection.cursor()
    # cursor.execute(query)

    connection.commit()
    connection.close()


def isValid(query):
    return True


def main():
    parser = argparse.ArgumentParser(
        prog=DB_NAME,
        description=''
    )

    parser.add_argument('-o', '--output_file')
    parser.add_argument('-f', '--input_file')

    args = parser.parse_args()

    if args.output_file is None:
        outfilename = f'./{DB_NAME}.db'

    if args.input_file is None:
        infile = sys.stdin
    else:
        infile = open(args.input_file, 'r')
    
    runQuery(outfilename, infile)
    if infile != sys.stdin:
        infile.close()


if __name__ == '__main__':
    main()
