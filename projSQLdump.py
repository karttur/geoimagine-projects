'''
Created on 1 apr. 2019

@author: thomasgumbricht
'''

from geoimagine.kartturmain.readXMLprocesses import ReadXMLProcesses, RunProcesses

if __name__ == "__main__":
    
    verbose = True
    
    #projFN ='/full/path/to/smap_20190221.txt'
    projFN ='doc/SQLdump/SQLdump_20190401.txt'
  
    procLL = ReadXMLProcesses(projFN,verbose)

    RunProcesses(procLL,verbose)