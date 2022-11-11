#!/usr/bin/python3

#1
s1="ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
s1_count=len(s1)
s1_A_count=s1.count('A')
s1_T_count=s1.count('T')
s1_AandT=s1_A_count+s1_T_count
s1_AandT_content=s1_AandT/s1_count*100
print("###the A+T content in",s1,"is",s1_AandT_content,"%" )


#2
s2="ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
change1=s2.replace("A", "t" )
change2=change1.replace("C", "g" )
change3=change2.replace("T", "a" )
Final_change=change3.replace("G", "c" )
s2_complement=Final_change.upper()
print("###The complementing DNA of s2 is", s2_complement)

#3
s3="ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT"
splic="AATTC"
fragment1_L=s3.find(splic)
s3_count=len(s3)
fragment2_L=s3_count-fragment1_L
print("###The length of fragment1 is", fragment1_L,",""the length of fragment2 is", fragment2_L )

#4
s4="ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"
#(1)
#exon1=s4[0:62]
exon1=s4[0:63]
exon2=s4[90:]
exons=exon1+exon2
print("###The exons of s4 is", exons)

#(2)
exons_L=len(exons)
s4_L=len(s4)
code_L=exons_L/s4_L*100
print("###The length of the coding sequence of s4 is", code_L,"%")

#(3)
exon1=s4[0:62]
exon2=s4[90:]
intron=s4[63:89]
intron_low=intron.lower()
print("### Exon intron exon ###\n",exon1+intron_low + exon2)
