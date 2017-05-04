import re

def re_function(string):
	return re.search('(?<=def )\w+', string)

def re_variable_assignment(string):
	return re.search('(\w+)( = .*)', string)

def re_for_loop_variable(string):
	return re.search('(for )(\w+)', string)

def re_comment(string):
	return re.search('\s*#', string)