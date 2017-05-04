"""
Usage: obfuscator.py [-o NAME] FILE...

Arguments:
    FILE        python file that should be obfuscated

Options:
    -o NAME     output into a file named NAME.i
"""

import docopt
import logging
import random

import regex_patterns as patterns

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def _rename_functions(src):
    """Hello."""
    pass


def _remove_comments(src):
    """Hello."""
    match = patterns.re_comments.search(src)
    # We have a comment
    if match:
        return ''
    return src


def _add_fuzzed_code(src):
    """
    Add random function and variable declarations on empty lines.

    The functions and variables will never be referenced but will be obfuscated
    like everything else to create confusion.
    """
    with open('data/random_code.py', 'r') as f:
        random_code = f.read()

    random_functions = random_code.split('def')
    random_functions = filter(None, random_functions)  # Remove empty strings
    random_functions = map(lambda x: 'def' + x, random_functions)  # Fix: ugly
    random_functions = map(lambda x: x.split('\n'), random_functions)

    def leading_spaces(s):
        return len(s) - len(s.lstrip())

    new_src = []
    for idx, line in enumerate(src):
        # Add random code to the line if it does not containg anything. Retain
        # identation.
        if line.strip():
            new_src.append(line)
            continue

        logging.info('Inserting random code on line %s', len(new_src))
        fun_lines = random.choice(random_functions)

        indent = ' ' * leading_spaces(src[idx - 1])
        for fun_line in fun_lines:
            new_src.append(indent + fun_line + '\n')

    return new_src


def _random_ordering(src):
    """Hello."""
    pass


def _write_file(lines, name):
    """Write all lines to a file."""
    out_file = open(name, 'w')
    for line in lines:
        out_file.write(line)


if __name__ == '__main__':
    try:
        args = docopt.docopt(__doc__)
        output_name = args['-o'] or 'obfuscated.py'
        file = open(args['FILE'][0])

        lines = []
        for line in file:
            lines.append(line)

        lines = _add_fuzzed_code(lines)
        for idx, line in enumerate(lines):
            lines[idx] = _remove_comments(line)

        _write_file(lines, output_name)
    except docopt.DocoptExit as e:
        print e.message
