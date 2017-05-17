
import random


def generate_key():
    return ''.join([random.choice('abcdefghijklmnopqrstu')
                    for _ in xrange(10)])


def encrypt_string(src, key):
    return ''.join(
        [_encrypt_char(c, key[idx % len(key)])for idx, c in enumerate(src)]
    )


def _encrypt_char(c, k):
    return chr(((ord(c) - 97 + ord(k) - 97) % 26) + 97) \
        if c in 'abcdefghijklmnopqrstuvwxyz' else c


def decrypt_string(src, key):
    return ''.join(
        [_decrypt_char(c, key[idx % len(key)])for idx, c in enumerate(src)]
    )


def _decrypt_char(c, k):
    lol = chr(((ord(c) - 97 - ord(k) + 97) % 26) + 97) \
        if c in 'abcdefghijklmnopqrstuvwxyz' else str(c)
    return lol

def shuffle_lines(lines, key):
    random.seed(key)
    random.shuffle(lines)
    return lines

def unshuffle_lines(lines, key):
    # Initialize the seed
    random.seed(key)
    # Create a list of indexes and shuffle it, it will have same order as encrypted
    # if using same key
    index_list = range(len(lines))  
    random.shuffle(index_list)
    unshuffled_list = [0]*len(lines)
    # Simply take the corresponding index in the shuffled list from lines
    for index, original_index in enumerate(index_list):
        unshuffled_list[original_index] = lines[index]    
    
    return unshuffled_list
