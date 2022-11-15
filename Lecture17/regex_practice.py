#user!/python3
#lecture17: regex

import re
import os


#2.raw string
'r' 就等于一个'\',将字符进行转义
exp1：
myvar= r'\n'
type(myvar)
<class 'str'>
print(myvar)
\n
myvar
'\\n'
exp2：
myvar= r'\\n'
type(myvar)
<class 'str'>
print(myvar)
\\n
myvar
'\\\\n'


#3.searching for patterns
#语法：re.search(pattern,string)
# It searches for the pattern 
# in the string and returns either True or None.


#Alternatives
# Searching for a simple pattern G-AorT-CG in a string
dna = 'ATCGCGAATTCAC'
if re.search(r'G(A|T)CG', dna):
    print('Restriction site G-AorT-CG found.')
else:
    print('Restriction site G-AorT-CG not found.')

Restriction site G-AorT-CG not found.

#Character groups
exp1:
# Any of four bases at one position, here's one way of doing it
# Looking for GC-then any base-GC
dna = 'ATCGCGAATTCAC'
if re.search(r'GC(A|T|G|C)GC', dna):
    print('Found what we were looking for...')

exp2:
# Here's another way of doing it
if re.search(r'GC[GATC]GC', dna):
    print('Found what we were looking for...')

exp3:
# Different search, found one this time!
if re.search(r'CG[GATC]AT', dna):
    print('Found what we were looking for...')

Found what we were looking for..

#"negated character group"
# A sequence with an ambiguous base in it
dna = 'ATCGCGYAATTCAC'
# Search to see if there are bases that are NOT G or A or T or C
if re.search(r'[^GATC]', dna):
    print('Ambiguous base found!')
else :
    print('Sequence has no ambiguous bases in it.')

4.Match 'shortcuts': the 'cheat sheet'

#(1)Quantifiers

#(2)Positions

#(3)Combinations,最重要的

#(4)Other stuff: what was the match?

#(5)Extracting multiple groups!!重要

#(6)Getting the position

#(7)split 分裂

#(8)Multiple finds

#(9)Finding and processing multiple matches
Some problems require complete match objects for multiple matches, for th
AorT_runs_v2 = re.finditer(r'[AT]{3}', dna)
AorT_runs_v2 = re.finditer(r'[AT]{3,3}', dna)
#both could

#(10)Lookahead assertions







#EXERCISES of lecture17
#1.Here's a list of made-up gene accession numbers: 
#Write a program that will print only the accessions that satisfy the following criteria individually 
#(i.e. treat each criterion separately):
#xkn59438, yhdck2, eihd39d9, chdsye847, hedle3455, xjhd53e, 45da, de37dp

#step1
import re
Acc = ['xkn59438','yhdck2','eihd39d9','chdsye847','hedle3455','xjhd53e','45da','de37dp']

# (1) contain the number 5
re.findall(r'5',Acc)
Q1_list=[]
for i in Acc:
    if re.search('5', i):
        print('For question1,'+i +'have 5')
        Q1_list.append(i)

print(Q1_list)
Q1_list

# (2)contain the letter d or e
Q2_list=[]
for i in Acc:
    if re.search(r'[de]', i):
        print('For question2,'+i +'have d or e')
        Q2_list.append(i)

print(Q2_list)
Q2_list

# (3)contain the letters d and e in that order
Q3_list=[]
for i in Acc:
    if re.search(r'd.*e', i):
        print('For question3,'+i +'have d and e')
        Q3_list.append(i)

print(Q3_list)
Q3_list

# (4)contain the letters d and e in that order with a single letter between them
Q4_list=[]
for i in Acc:
    if re.search(r'd.e', i):
        print('For question4,'+i +'have d and e with a single letter between them')
        Q4_list.append(i)

print(Q4_list)
Q4_list

# (5)contain both the letters d and e in any order
Q5_list=[]
for i in Acc:
    if re.search(r'd', i):
        if re.search(r'e', i):
            print('For question5,'+i +'contain both the letters d and e in any order')
            Q5_list.append(i)

print(Q5_list)
Q5_list

# (6)start with x or y
Q6_list=[]
for i in Acc:
    if re.search(r'^[xy]', i):
            print('For question6,'+i +'cstart with x or y')
            Q6_list.append(i)

print(Q6_list)
Q6_list

# (7)start with x or y and end with e
Q7_list=[]
for i in Acc:
    if re.search(r'^[xy].*e$', i):
            print('For question7,'+i +'cstart with x or y')
            Q7_list.append(i)
Q7_list

# (8)contains any 3 numbers in any order
Q8_list=[]
#Num=[1,2,3,4,5,6,7,8,9]
#Num='123456789'
for i in Acc:
    if re.search(r'[0-9].*[0-9].*[0-9]', i):
            print('For question8,'+i +'contains any 3 numbers in any order')
            Q8_list.append(i)
Q8_list
.*[0-9].*[0-9]
#better way
# if len(re.findall(r'\d',acc)) == 3 :

