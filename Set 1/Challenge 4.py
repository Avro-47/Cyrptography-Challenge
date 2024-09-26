import binascii
from os import close
from shlex import join
from venv import create

def Xor_Check(encoded: str, number: int):
    mystr = bytes.fromhex(encoded)
    for xor_key in range(256):
        decoded = ''.join(chr(b ^ xor_key) for b in mystr)
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
#Print a space between sets of strings. 
#verify that it found an actually awnser and has not been all for nought. 

OutputData = open(r"Challenge4Output","w")

# lines = len(Data.readlines())
with open('D:\Code files\GItRepo\Cyrptography-Challenge\Set 1\Challenge4data') as f: #This goes through ALL lines
    for i, line in enumerate(f, start=1):                                            #This goes through ALL lines
        Xor_Check(line, i)
        



f.close()
OutputData.close()