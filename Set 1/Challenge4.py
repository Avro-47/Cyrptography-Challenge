from Define import guess_single_byte_xor
from binascii import unhexlify

def search(items, value_function):
    # This SHOULD be what will score all of the results, allowing for the most english awnser to be gathered. 

    current_leader = None
    current_leader_value = 0

    for item in items: 
        rval = value_function(item)
        
        if isinstance(rval, tuple):
            value, others = rval[0], rval[1:]
            others = (item,) + others
            
        else:
            value = rval
            others = (item,)

        if value > current_leader_value:
            current_leader = others
            current_leader_value = value


    return current_leader

def unhexlify_file(fobj):
    #should unhexify the entire doc
    return (line.strip() for line in fobj if line)

with open('D:\Code files\GItRepo\Cyrptography-Challenge\Set 1\Challenge4data', 'rb') as f:
    most_fit = search(unhexlify_file(f), guess_single_byte_xor)
    #decoded string is the 2nd element, the key is the 3rd 
    input_string, outcome, byte = most_fit
    print('String {} \nDecoded into {}, Using Byte {}'.format(input_string.decode('ascii'), outcome.decode('ascii'), byte))

#TODO
#General bug fix, it is currently return line 71 ( random enough that I believe it is reading and socring them all) 
# IE its not just taking the last input, nor stoping after the first, 71 is also not a obs fraction of the file for it to have stopped at. 
#Line 71 is not a line that was flaged during earlier implementation. 

#Could be an error in the value of characters in the table | changed that, new values functioned for challenge 3, 
#returned line 215 with byte 92 for this. Not Correct