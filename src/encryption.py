
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
