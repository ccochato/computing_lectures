import numpy as np
def fence(string_1, string_2):
    '''Function  that given two strings as arguments: string1 
    and string2, the output is string1_string2_string1. 

    Arguments:

    string1 :: whatever string.
    string2  :: whatever  string.


    Example:

    fence("aaa","bbb")
    "aaa_bbb_aaa"    
    '''
    return string_1 + '_' + string_2 +'_'+ string_1

def outer(string):
    '''Function  that given a string the output is 
    its first and last character. 

    Arguments:
    string :: whatever string.
    
    Example:
    fence("Betis")
    "Bs"
    '''

    return string[0]+string[-1] 

