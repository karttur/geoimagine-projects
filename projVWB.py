'''
Created on 23 feb. 2018

@author: thomasgumbricht
'''

from geoimagine.kartturmain.readXMLprocesses import ReadXMLProcesses, RunProcesses

if __name__ == "__main__":
    
    verbose = True
    
    projFN = '/Users/thomasgumbricht/Dropbox/projects/geoimagine_mbpro/USERS/karttur/VerticalWaterBalance/VWB_TRMM-vs-FAOrefevap.txt'
    #projFN = '/Users/thomasgumbricht/Dropbox/projects/geoimagine_mbpro/USERS/karttur/VerticalWaterBalance/VWB_TRMM-vs-FAOrefevap_transfer.txt'
    procLL = ReadXMLProcesses(projFN,verbose)

    RunProcesses(procLL,verbose)