import os
import mmap
import re
##keys = open('C:\Users\Krishna\Desktop\dnew gene symbols\mus musculus_gene_symbols.txt','r').readlines()
##indir = 'F:\M.Tech\org segregated\mus musculus\zaq'
##for root, dirs, filenames in os.walk(indir):
## #   print 'r'
##    for f in filenames:
## #     print 'starOed'+str(f)+str(count)
##      log = open(f, 'r')
###f = open('example.txt')
##      s = mmap.mmap(log.fileno(), 0, access=mmap.ACCESS_READ)
##      for key in keys:
## #         print key
##          if s.find(key.rstrip('\n')) != -1:
##              print str(log)
##              print 'true'
##          


#keywords = open('C:\Users\Krishna\Documents\ztestt.txt','r').readlines()
#q=open('C:\Users\Krishna\Desktop\qfilter_output_st3.txt','w')
keywords = open('F:\M.Tech\org segregated\mus musculus\zaq\mouse_keywords123_3.txt','r').readlines()  # this has the keywords
c=0
#for path, dirs, files in os.walk('F:\M.Tech\org segregated\mus musculus'):
 #   for file in files:

sentences = open('F:\M.Tech\org segregated\mus musculus\GSE10029-GPL6330_series_matrix.txtimp_info.txt','r').readlines();
c = c+1
r=0
print c
for sentence in sentences:
    k=0
   # if r==1:
    #    break
    for keyword in keywords:
   #     print k, 'file ', c, 'line', r, file
        k=k+1
        key2 = re.escape(keyword.rstrip())
        if re.search(r'\b%s\b' % key2, sentence):
  #          print("Found '%s' in '%s'" % (keyword.strip(), sentence.strip()))
            #q.write(file)
            #q.write('\n')
            #q.write("Found '%s' in '%s'" % (keyword.strip(), sentence.strip()))
            #q.write('\n')
            
            print keyword.strip()
            print sentence.strip()
     #       r=1
      #      break

      