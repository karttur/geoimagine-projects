'''
Created on 23 feb. 2018

@author: thomasgumbricht
'''

from geoimagine.kartturmain.readXMLprocesses import ReadXMLProcesses, RunProcesses

if __name__ == "__main__":
    
    verbose = True
    
    #projFN ='/full/path/to/grace_20181018_0.txt'
    projFN ='doc/GRACE/grace_20190216.txt'
  
    procLL = ReadXMLProcesses(projFN,verbose)

    RunProcesses(procLL,verbose)