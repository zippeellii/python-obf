import fileinput
import re
import utils

file = fileinput.input()
obf_file = open('output/obf.py', 'w')
mapping = dict()

lines = []

for line in file:
    lines.append(line)
    # See if line includes a function definiton
    m = re.search('(?<=def )\w+', line)
    # See if line includes a variable instanciate 
    n = re.search('(\w+)( = .*)', line)
    for k, v in mapping.iteritems():
        # Does line contain a stored keyword for a function call
        w = re.search(k +'\(', line)
        if w:
            line = line.replace(k, v)
    if m:
        function_name = m.group(0)
        random_name = utils.gen_random_name()
        mapping[function_name] = random_name
        line.replace(function_name, random_name)
        line = line.replace(function_name, random_name)
    elif n:
        variable_name = n.group(1)
        random_name = utils.gen_random_name()
        mapping[variable_name] = random_name
        line = line.replace(variable_name, random_name)

    obf_file.write(line)


def test():
    a = 'Hello'
    a = 'None'
    print a

test()