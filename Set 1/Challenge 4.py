import binascii
import math
import struct
from os import close
from shlex import join
from typing import Counter
from venv import create

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

def English_Test(mystr: str):
    c = Counter(mystr.lower())
    total_characters = len(mystr)

    # This *Should* be the fancy math bs that I keep finding
    coefficient = sum(math.sqrt(Frequency_Table.get(char, 0) * y/total_characters) for char, y in c.items())
    return coefficient

def English_Check(results: str):
    sorter = [(English_Test(r[0]), r[0], r[0]) for r in results]
    sorter.sort(key=lambda x: x[0], reverse=True)
    winner = sorter[0]

    return winner

def Xor_Check(encoded: str, number: int):
    mystr = bytes.fromhex(encoded)
    for xor_key in range(256):
        decoded = ''.join(chr(b ^ xor_key) for b in mystr)
        # trying to chekc the value englishness of text
        English_Check(decoded)

        if decoded.isprintable() and decoded.isascii():



            # my work around for printing the key, line that the cipher was on, plus decoded message in one line
            OUTPUT = ''.join(str(xor_key))
            OUTPUT += ''.join("  ")
            OUTPUT += ''.join(str(i))
            OUTPUT += ''.join("  ")
            OUTPUT += ''.join(decoded)
            OUTPUT += '\n'
            #print(OUTPUT)
            OutputData.write(OUTPUT)           
#TODO                                             
#Print a space between sets of strings. Still not done, but a reasonable alternative has been implemented.  

OutputData = open(r"Challenge4Output","w")

# lines = len(Data.readlines())
with open('D:\Code files\GItRepo\Cyrptography-Challenge\Set 1\Challenge4data') as f: #This goes through ALL lines
    Current_Winner = None       #Start of new code attempting to sort though results 
    Current_Winner_Score = 0    #Start of new code attempting to sort though results 

    for i, line in enumerate(f, start=1):                                            #This goes through ALL lines
        Xor_Check(line, i)
        



f.close()
OutputData.close()