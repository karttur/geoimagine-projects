'''
Created on 10 Jan 2019

@author: thomasgumbricht
'''

from geoimagine.kartturmain.readXMLprocesses import ReadXMLProcesses, RunProcesses

if __name__ == "__main__":
    
    verbose = True
    
    projFN = '/Users/thomasgumbricht/eclipse-workspace/Karttur2018c/geoimagine/projects/doc/ArcticDEM/ArcticDEM_process.txt'

    procLL = ReadXMLProcesses(projFN,verbose)

    RunProcesses(procLL,verbose)