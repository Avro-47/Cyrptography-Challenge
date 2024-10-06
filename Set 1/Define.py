import binascii
import imp
import math
import struct
import array
import operator
from collections import Counter
from tkinter import SINGLE
from typing import ByteString
from xml.etree.ElementTree import tostring
try:
    from itertools import imap
except ImportError:
    imap = map



Frequency_Table = {
    b'a':  43.31,
    b'b':  10.56,
    b'c':  23.13,
    b'd':  17.25,
    b'e':  56.88,
    b'f':  9.24,
    b'g':  12.59,
    b'h':  15.31,
    b'i':  38.45,
    b'j':  1,
    b'k':  5.61,
    b'l':  27.98,
    b'm':  15.36,
    b'n':  33.92,
    b'o':  36.51,
    b'p':  16.14,
    b'q':  1,
    b'r':  38.64,
    b's':  29.23,
    b't':  35.43,
    b'u':  18.51,
    b'v':  5.13,
    b'w':  6.57,
    b'x':  1.48,
    b'y':  9.06,
    b'z':  1.39,
    b' ':  36.8,      # I don't think that this is being counted 
    }
if isinstance(b'a'[0], int):
    Frequency_Table = {x[0]: y for x, y in Frequency_Table.items()}

def English_Test(mystr: str):
    # I believe this is counting how often each caracter appears, as 
    # well as converting them into lowercase ( I persume for ease of counting)
    c = Counter(mystr.lower())
    total_characters = len(mystr)

    #this should be the fancy math BS that I was finding. 
    coefficient = sum(math.sqrt(Frequency_Table.get(char, 0) * y/total_characters) for char, y in c.items())
    return coefficient

def bytes_xor(a,b):
    aa = array.array('B', a)
    bb = array.array('B', b)

    return array.array('B', imap(operator.xor, aa, bb)).tobytes()

def single_byte_xor(string, byte):
    # this SHOULD go over all the bytes in a string, and XOR them all with a byte 
    teststring = struct.pack("B", byte) * len(string)
    return bytes_xor(string, teststring)

def guess_single_byte_xor(string):
    #This SHOULD be what is brute forcing the single byte xor, and then list everything in the most the
    #least likely to have english words before returning the topmost result. 
    results = ((single_byte_xor(string, byte), byte) for byte in range(0,256))
    emap = [(English_Test(r[0]), r[0],r[1]) for r in results]

    emap.sort(key=lambda x: x[0], reverse=True)
    winner = emap[0]

    return winner
