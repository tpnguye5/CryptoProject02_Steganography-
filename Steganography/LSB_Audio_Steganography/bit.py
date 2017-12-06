
def getbit(integer, pos):
    """
    :return: 0 or 1 because bits are only 0 or 1
    Returns the bit at the argument position
    """
    value = (integer & (1 << pos)!= 0)
    if value == False:
        return 0
    else:
        return 1

def changeLSB(integer, bit):
    return ((integer & ~1)|bit)

def dataToO