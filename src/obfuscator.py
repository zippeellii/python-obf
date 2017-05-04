"""
Usage: obfuscator.py [-o NAME] FILE...

Arguments:
    FILE        python file that should be obfuscated

Options:
    -o NAME     output into a file named NAME.i
"""

import docopt


def _rename_functions(src):
    """Hello."""
    pass


def _remove_comments(src):
    """Hello."""
    pass


def _add_fuzzed_code(src):
    """Hello."""
    for line in src:
        # Add random code to the line if contains none.
        if not line.trim():
            pass


def _random_ordering(src):
    """Hello."""
    pass


if __name__ == '__main__':
    try:
        args = docopt.docopt(__doc__)
        print "hello"
    except docopt.DocoptExit as e:
        print e.message
