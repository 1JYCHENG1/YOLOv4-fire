import xml.etree.ElementTree as ET
import os, shutil
path_xml="G:\\YOLO-FIRE\\yolov4-pytorch-master\\VOCdevkit\\VOC2007\\Annotations\\" # xml文件存放路径
sv_path_xml="G:\\YOLO-FIRE\\FireImageSet\\Annotations\\" # 修改后的xml文件存放路径
imgpath_xml="G:\\YOLO-FIRE\\FireImageSet\\ImageSets\\"#新的path路径

path_jpg="G:\\YOLO-FIRE\\yolov4-pytorch-master\\VOCdevkit\\VOC2007\\JPEGImages\\" # jpg文件存放路径
sv_path_jpg="G:\\YOLO-FIRE\\FireImageSet\\ImageSets\\" # 修改后的jpg文件存放路径

files_xml=os.listdir(path_xml) #读取路径下所有文件名
files_jpg=os.listdir(path_jpg)
if len(files_xml) != len(files_jpg):
    pause
i = 0
for j in range(len(files_xml)):
    xmlFile = files_xml[j]
    jpgFile = files_jpg[j]
    if xmlFile[:-4] == jpgFile[:-4] :
        i = i + 1
        k = "%06d" % i
        if xmlFile.endswith('.xml'):
            tree=ET.ElementTree(file = path_xml+xmlFile) #打开xml文件，送到tree解析
            root=tree.getroot() #得到文档元素对象
            # print(root[1].text)
            root[0].text='ImageSets'
            root[1].text='{}.jpg'.format(k)
            #root[0].text是annotation下第一个子节点中内容，直接赋值替换文本内容
            root[2].text=imgpath_xml+'{}.jpg'.format(k)
            #替换后的内容保存在内存中需要将其写出
            tree.write(sv_path_xml+'{}.xml'.format(k))
        if jpgFile.endswith('.jpg'):
            shutil.move(path_jpg+jpgFile,sv_path_jpg+jpgFile)
            os.chdir(sv_path_jpg[:-1]) # 切换当前路径
            os.rename(jpgFile,'{}.jpg'.format(k)) # 对jpg图像进行重命名
