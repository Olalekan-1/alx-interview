#!/usr/bin/python3

""" Module for Utf-8 validation
"""


def validUTF8(data):
    """ Checks for valid Utf-8 encoding
    """
    num_bytes = 0

    for byte in data:
        if num_bytes == 0:
            if byte >> 7 == 0b0:
                continue
            while (byte >> num_bytes) & 0b1:
                num_bytes += 1
            if num_bytes == 1 or num_bytes > 4:
                return False
            num_bytes -= 1
        else:
            if (byte >> 6) != 0b10:
                return False
            num_bytes -= 1

    return num_bytes == 0
