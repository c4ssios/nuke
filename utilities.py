#Set all read Node to hold

def setAllReadNodeToHold():

readnodes = nuke.allNodes('Read')
for readnode in readnodes:
    nodeName = readnode.fullName()
    nuke.toNode(nodeName).knob('after').setValue('hold')

 
