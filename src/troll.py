"""Usage: obfuscator.py [-o NAME] FILE...

Arguments:
    FILE        python file that should be obfuscated

Options:
    -o NAME     output into a file named NAME.i
"""

import docopt
import regex_patterns as patterns
import utils

function_mapper = dict()


def akjlkqce(src):
    match = patterns.re_function.search(src)
    if match:
        new_name = utils.gen_random_name()
        function_mapper[match.group(0)] = new_name
        return src.replace(match.group(0), new_name)
    return src

def erljrpnq(src):
    for name, mapped_name in function_mapper.iteritems():
        if name in src:
            return src.replace(name, mapped_name)
    return src


def ooerimdc(src):
    """Hello."""
    match = patterns.re_comments.search(src)
    # We have a comment
    if match:
        return ''
    return src


def injucgkt(src):
    """Hello."""
    pass


def tiijcoad(src):
    """Hello."""
    pass

def ukqfndfk(lines, name):
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
            lines[idx] = ooerimdc(line)
            lines[idx] = akjlkqce(line)
            lines[idx] = erljrpnq(line)

        ukqfndfk(lines, output_name)
    except docopt.DocoptExit as e:
        print e.message
