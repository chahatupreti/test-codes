# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 17:43:23 2016

@author: chahat
"""
import re
#a = '	Aberrant DNA methylation, one of the major epigenetic alterations in cancer, has been reported to accumulate in a subset of colorectal cancer (CRC), so-called CpG island methylator phenotype (CIMP), which was known to correlate with microsatellite instability (MSI)-high CRC. To select new methylation markers genome-widely and epigenotype CRC by DNA methylation comprehensively, we performed methylated DNA immunoprecipitation-on-chip analysis using MSI-high CRC cell line HCT116 and microsatellite-stable SW480, and re-expression array analysis by 5-aza-2-deoxycytidine/Trichostatin A. Methylation levels of 44 new markers selected and 16 previously reported markers were analyzed quantitatively in 149 clinical CRC samples using MALDI-TOF mass spectrometry. By unsupervised two-way hierarchical clustering, CRC was clustered into high-, intermediate-, and low-methylation epigenotypes. Methylation markers were clustered into two groups: Group-1 showing methylation in high-methylation epigenotype and including all the 11 CIMP-related markers except NEUROG1, and Group-2 showing methylation in high- and intermediate-methylation epigenotypes. Marker panel deciding methylation epigenotypes with the highest accuracy was developed: 1st-Panel consisting of Group-1 genes (CACNA1G, LOX, SLC30A10) to extract high-methylation epigenotype, and 2nd-Panel consisting of Group-2 genes (ELMO1, FBN2, THBD, HAND1) and SLC30A10 again to divide the remains into intermediate- and low-methylation epigenotypes. High-methylation epigenotype correlated significantly with BRAF mutation, MSI, proximal tumor location, and mucinous component, in concordance with reported CIMP. Intermediate- and low-methylation epigenotypes significantly correlated with KRAS-mutation(+) and KRAS-mutation(-), respectively. KRAS-mutation(+) intermediate-methylation epigenotype showed worse prognosis than KRAS-mutation(-) low-methylation epigenotype (p=0.030). These three epigenotypes with different genetic characteristics suggested different molecular CRC genesis, and the markers might be useful to predict prognosis.'
#if re.search(r'(\(.*?\))' ,a):
#    pr
#s = 'there are many people in the colorectal cancer (crc) here in the people (crc) there'
s = 'there are many people in the world having colorectal cancer (crc) who also have the depression syndrome (ds) worldwide'
acrolen=5
acrolist=['crc','ds']
rt=[]
for acro in acrolist:
    print (acro)
    refind= re.findall('((?:\w+\W+){1,%d}\(%s\))'  %(acrolen, acro), s, re.I)
    for er in refind:
        rt.append(er)
#    refind= re.findall('((?:\w+\W+){1,%d}\(crc\))'  %(acrolen),s, re.I)
if rt:       
    print (2)
    for rr in rt:         
        print (rr)