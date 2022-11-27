from sqlite3 import complete_statement


def PatternCount(Text, Pattern):
    count = 0
    for i in range(len(Text)-len(Pattern)+1):
        if Text[i:i+len(Pattern)] == Pattern:
            count = count+1
    return count


def FrequencyMap(Text, k):
    freq = {}
    n = len(Text)
    for i in range(n-k+1):
        Pattern = Text[i:i+k]
        freq[Pattern] = PatternCount(Text, Pattern)
    return freq


def FrequentWords(Text, k):
    words = []
    freq = FrequencyMap(Text, k)
    m = max(freq.values())
    for key in freq:
        # add each key to words whose corresponding frequency value is equal to m
        if freq[key] == m:
            words.append(key)
    return words


DNA = "ATCAATGATCAACGTAAGCTTCTAAGCATGATCAAGGTGCTCACACAGTTTATCCACAACCTGAGTGGATGACATCAAGATAGGTCGTTGTATCTCCTTCCTCTCGTACTCTCATGACCACGGAAAGATGATCAAGAGAGGATGATTTCTTGGCCATATCGCAATGAATACTTGTGACTTGTGCTTCCAATTGACATCTTCAGCGCCATATTGCGCTGGCCAAGGTGACGGAGCGGGATTACGAAAGCATGATCATGGCTGTTGTTCTGTTTATCTTGTTTTGACTGAGACTTGTTAGGATAGACGGTTTTTCATCACTGACTAGCCAAAGCCTTACTCTGCCTGACATCGACCGTAAATTGATAATGAATTTACATGCTTCCGCGACGATTTACCTCTTGATCATCGATCCGATTGAAGATCTTCAATTGTTAATTCTCTTGCCTCGACTCATAGCCATGATGAGCTCTTGATCATGTTTCCTTAACCCTCTATTTTTTACGGAAGAATGATCAAGCTGCTGCTCTTGATCATCGTTTC"
k = 9
print(FrequentWords(DNA, k))


# Input:  A string Pattern
# Output: The reverse of Pattern
def Reverse1(Pattern):
    # your code here
    length = len(Pattern)
    revPattern = list(range(length))
    strs = ""
    for index, ch in enumerate(Pattern):
        print(index, " ", ch)
        revPattern[length-index-1] = ch
    for ch in revPattern:
        strs += ch
    print("/n/n", strs)


# Input:  A string Pattern
# Output: The reverse of Pattern
def Reverse(Pattern):
    # your code here
    length = len(Pattern)
    strs = ""
    for index in range(length):
        strs += Pattern[length-index-1]
    return strs


# Input:  A DNA string Pattern
# Output: The complementary string of Pattern (with every nucleotide replaced by its complement).
def Complement(Pattern):
    # your code here
    r = {"A": "T",
         "T": "A",
         "C": "G",
         "G": "C"}
    ComPattern = ""
    for ch in Pattern:
        ComPattern += r[ch]
    return ComPattern

def ReverseComplement(Pattern):   
    # your code here
    return Complement(Reverse(Pattern))




# fill in your PatternMatching() function along with any subroutines that you need.
def PatternMatching(Pattern, Genome):
    positions = [] # output variable
    # your code here
    lenPattern = len(Pattern)
    lenGenome = len(Genome)
    for i in range(lenGenome-lenPattern+1):
        if Pattern == Genome[i:i+lenPattern]:
            positions.append(i)
    return positions


def SymbolArray(Genome, symbol):
    array = {}
    n = len(Genome)
    ExtendedGenome = Genome + Genome[0:n//2]
    for i in range(n):
        array[i] = PatternCount(symbol, ExtendedGenome[i:i+(n//2)])
    return array

a ="ab"
l = list(range(0,5))
s = "abcdab"
print(l)
print(s[4:6])
print(PatternMatching(a,s))


# The following lines will automatically read in the Vibrio cholerae genome for you and store it in a variable named v_cholerae
#import sys                              # needed to read the genome
#input = sys.stdin.read().splitlines()   #
#v_cholerae = input[1]                   # store the genome as 'v_cholerae'
#pattern =  input[0]  #

# On the following line, create a variable called Text that is equal to the oriC region from T petrophila
Text = "AACTCTATACCTCCTTTTTGTCGAATTTGTGTGATTTATAGAGAAAATCTTATTAACTGAAACTAAAATGGTAGGTTTGGTGGTAGGTTTTGTGTACATTTTGTAGTATCTGATTTTTAATTACATACCGTATATTGTATTAAATTGACGAACAATTGCATGGAATTGAATATATGCAAAACAAACCTACCACCAAACTCTGTATTGACCATTTTAGGACAACTTCAGGGTGGTAGGTTTCTGAAGCTCTCATCAATAGACTATTTTAGTCTTTACAAACAATATTACCGTTCAGATTCAAGATTCTACAACGCTGTTTTAATGGGCGTTGCAGAAAACTTACCACCTAAAATCCAGTATCCAAGCCGATTTCAGAGAAACCTACCACTTACCTACCACTTACCTACCACCCGGGTGGTAAGTTGCAGACATTATTAAAAACCTCATCAGAAGCTTGTTCAAAAATTTCAATACTCGAAACCTACCACCTGCGTCCCCTATTATTTACTACTACTAATAATAGCAGTATAATTGATCTGA"

# On the following line, create a variable called count_1 that is equal to the number of times
# that "ATGATCAAG" occurs in Text.
count_1 = PatternCount(Text,"ATGATCAAG")

# On the following line, create a variable called count_2 that is equal to the number of times
# that "CTTGATCAT" occurs in Text. 
count_2 = PatternCount(Text,"CTTGATCAT")

print(count_1+count_2)
# Finally, print the sum of count_1 and count_2


print(FrequentWords("CGCCTAAATAGCCTCGCGGAGCCTTATGTCATACTCGTCCT", 3))

print(ReverseComplement("CCAGATC"))