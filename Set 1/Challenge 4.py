import binascii
from os import close
from venv import create

def Xor_Check(encoded: str):
    mystr = bytes.fromhex(encoded)
    for xor_key in range(256):
        decoded = ''.join(chr(b ^ xor_key) for b in mystr)
        if decoded.isprintable() and decoded.isascii():
            

            print(xor_key, decoded)        #    <<--|
#TODO                                      #        |
#Print a space between sets of strings.    #        |
#print to Challenge4Output rahter then cmt ---->>>> |
#verify that it found an actually awnser and has not been all for nought. 

OutputData = open(r"Challenge4Output","w")

# lines = len(Data.readlines())
with open('D:\Code files\GItRepo\Cyrptography-Challenge\Set 1\Challenge4data') as f: #This goes through ALL lines
    for i, line in enumerate(f, start=1):                                            #This goes through ALL lines
        Xor_Check(line)
        



f.close()
OutputData.close()