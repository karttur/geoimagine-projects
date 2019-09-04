'''
Created on 29 Mar 2019

@author: thomasgumbricht
'''

from geoimagine.kartturmain.readXMLprocesses import ReadXMLProcesses, RunProcesses

if __name__ == "__main__":
    
    verbose = True
    
    projFN ='doc/LesothoMoisture/LesothoMoisture.txt'
    procLL = ReadXMLProcesses(projFN,verbose)

    RunProcesses(procLL,verbose)