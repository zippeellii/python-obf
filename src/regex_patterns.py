"""Contains regex patterns to find specific properties in source file."""

import re

re_comments = re.compile('(\s*#)')

re_function = re.compile('(?<=def )\w+')

re_var_assignment = re.compile('(\w+)( = .*)')

re_for_loop_variable = re.compile('(for )(\w+)')
