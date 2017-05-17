"""Python Obfuscator.

Usage:
    obfuscator.py [-o NAME] [-k KEY] [--quiet | --verbose | --encrypt] FILE...
    obfuscator.py (-h | --help)
    obfuscator.py --version

Arguments:
    FILE        python file that should be obfuscated

Options:
    -o NAME     output into a file named NAME
    -k KEY      decrypt file with KEY
"""

# TODO: Do not troll with strings that can contain variable names
import logging
import os
import random
import re

from subprocess import check_output

import docopt

import encryption

import regex_patterns as patterns

import utils

function_mapper = dict()
variable_mapper = dict()

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('python-obf')


def _rename_functions(src):
    match = patterns.re_function.search(src)
    if match:
        new_name = utils.gen_random_name()
        function_mapper[match.group(0)] = new_name
        return re.sub(r'(def )' + match.group(0), r'\1' + new_name, src)
    return src


def _rename_function_calls(src):
    words = re.split(r'(\')', src)
    found_quote = False
    new_str = ''
    for w in words:
        if w == "'":
            new_str += "'"
            found_quote = not found_quote
            continue
        if not found_quote:
            for name, mapped in function_mapper.iteritems():
                if name in w:
                    w = re.sub(
                        (r'(?<![a-zA-Z_])' + name + r'(?![a-zA-Z0-9_])'),
                        mapped,
                        w
                    )
        new_str += w
    return new_str


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
        name = variable_mapper.get(match.group(1)) or utils.gen_random_name()
        variable_mapper[match.group(1)] = name
        return re.sub(r'(\w+)( =)', name + r'\2', src)
    return src


def _rename_variable_usage(src):
    words = re.split(r'(\')', src)
    found_quote = False
    new_str = ''
    for w in words:
        if w == "'":
            new_str += "'"
            found_quote = not found_quote
            continue
        if not found_quote:
            for name, mapped in variable_mapper.iteritems():
                if name in w:
                    w = re.sub(
                        r'(?<![a-zA-Z_])' + name + r'(?![a-zA-Z0-9_])',
                        mapped,
                        w
                    )
        new_str += w
    return new_str


def _add_fuzzed_code(src):
    """
    Add random function and variable declarations on empty lines.

    The functions and variables will never be referenced but will be obfuscated
    like everything else to create confusion.
    """
    data_dir = os.path.join(os.path.dirname(__file__), '..', 'data')
    with open(data_dir + '/random_code.py', 'r') as f:
        random_code = f.read()

    # Find all functions in the file and get the code for each one of them
    random_functions = random_code.split('def')
    random_functions = filter(None, random_functions)  # Remove empty strings
    random_functions = ['def' + f for f in random_functions]
    random_functions = [f.split('\n') for f in random_functions]
    # List comprehensions are preferred over map lambdas
    
    # random_functions = map(lambda x: 'def' + x, random_functions)  # Fix: ugly
    # random_functions = map(lambda x: x.split('\n'), random_functions)

    def leading_spaces(s):
        """Calculate how many spaces a line is indented with."""
        return len(s) - len(s.lstrip())

    new_src = []
    in_comment_block = False
    for idx, line in enumerate(src):
        # Add random code to the line if it does not containg anything. Retain
        # identation.
        if '\"\"\"' in line:
            in_comment_block = not in_comment_block

        # We do not wanna add code within a comment block. It will create
        # syntax errors.
        if in_comment_block:
            new_src.append(line)
            continue

        # Fetch how much previous line is indented
        leads = leading_spaces(src[idx - 1])

        # If previous line is beginning of a block we have to add som addtional
        # identation. Assuming its pep8 compliant, so we use 4 spaces
        if src[idx - 1].strip() and src[idx - 1].rstrip()[-1] == ':':
            leads += 4

        # Some lines have one space in them so we do some magic to compensate
        indent = ' ' * (leads - leads % 2)

        # Randomly decide if we should add a random variable to the code. It
        # will never be referenced by any code.
        if src[idx - 1].strip() and random.random() > 0.5:
            # TODO: This actually puts random variable assignments in multi line
            # function calls making the call become a keyword call. 
            name = utils.gen_random_name()
            num = str(random.randint(-10000, 10000))
            dec = str(random.random())
            chars = '\'' + utils.gen_random_name() + '\''
            val = random.choice([num, dec, chars])
            new_src.append(indent + name + ' = ' + val + '\n')

        if line.strip():
            new_src.append(line)
            continue

        logger.info('Inserting random code on line %s', len(new_src))

        # Pick a random function to insert
        fun_lines = random.choice(random_functions)

        # Append each line of the function with correct indentation
        for fun_line in fun_lines:
            new_src.append(indent + fun_line + '\n')

    return new_src


def _replace_constants(src):
    """Hello."""
    pass


def _redefine_stdlib(src):
    pass


def _write_file(lines, name):
    """Write all lines to a file."""
    out_file = open(name, 'w')
    for line in lines:
        out_file.write(line)


def _main():
    try:
        args = docopt.docopt(__doc__)

        if args['--version']:
            git_hash = check_output(['git', 'rev-parse', '--verify', '--short', 'HEAD'])
            print "Python obfuscator 1.3.3.7-%s" % git_hash
            return

        encrypt = False

        if args.get('--verbose'):
            logging.basicConfig(level=logging.NOTSET)
        if args.get('--quiet'):
            logging.basicConfig(level=logging.ERROR)
        if args.get('--encrypt'):
            encrypt = True

        file = open(args['FILE'][0])
        file_name = args['FILE'][0].split('/')[-1].split('.')[0]
        output_name = args['-o'] or file_name + '_obfuscated.py'
        decrypt_key = args['-k'] or None
        enc_key = None
        lines = []
        for line in file:
            lines.append(line)
        if decrypt_key:
            for idx, _ in enumerate(lines):
                lines[idx] = encryption.decrypt_string(lines[idx], decrypt_key)
            code = ''.join(line for line in lines)
            # This only exists for testing purposes
            _write_file(lines, output_name)

            # exec code

        else:
            enc_key = encryption.generate_key()
            lines = _add_fuzzed_code(lines)
            for idx, _ in enumerate(lines):
                lines[idx] = _remove_comments(lines[idx])
                lines[idx] = _rename_functions(lines[idx])
                lines[idx] = _rename_function_calls(lines[idx])
                lines[idx] = _rename_variables(lines[idx])
            for idx, _ in enumerate(lines):
                lines[idx] = _rename_variable_usage(lines[idx])
                if encrypt:
                    lines[idx] = encryption.encrypt_string(lines[idx], enc_key)
            _write_file(lines, output_name)

        if encrypt and enc_key:
            print 'Encryption key is:', enc_key
    except docopt.DocoptExit as e:
        print e.message


if __name__ == '__main__':
    _main()
