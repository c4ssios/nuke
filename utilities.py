import os
import nuke


#Set all read Node to hold

def setAllReadNodeToHold():

    readnodes = nuke.allNodes('Read')
    for readnode in readnodes:
        nodeName = readnode.fullName()
        nuke.toNode(nodeName).knob('after').setValue('hold')

######################################################################################################################

def createReadNodesFromFile():

    path = "/Volumes/luma/stellarvortex/byPrefix/_MODEL/envTitan/txtr/mari/_output/images/color/"

    for dirpath, dirnames, filenames in os.walk(path):
        for f in filenames:
            #print(os.path.join(dirpath, f))
            filePath = os.path.join(dirpath, f)

            nuke.nodes.Read(file=filePath)
