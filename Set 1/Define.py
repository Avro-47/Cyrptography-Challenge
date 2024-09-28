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
    b'a':  0.08167,
    b'b':  0.01492,
    b'c':  0.02782,
    b'd':  0.04253,
    b'e':  0.1270,
    b'f':  0.02228,
    b'g':  0.02015,
    b'h':  0.06094,
    b'i':  0.06966,
    b'j':  0.00153,
    b'k':  0.00772,
    b'l':  0.04025,
    b'm':  0.02406,
    b'n':  0.06749,
    b'o':  0.07507,
    b'p':  0.01929,
    b'q':  0.00095,
    b'r':  0.05987,
    b's':  0.06327,
    b't':  0.09056,
    b'u':  0.02758,
    b'v':  0.00978,
    b'w':  0.02360,
    b'x':  0.00150,
    b'y':  0.01974,
    b'z':  0.00074,
    }
if isinstance(b'a'[0], int):
    Frequency_Table = {x[0]: y for x, y in Frequency_Table.items()}

def English_Test(mystr: str):
    # I believe this is counting how offtne each caracter appears, as 
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
