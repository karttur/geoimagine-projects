'''
Created on 4 Feb 2019

@author: thomasgumbricht
'''

from geoimagine.kartturmain.readXMLprocesses import ReadXMLProcesses, RunProcesses

if __name__ == "__main__":
    
    verbose = True
    
    #ALL: projFN = 'doc/AfricaSubSahara/AfricaSubSahara_process.txt'
    projFN = 'doc/AfricaSubSahara/AfricaSubSahara_TRMM_process-pro.txt'
    #projFN = '/Users/thomasgumbricht/eclipse-workspace/Karttur2019a/geoimagine/projects/doc/AfricaSubSahara/AfricaSubSahara_VWB_process.txt'
    #projFN = '/Users/thomasgumbricht/eclipse-workspace/Karttur2019a/geoimagine/projects/doc/AfricaSubSahara/AfricaSubSahara_GRACE_process.txt'
    #projFN = '/Users/thomasgumbricht/eclipse-workspace/Karttur2019a/geoimagine/projects/doc/AfricaSubSahara/AfricaSubSahara_TRMM-GRACE_process.txt'
    #projFN = '/Users/thomasgumbricht/eclipse-workspace/Karttur2019a/geoimagine/projects/doc/AfricaSubSahara/AfricaSubSahara_VWB-GRACE_process.txt'
    #projFN = '/Users/thomasgumbricht/eclipse-workspace/Karttur2019a/geoimagine/projects/doc/AfricaSubSahara/AfricaSubSahara_SMAP_process.txt'
    #projFN = '/Users/thomasgumbricht/eclipse-workspace/Karttur2019a/geoimagine/projects/doc/AfricaSubSahara/AfricaSubSahara_MODIS-getdata_process.txt'
    #projFN = '/Users/thomasgumbricht/eclipse-workspace/Karttur2019a/geoimagine/projects/doc/AfricaSubSahara/AfricaSubSahara_MODIS-TWI_process.txt'
    #projFN = '/Users/thomasgumbricht/eclipse-workspace/Karttur2019a/geoimagine/projects/doc/AfricaSubSahara/AfricaSubSahara_SMAP-MODIS_process.txt'
    procLL = ReadXMLProcesses(projFN,verbose)

    RunProcesses(procLL,verbose)