'''
Created on 19 Feb 2019

@author: thomasgumbricht
'''

from geoimagine.kartturmain.readXMLprocesses import ReadXMLProcesses, RunProcesses

if __name__ == "__main__":
    
    verbose = True
    
    #projFN ='/full/path/to/smap_20190221.txt'
    projFN ='doc/SMAP/smap_20190416.txt'
    #projFN ='doc/SMAP/smap-waterbodies-adjust_20190416.txt'
  
    procLL = ReadXMLProcesses(projFN,verbose)

    RunProcesses(procLL,verbose)
    