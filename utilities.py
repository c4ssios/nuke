import nuke
import os
import math


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
           
        
######################################################################################################################

def contactSheetFromFiles():

    path = "/Volumes/luma/stellarvortex/byPrefix/_MODEL/envTitan/txtr/mari/_output/images/color/"

    contactSheet = nuke.createNode("ContactSheet")
    nodeList = []

    for dirpath, dirnames, filenames in os.walk(path):
        for f in filenames:
            #print(os.path.join(dirpath, f))
            filePath = os.path.join(dirpath, f)

            read = nuke.nodes.Read(file=filePath)
            read["postage_stamp"].setValue(False)

            textValue = "[join [lrange [split [value input.file]  /] end-1 end] /]"

            label = nuke.createNode("Text")
            label.setInput(0, read)
            label['box'].setValue(0, 0)
            label['box'].setValue(0, 1)
            label['box'].setExpression("input.width", 2)
            label['box'].setExpression("input.height", 3)
            label['xjustify'].setValue("left")
            label['yjustify'].setValue("bottom")
            label['size'].setValue(200)
            label['message'].setValue(textValue)

            nodeList.append(label)

    rows = math.ceil(math.sqrt(len(nodeList)))

    contactSheet['rows'].setValue(rows)
    contactSheet['columns'].setValue(rows)
    contactSheet['height'].setValue(8192)
    contactSheet['width'].setValue(8192)

    for n in nodeList:
        inputNum = nodeList.index(n)
        contactSheet.setInput(inputNum, n)
    #print(nuke.selectedNode())
