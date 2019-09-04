'''
Created on 23 feb. 2018

@author: thomasgumbricht
'''

from geoimagine.kartturmain.readXMLprocesses import ReadXMLProcesses, RunProcesses

if __name__ == "__main__":
    
    verbose = True
    
    #projFN ='/full/path/to/FAOrefet_YYYYMMDD.txt'
    projFN ='doc/FAOrefet/FAOrefet_YYYYMMDD.txt'

    procLL = ReadXMLProcesses(projFN,verbose)

    RunProcesses(procLL,verbose)