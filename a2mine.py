def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """
    #if len('dna') != 0
    return len(dna)
    #elseif print 'You didnt enter anything'


def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """
    #if len('dna1') or len('dna2') != 0
    return len(dna1) > len(dna2)
    #elseif return ''


def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """
    #count_nucleotides(dna, nucleotide):
    number = 0
    for nucleotide in dna:
        number += 1
        print (number)



def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False

    """
    return 'dna2' in 'dna1'

"""four more defs from here"""   

#def is_valid_sequence 
'''str-> bool
returns true if only A,T, C, G is represented 

'''
#def insert_sequence
'''(str, str, int) -> str
Inserts sequense at a given index

'''


#def get_complement  
'''(str) -> str
Returns complimentary nukleotide for A(=T), T(=A), C(=G), G(=C) 
'''


#def get_complementary_sequence
'''(str) -> str
eturns complimentary nukleotide for A(=T), T(=A), C(=G), G(=C) in sequense
'''



