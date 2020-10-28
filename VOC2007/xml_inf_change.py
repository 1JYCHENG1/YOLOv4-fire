import xml.etree.ElementTree as ET
import os, shutil
path_xml="F:\\火灾检测\\2-代码\\pytorch-YOLOv4-master\\VOCdevkit\\VOC2007\\Annotations\\" # xml文件存放路径

imgpath_xml = "FireImageSet\\ImageSets\\"

files_xml=os.listdir(path_xml) #读取路径下所有文件名


for j in range(len(files_xml)):
    xmlFile = files_xml[j]

    if xmlFile.endswith('.xml'):
        tree=ET.ElementTree(file = path_xml+xmlFile) #打开xml文件，送到tree解析
        root=tree.getroot() #得到文档元素对象

        root[2].text=imgpath_xml+root[1].text
        #替换后的内容保存在内存中需要将其写出
        tree.write(path_xml+xmlFile)
