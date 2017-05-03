import random

def gen_random_name():
	return ''.join([random.choice('abcdefghijklmnopqrstu') for _ in xrange(8)])