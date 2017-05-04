"""
Usage: obfuscator.py [-o NAME] FILE...

Arguments:
    FILE        python file that should be obfuscated

Options:
    -o NAME     output into a file named NAME.i
"""

import docopt
import logging
import os
import random

import regex_patterns as patterns
import utils
import re

function_mapper = dict()
variable_mapper = dict()

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def _rename_functions(src):
    match = patterns.re_function.search(src)
    if match:
        new_name = utils.gen_random_name()
        function_mapper[match.group(0)] = new_name
        return re.sub(r'(def )' + match.group(0), r'\1' + new_name, src)
    return src


def _rename_function_calls(src):
    for name, m in function_mapper.iteritems():
        if name in src:
            src = re.sub(r'(.*)' + name + r'(.*)', r'\1' + m + r'\2', src)
    return src


def _remove_comments(src):
    """Hello."""
    match = patterns.re_comments.search(src)
    # We have a comment
    if match:
        return ''
    return src


def _rename_variables(src):
    match = patterns.re_var_assignment.search(src)
    if match:
        new_name = utils.gen_random_name()
        variable_mapper[match.group(1)] = new_name
        return re.sub(r'(\w+)( =)', new_name + r'\2', src)
    return src


def _rename_variable_usage(src):
    for n, m in variable_mapper.iteritems():
        if n in src:
            logger.debug('Found variable usage')
            src = re.sub(r'(.*)' + n + r'([.[, :)])', r'\1' + m + r'\2', src)
            logger.debug(src)
    return src


def _add_fuzzed_code(src):
    """
    Add random function and variable declarations on empty lines.

    The functions and variables will never be referenced but will be obfuscated
    like everything else to create confusion.
    """
    data_dir = os.path.join(os.path.dirname(__file__), '..', 'data')
    with open(data_dir + '/random_code.py', 'r') as f:
        random_code = f.read()

    random_functions = random_code.split('def')
    random_functions = filter(None, random_functions)  # Remove empty strings
    random_functions = map(lambda x: 'def' + x, random_functions)  # Fix: ugly
    random_functions = map(lambda x: x.split('\n'), random_functions)

    def leading_spaces(s):
        return len(s) - len(s.lstrip())

    new_src = []
    in_comment_block = False
    for idx, line in enumerate(src):
        # Add random code to the line if it does not containg anything. Retain
        # identation.
        if '\"\"\"' in line:
            in_comment_block = not in_comment_block

        if line.strip() or in_comment_block:
            new_src.append(line)
            continue

        logging.info('Inserting random code on line %s', len(new_src))

        # Pick a random function to insert
        fun_lines = random.choice(random_functions)

        leads = leading_spaces(src[idx - 1])
        # Some lines have one space in them so we do some magic to compensate
        indent = ' ' * (leads - leads % 2)

        # Append each line of the function with correct indentation
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
        file = open(args['FILE'][0])
        file_name = args['FILE'][0].split('/')[-1].split('.')[0]
        output_name = args['-o'] or file_name + '_obfuscated.py'

        lines = []
        for line in file:
            lines.append(line)

        lines = _add_fuzzed_code(lines)

        for idx, _ in enumerate(lines):
            lines[idx] = _remove_comments(lines[idx])
            lines[idx] = _rename_functions(lines[idx])
            lines[idx] = _rename_function_calls(lines[idx])
            lines[idx] = _rename_variables(lines[idx])
            lines[idx] = _rename_variable_usage(lines[idx])

        _write_file(lines, output_name)
    except docopt.DocoptExit as e:
        print e.message
