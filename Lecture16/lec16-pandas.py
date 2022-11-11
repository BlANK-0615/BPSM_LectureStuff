#user!/python3
#lecture16: Pandas

import os, sys, subprocess
import numpy as np
import pandas as pd

#Download the latest eukaryotes.txt equivalent file from NCBI
subprocess.call('wget -qO eukaryotes.txt "ftp://ftp.ncbi.nlm.nih.gov/genomes/GENOME_REPORTS/eukaryotes.txt" ' , shell=True)

#Q1.how many fungal species have genomes bigger than 100Mb? What are their names?
Fungal_count = len( df[ (df['Group'] == 'Fungi')& (df[ 'Size (Mb)'] >  100)] )
Fungal = df[ (df['Group'] == 'Fungi')& (df[ 'Size (Mb)'] >  100)] 
Name1 = Fungal['#Organism/Name']
Name2 = df[ (df['Group'] == 'Fungi')& (df[ 'Size (Mb)'] >  100)]['#Organism/Name']#这种可以

#Q2.how many of each Kingdom/group (plants, animals, fungi and protists) have been sequenced?
Plants1 = len( df[ (df['Group'] == 'Plants')])
Animals1 = len( df[ (df['Group'] == 'Animals')])
Fungi1 = len( df[ (df['Group'] == 'Fungi')])
Protist1 = len( df[ (df['Group'] == 'Protists')])

#正确
Plants1
Animals1
Fungi1
Protist1

#如何生成一个dataframe储存数据
pd.DataFrame(Plants2) = (Df['Group'] == 'Plants').value_counts()#这个不行
Animals2 = (df['Group'] == 'Animals').value_counts()
Fungi2 = (df['Group'] == 'Fungi').value_counts()
Protst2 = (df['Group'] == 'Protists').value_counts()
#不对，输出不了
Plants2
Animals2
Fungi2
Protist2


#Q3.which Heliconius species genomes have been sequenced?
Name_Heli = df[ (df['genus'] == 'Heliconius')]['#Organism/Name']#这种可以

#Q4.which sequencing centre has sequenced the most plant genomes? the most insect genomes?
list(df.columns)
Plants_Centre1 = df['Group'] == 'Plants'#这个语法是判断是否，返回logical value
Insects_Centre1 = df['SubGroup'] == 'Insects'

Plants_Centre2 =df[df['Group'] == 'Plants']
Insects_Centre2 =df[ df['SubGroup'] == 'Insects']

Plants_Centre2['Center'].value_counts().head()
Insects_Centre2['Center'].value_counts().head()


#Q5.add a column giving the number of proteins per gene. Which genomes have at least 10% more proteins than genes?
df['protein_per_gene'] = df['Proteins']/df['Genes']
df['protein_per_gene']
#大于1.1的数量
PPG_count = len(df[ df[ 'protein_per_gene' ] > 1.1 ])
#大于1.1的genemo
PPG_genemo = df[ ( df[ 'protein_per_gene' ] > 1.1)]['#Organism/Name']#这种可以