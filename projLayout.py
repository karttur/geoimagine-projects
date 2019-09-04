'''
Created on 9 Apr 2019

@author: thomasgumbricht
'''
import csv

from geoimagine.kartturmain.readXMLprocesses import ReadXMLProcesses, RunProcesses

def CreatepaletteFromCsv(palette,csvSrcFPN,xmlDstFPN,alpha=0,label=0,hint=0):
    '''
    '''
    writeL = []
    writeL.append("<?xml version='1.0' encoding='utf-8'?>")
    writeL.append("<palette>")
    writeL.append("    <userproj userid = 'karttur' projectid = 'karttur' tractid= 'karttur' siteid = '*' plotid = '*' system = 'system'></userproj>")
    writeL.append("    <process processid = 'addrasterpalette'>")
    writeln = "        <parameters palette = '%(p)s' compid='test'>" %{'p':palette}
    writeL.append( writeln )

    with open(csvSrcFPN) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            if len(row) < 4:
                continue
            i,r,g,b = row[0:4]
            if alpha:
                a = row[5]
            else:
                a = 0
            if label:
                l = row[6]
            else:
                l = 'NA'
            if hint:
                h = row[7]
            else:
                h = ''
            query = {'id':int(i),'r':int(r),'g':int(g),'b':int(b),'a':int(a),'l':l,'h':h}
            xmltag = "            <setcolor id = '%(id)d' red = '%(r)d' green ='%(g)d' blue='%(b)d' alpha ='%(a)d' label='%(l)s' hint='%(h)s' ></setcolor>" %query           
            #print (xmltag)
            writeL.append( xmltag )
    writeL.append("        </parameters>")
    writeL.append("    </process>")
    writeL.append("</palette>")
    for row in writeL:
        print (row)
        
    #if xmlDstFPN is given, write the process to file
    if xmlDstFPN:
        with open(xmlDstFPN, "w") as f:
            #writer = csv.writer(csvfile, delimiter=',')
            for line in writeL:
                #writer.writerow(line)
                f.write(line)
                f.write('\n')
            
if __name__ == "__main__":
    ''' Use http://www.zonums.com/online/color_ramp/ for defining a color ramp
    save the ramp r,g,b,HEX as a simple txt file and process it with CreatepaletteFromCsv
    Then run the process to add the palette ot Framework database
    '''
    csvSrcFPN = 'doc/Layout/txt/palette_mirrorlag12*2.txt'
    xmlDstFPN = 'doc/Layout/xml/palette_mirrorlag12*2.xml'
    palette = 'lag12mirror'
    #CreatepaletteFromCsv(palette,csvSrcFPN,xmlDstFPN)

    
    verbose = True
    
    #projFN ='/full/path/to/layout.txt'
    projFN ='doc/Layout/layout.txt'
  
    procLL = ReadXMLProcesses(projFN,verbose)

    RunProcesses(procLL,verbose)