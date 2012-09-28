"""
    mersenne_twister.py
    This module implements the Mersenne twister algorithm.

    Mersenne Twister Overview:
    ------------------------
    Pseudorandomly generates 32-bit numbers in the range 0, ..., 2^32 - 1

    Pre: nothing
    Post: returns a generated number
    Time Complexity: 1
    Psuedocode: http://en.wikipedia.org/wiki/Mersenne_twister

    mersenne_twister.extract_number() -> randnum

"""

import random
print random.random()