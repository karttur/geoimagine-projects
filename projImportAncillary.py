'''
Created on 24 Apr 2019

@author: thomasgumbricht
'''

from geoimagine.kartturmain.readXMLprocesses import ReadXMLProcesses, RunProcesses

if __name__ == "__main__":
    
    verbose = True
    
    #projFN ='/full/path/to/grace_20181018_0.txt'
    projFN ='doc/ImportAncillary/Import_NaturalEarth.txt'
  
    procLL = ReadXMLProcesses(projFN,verbose)

    RunProcesses(procLL,verbose)
    
