import nuke
import os

path = "writeFilePathHere"

extension = "png"

fileList = []

for path, currentDirectory, files in os.walk(path):

    for file in files:

        filePath = os.path.join(path, file)

        if "."+extension in filePath:

            fileList.append(filePath)


for f in fileList:

    read = nuke.nodes.Read(file=f)
    read["postage_stamp"].setValue(False)
    read["raw"].setValue(True)

    write_node = nuke.createNode("Write")
    write_node["file"].setValue(f.replace("."+extension, ".exr"))
    write_node["datatype"].setValue("32 bit float")
    write_node["raw"].setValue(True)
    write_node.setInput(0, read)

    nuke.render(write_node, 1, 1)

    nuke.delete(read)
    nuke.delete(write_node)
