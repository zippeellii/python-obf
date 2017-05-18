"""Utility functions for the obfuscator."""

import random

reserved_words = ['encrypt', 'debug']

def gen_random_name():
    """Generate a random string of characters."""
    return ''.join([random.choice('abcdefghijklmnopqrstu') for _ in xrange(8)])
