from __future__ import division 
#! usr/bin/python
print("hello, kelcie") 

# In class assignment     
def get_at_content(dna):
    length= len(dna)
    a_count = dna.count('A')
    t_count = dna.count('T')
    at_content = (a_count + t_count)/ length
    return at_content
    
    
my_at_content = get_at_content("ATGCATGCAACTGTAGC")
print(str(my_at_content))
print(get_at_content("ATGCATGCAACTAGTAGC"))
print(get_at_content("aactgtagctagctagcagcgta"))

#Improvement of significant figures including with round and counts the a and t's for 
#in lowercase



def get_at_content1(dna):
    length= len(dna)
    a_count = dna.upper().count('A')
    t_count = dna.upper().count('T')
    at_content = (a_count + t_count)/ length
    return round(at_content, 2) 
    
my_at_content = get_at_content1("ATGCATGCAACTGTAGC")
print(str(my_at_content))
print(get_at_content1("ATGCATGCAACTAGTAGC"))
print(get_at_content1("aactgtagctagctagcagcgta"))

#BONUS
from __future__ import division 

def get_at_content2(dna):
    length= len(dna)
    a_count = dna.upper().count('A')
    t_count = dna.upper().count('T')
    at_content = (a_count + t_count)/ length
    return round(at_content, 2) 
    
my_at_content = get_at_content2("TTCGNNN")
print(str(my_at_content))
print(get_at_content2("tnnacgnnat"))
print(get_at_content2("cccncncncnceeen")) #test to see if it worked. 