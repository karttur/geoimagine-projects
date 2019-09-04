'''
Created on 23 feb. 2018

@author: thomasgumbricht
'''

from geoimagine.kartturmain.readXMLprocesses import ReadXMLProcesses, RunProcesses

#from . import ReadXMLProcesses 

if __name__ == "__main__":
    
    verbose = True
    
    #projFN ='/full/path/to/landsat.txt' 
    projFN ='doc/Landsat/Landsat.txt'
  
    procLL = ReadXMLProcesses(projFN,verbose)

    RunProcesses(procLL,verbose)