# (9)contains 3 different numbers in the accession
Q9_list=[]
#Num=[1,2,3,4,5,6,7,8,9]
#Num='123456789'
##一看different，就要考虑set
for i in Acc:
    if len(set(re.findall(r'\d',i))) == 3 :
         print('For question9,'+ i +'contains any 3 numbers in any order')
         Q9_list.append(i)
    # if re.search(r'[0-9]', i):
    #     num1=re.search(r'[0-9]', i).group()
    #     re.search(r'[0-9]', i)
    #         if 
    #         print('For question9,'+i +'contains any 3 numbers in any order')
    #         Q9_list.append(i)
Q9_list

# (10)contain three or more numbers in a row
Q10_list=[]
for i in Acc:
    re.findall(r'\d', i)
    length=len(re.findall(r'\d', i))
    if length>=3:
        Q10_list.append(i)
        print('For question10,'+i +'contain three or more numbers in a row')

Q10_list

# (11)end with d followed by either a, r or p
Q11_list=[]
for i in Acc:
    if re.search(r'd[arp]$', i):
            print('For question11,'+ i +' end with d followed by either a, r or p')
            Q11_list.append(i)
Q11_list



#Question2 DNA sequence: a double digest
# a file contains a made-up DNA sequence. long_dna.txt/localdisk/data/BPSM/Lecture17
# What fragment lengths will we get if we digest the sequence with a novel restriction enzyme BpsmI,
# whose recognition site is ANT*AAT, where * indicates the position of the cut site.
# What will the fragment lengths be if we do a double digest with both BpsmI and BpsmII 
# (whose recognition site is GCRW*TG)?
# What are the sequences of the fragments themselves?

(1)step1
dna = open('/localdisk/data/BPSM/Lecture17/long_dna.txt').read().rstrip('\n')
(2)BPSM1
BpsmI='A[GATC]TAAT'
print('BpsmI cuts at:',BpsmI) 

for matching in re.finditer(BpsmI, dna): 
    print(matching.start()+3) 

last_cut = 0 #上一个剪切位点，会移动
findnum=0  #剪切个数
for matching in re.finditer(BpsmI, dna): #对于每一个找到的剪切位点
    findnum += 1  #计数一次剪切
    cut_position = matching.start() + 3#本次剪切位点，会移动
# Distance from the current cut site to the previous one
    fragment_size = cut_position - last_cut #剪切序列长度
    print('Fragment size is ' + str(fragment_size))
    last_cut = cut_position #移动剪切位点
# We also have to remember the last fragment, from the last cut to the end:
    if findnum == len(list(re.finditer(BpsmI, dna))) :  #记得最后的剪切以序列长度为终点
       #这里可以用len(re.findall(BpsmI, dna))
       fragment_size = len(dna) - last_cut
       print('Fragment size is ' + str(fragment_size))

#finditer 和 findall 不一样

#(3)Bpsm2
BpsmI='A[GATC]TAAT'
BpsmII='GC[AG][AT]TG'
all_cuts = []
for match in re.finditer(BpsmI, dna): 
    all_cuts.append(match.start() + 3)

for match in re.finditer(BpsmII, dna): 
    all_cuts.append(match.start() + 4)

all_cuts.sort()
all_cuts

last_cut = 0
counter = 0
for cut_position in all_cuts:
    counter +=1
    fragment_size = cut_position - last_cut
    print('Fragment '+str(counter)+' size is ' + \
       str(fragment_size) +': '+ str(last_cut)+ ' to ' +str(cut_position) )
    last_cut = cut_position
    if counter == len(all_cuts):
        fragment_size = len(dna) - last_cut
        counter +=1
        print('Fragment '+str(counter)+' size is ' + \
        str(fragment_size) +': '+ str(last_cut)+ ' to ' +str(len(dna)) )

(4)# Let's use a dictionary to store the fragment sequences
fragment_sequences = {}
last_cut = 0
counter = 0
for cut_position in all_cuts:
    counter +=1
    fragment_size = cut_position - last_cut
    fragment_sequences['Fragment'+str(counter)] = dna[last_cut:cut_position]
    print(fragment_sequences['Fragment'+str(counter)])# Get the sequence substring
    print('Fragment '+str(counter)+' size is ' + \
       str(fragment_size) +': '+ str(last_cut)+ ' to ' +str(cut_position) )
    # Get the fragment start and end
    fragends = dna[last_cut:cut_position][0:6] + '...' + dna[last_cut:cut_position][-6:]
    print('Fragment '+str(counter)+ ' has ends: '+fragends+'\n')
    last_cut = cut_position
    if counter == len(all_cuts):
        fragment_size = len(dna) - last_cut
        counter +=1
        print('Fragment '+str(counter)+' size is ' + \
        str(fragment_size) +': '+ str(last_cut)+ ' to ' +str(len(dna)) )
        fragment_sequences['Fragment'+str(counter)] = dna[last_cut:]
        print(fragment_sequences['Fragment'+str(counter)])
        fragends = dna[last_cut:][0:6] + '...' + dna[last_cut:][-6:]    
        print('Fragment has ends: '+fragends)

# Show all the sequences
print(('\n########\n').join(list(fragment_sequences.values())))

#check out
re.search(r'ACGCGTTGAACA',dna)