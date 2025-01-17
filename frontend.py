

import sys

from resources import *
from frontend import *
from core import *

import cProfile

reader = None
scanner = None
ir = None


def scan(scanner: Scanner):
    """
    Scan the input file and print each token to stdout.
    """
    while True:
        c = scanner.get_token()

        if c:
            print_token(c)

            if c[TOK_ID] == ENDFILE_CAT:
                return

def parse(parser: Parser, p: bool):
    """
    Scan and parse the input file. If p is True, then report success/failure,
    otherwise print the internal representation.
    """
    parser.parse()

    if p:
        if not parser.errors:
            print("Parse succeeded, finding {0} ILOC operations.".format(parser.count))
        else:
            print("Parser found {0} syntax errors in {1} lines of input."
                  .format(parser.errors, parser.ln)
                  )

    else:
        parser.print_ir()


def help_handler():

    print("COMP 412, Fall 2019 Front End (lab 1)\n"
          "Command Syntax:\n"
          "\t./lab1_ref [flags] filename\n"
          "\n"
          "Required arguments:\n"
          "\tfilename  is the pathname (absolute or relative) to the input file\n"
          "\n"
          "Optional flags:\n"
          "\t-h       prints this message\n"
          "\t-s       prints tokens in token stream\n"
          "\t-p       invokes parser and reports on success or failure\n"
          "\t-r       prints human readable version of parser's IR\n"
          "\t-P       Enables profiling.")


def command_line_error(msg: str):
    """
    Prints error message to stderr, followed by printing correct command line usage to stdout.
    """
    error(msg, "Command Line Error")
    print("Correct Usage:")
    help_handler()


if __name__ == "__main__":
    argv = sys.argv[1:]

    p = False
    s = False
    r = False

    profile = False
    pr = None

    filename = None

    # Invalid
    if not len(argv):
        command_line_error("No command line arguments specified.")
        exit(1)
    else:
        while argv:
            arg = argv.pop(0)

            if arg == "-h":
                help_handler()
                exit(0)

            elif arg == "-p":
                if p or s or r:
                    error("Input should contain only one command line flag. "
                          "Defaulting to highest priority flag.")

                    if not r:
                        p, s = True, False

                else:
                    p = True

            elif arg == "-s":
                if p or s or r:
                    error("Input should contain only one command line flag. "
                          "Defaulting to highest priority flag.")

                else:
                    s = True

            elif arg == "-r":
                if p or r or s:
                    error("Input should contain only one command line flag. "
                          "Defaulting to highest priority flag.")

                    p, s = False, False

                r = True

            # profile
            elif arg == "-P":
                profile = True

            else:
                if filename is None:
                    filename = arg
                else:
                    command_line_error("Multiple file names/unrecognized flags provided.")
                    exit(1)

        # default behavior
        if not (p or r or s):
            p = True

        assert not argv, "Did not process all arguments"

        if filename is None: # no file name provided
            command_line_error("Must provide a valid file name.")
            exit(1)

    try:
        reader = FileReader(filename)
    except OSError as o:
        error("Unable to open file with name {0}, no operations performed.".format(filename))
        exit(1)


    # Initialize the profiler
    if profile:
        pr = cProfile.Profile()
        pr.enable()

    scanner = Scanner(fr=reader)

    # scan and print out results
    if s:
        scan(scanner)
    else:
        ir = InternalRepresentation()
        parser = Parser(scanner = scanner, ir = ir)

        parse(parser, p)

    # Creates profiler output
    if profile:
        pr.create_stats()
        pr.dump_stats("prof.prof")
        pr.print_stats(sort = 'tottime')
