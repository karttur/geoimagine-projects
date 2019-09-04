'''
Created on 23 Apr 2019

@author: thomasgumbricht
'''

from geoimagine.kartturmain.readXMLprocesses import ReadXMLProcesses, RunProcesses

if __name__ == "__main__":
    
    verbose = True
    
    #projFN ='/full/path/to/modis_20190303.txt'
    projFN ='doc/MODIS/modis_20190303.txt'
  
    procLL = ReadXMLProcesses(projFN,verbose)

    RunProcesses(procLL,verbose)