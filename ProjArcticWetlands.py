'''
Created on 13 Mar 2019

@author: thomasgumbricht
'''

from geoimagine.kartturmain.readXMLprocesses import ReadXMLProcesses, RunProcesses

if __name__ == "__main__":
    
    verbose = True
    
    #projFN = '/Users/thomasgumbricht/eclipse-workspace/Karttur2018c/geoimagine/projects/doc/ArcticWetlands/ArcticWetlands.txt'
    projFN ='doc/ArcticWetlands/ArcticWetlands.txt'
    procLL = ReadXMLProcesses(projFN,verbose)

    RunProcesses(procLL,verbose)