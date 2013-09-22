def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """
    #tested and workx
    return (len(dna))
 


def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """
    #tested and workx
    return (len(dna1) > len(dna2))
 


def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """
    #tested and workx
    n = 0
    for u in dna:
        if u in nucleotide:
            n = n + 1
    
    return n



def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False

    """
    return dna1.count(dna2) >= 1
 

"""All above tested and OK. Score 12/24 as of sun 22.9"""   
#is valid is tested and checked in IDLE:-)
def is_valid_sequence(dna):
    """str-> bool
    returns true if only A,T, C, G is represented"""
    

    n = 0
    for u in dna:
        if u not in 'ATCG':
            n = n + 1

    
    return (n == 0)

def insert_sequence(nuc1,nuc2,num):#TEsted and workx
    '''(str, str, int) -> str
    Inserts sequense at a given index

    insert_sequence('ATCG','TTT', -2)
    'ATTTTCG'

    '''
    dns = ''


    if abs(num) < (len(nuc1)):
        num = len(nuc1)

    dns = (nuc1[0:num] + nuc2 + nuc1[(num):(len(nuc1)+len(nuc2))])
    return dns



def get_complement(dna):  #Tested and si valid in IDLE
    '''(str) -> str
    Returns complimentary nukleotide for A(=T), T(=A), C(=G), G(=C) 
    get_complement('A')
    'T'
    '''
    complementary = ''

    for u in dna:
        if u in 'A':
            complementary = 'T'
        if u in 'T':
            complementary = 'A'
        if u in 'C':
            complementary = 'G'
        if u in 'G':
            complementary = 'C'

    return complementary

def get_complementary_sequence(dna):#Tested and si valid in IDLE
    '''(str) -> str
    
    Returns complimentary nukleotide for A(=T), T(=A), C(=G), G(=C) in sequense
    get_complementary_sequence('ATCTA')
    'TAGAT'
    '''
    complementary = ''

    for u in dna:
        if u in 'A':
            complementary += 'T'
        if u in 'T':
            complementary += 'A'
        if u in 'C':
            complementary += 'G'
        if u in 'G':
            complementary += 'C'

    return complementary



