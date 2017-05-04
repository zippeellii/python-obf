import fileinput
import re
import utils

file = fileinput.input()
obf_file = open('output/obf.py', 'w')
mapping = dict()

lines = []

for line in file:
    lines.append(line)
    for k, v in mapping.iteritems():
        # Does line contain a stored keyword for a function call
        w = re.search(k +'\(', line)
        if w:
            line = line.replace(k, v)
        w = re.search(('[\s(]'+k+'[]\s:.[,]'), line)
        if w:
            print 'Replace variable'
            print line
            line = line.replace(k, v)
    # See if line includes a function definiton
    function_def = re.search('(?<=def )\w+', line)
    # See if line includes a variable assignment 
    n = re.search('(\w+)( = .*)', line)
    # Find variable declaration in foor loop
    p = re.search('(for )\w+', line)
    # Find if comment line
    b = re.search('\s*#', line)
    if function_def:
        function_name = function_def.group(0)
        random_name = utils.gen_random_name()
        mapping[function_name] = random_name
        line.replace(function_name, random_name)
        line = re.sub('(?<=def )\w+', random_name, line)
    if n:
        variable_name = n.group(1)
        random_name = utils.gen_random_name()
        mapping[variable_name] = random_name
        line = re.sub('(\w+)( =)', random_name + ' =', line)
    if p:
        variable_name = p.group(0)
        random_name = utils.gen_random_name()
        mapping[variable_name] = random_name
        line = line.replace(variable_name, random_name)
    if b:
        continue

    obf_file.write(line)


def test():
    a = 'Hello'
    a = 'None'
    print a

test()