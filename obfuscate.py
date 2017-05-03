import fileinput
import re
import utils

file = fileinput.input()
obf_file = open('output/obf.py', 'w')
mapping = dict()

for line in file:
    m = re.search('(?<=def )\w+',line) 
    if m:
        function_name = m.group(0)
        random_name = utils.gen_random_name()
        mapping[function_name] = random_name
        obf_file.write(line.replace(function_name, random_name))
    else:
        obf_file.write(line)

def test():
    print 'Hello'