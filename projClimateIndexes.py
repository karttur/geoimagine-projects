'''
Created on 5 Apr 2019

@author: thomasgumbricht
'''

from geoimagine.kartturmain.readXMLprocesses import ReadXMLProcesses, RunProcesses

if __name__ == "__main__":
    
    verbose = True
    
    #projFN = '/doc/ClimateIndexes/xml/climateIndex-0100_import-NOAA.xml'
    #projFN = '/doc/ClimateIndexes/xml/climateIndex-0100_import-co2records.xml'
    projFN = '/doc/ClimateIndexes/xml/climateIndexes-0800_plot.xml'

    procLL = ReadXMLProcesses(projFN,verbose)

    RunProcesses(procLL,verbose)