"""Usage: obfuscator.py [-o NAME] FILE...

Arguments:
    FILE        python file that should be obfuscated

Options:
    -o NAME     output into a file named NAME.i
"""

import docopt
import regex_patterns as patterns


def _rename_functions(src):
    """Hello."""
    pass


def _remove_comments(src):
    """Hello."""
    match = patterns.re_comments.search(src)
    if match:
        print match
        print src
        return ''
    return src


def _add_fuzzed_code(src):
    """Hello."""
    pass


def _random_ordering(src):
    """Hello."""
    pass

def _write_file(lines, name):
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

        for idx, line in enumerate(lines):
            lines[idx] = _remove_comments(line)

        _write_file(lines, output_name)
    except docopt.DocoptExit as e:
        print e.message
