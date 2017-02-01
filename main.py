# Converts images into Lego Digital Designer compatible XML. Written by Joe Samela 12/11/2016

import xml.etree.cElementTree as ET
from tkinter import Tk, filedialog
from PIL import Image


##### IMPORT IMAGE #####

#Prompts user to select .jpg image
root = Tk()
root.withdraw()
root.fileName = filedialog.askopenfilename(title = "Select file", filetypes = ( ("Image files", ("*.jpg", "*.png")),("All files", "*.*") ) )

##### PROCESS IMAGE #####

#Imports Image
if len(root.fileName) == 0:
    root.destroy()
    exit()

image = Image.open(root.fileName)
pixel = image.load()

#Image dimensions and Number of Pixels
ImageWidth,ImageHeight=image.size
NumberOfPixels = ImageHeight*ImageWidth

#DEFINE PALETTE
RGBValues = ("27,42,52","100,100,100","150,150,150","200,200,200","244,244,244","114,0,18","180,0,0","55,33,0","95,49,9","119,119,78","137,125,98","176,160,111","145,80,28","187,128,90","170,125,85","252,172,0","41,100,99","255,201,149","250,200,10","255,236,108","245,243,215","0,69,26","112,142,124","0,133,43","88,171,65","165,202,24","226,249,154","70,155,195","104,195,226","25,50,90","30,90,168","115,150,200","112,129,154","157,195,247","211,242,234","68,26,145","144,31,118","160,110,185","205,164,222","211,53,157","255,158,205")
ColorNames = ("Black","Dark Stone Grey","Medium Stone Grey","Light Stone Grey","White","New Dark Red","Bright Red","Dark Brown","Reddish Brown","Olive Green","Sand Yellow","Brick Yellow","Dark Orange","Nougat","Medium Nougat","Bright Orange","Flame Yellowish Orange","Light Nougat","Bright Yellow","Cool Yellow","White Glow","Earth Green","Sand Green","Dark Green","Bright Green","Bright Yellowish Green","Spring Yellowish Green","Dark Azur","Medium Azur","Earth Blue","Bright Blue","Medium Blue","Sand Blue","Light Royal Blue","Aqua","Medium Lilac","Bright Reddish Violet","Medium Lavender","Lavender","Bright Purple","Light Purple")
ColorCodes = [26,199,194,208,1,154,21,308,192,330,138,5,38,18,312,106,191,283,24,226,329,141,151,28,37,119,326,321,322,140,23,102,135,212,323,268,124,324,325,221,222]

ColorPalette= Image.new("P", (1,1))
ColorPalette.putpalette( (27,42,52, 100,100,100, 150,150,150, 200,200,200, 244,244,244, 114,0,18, 180,0,0, 55,33,0, 95,49,9, 119,119,78, 137,125,98, 176,160,111, 145,80,28, 187,128,90, 170,125,85, 214,121,35, 252,172,0, 255,201,149, 250,200,10, 255,236,108, 245,243,215, 0,69,26, 112,142,124, 0,133,43, 88,171,65, 165,202,24, 226,249,154, 70,155,195, 104,195,226, 25,50,90, 30,90,168, 115,150,200, 112,129,154, 157,195,247, 211,242,234, 68,26,145, 144,31,118, 160,110,185, 205,164,222, 211,53,157, 255,158,205) + (0,0,0)*215)

#REDUCE COLORS
converted = image.convert("RGB").quantize(palette=ColorPalette)
pixel = converted.load()
#converted.show() #show converted image
#image.show() #show origonal image


##### GENERATE FILE #####

#Produces LXFML elements
LXFML = ET.Element("LXFML",versionMajor="5",versionMinor="0",name="output")

#Produces Meta elements
Meta = ET.SubElement(LXFML,"Meta")
ET.SubElement(Meta,"Application", name="LEGO Digital Designer",versionMajor="4",versionMinot="3")
ET.SubElement(Meta,"Brand",name="LDD")
ET.SubElement(Meta,"BrickSet",version="2248")

#Produces Cameras elements
Cameras = ET.SubElement(LXFML, "Cameras")
ET.SubElement(Cameras,"Camera",refID="0",fieldOfView="80",distance="85.876968383789063",transformation="0.021367546170949936,0,0.99977171421051025,0.27041879296302795,0.96272546052932739,-0.0057795057073235512,-0.96250569820404053,0.27048054337501526,0.020571080967783928,-84.712471008300781,26.189098358154297,2.1018843650817871").text = ""

#Produces Brick elements
Bricks = ET.SubElement(LXFML, "Bricks", cameraRef="0")
RigidSystems = ET.SubElement(LXFML, "RigidSystems")
x = 0.0
y = 0.0
offset = 0.4000000059604644775390625
value = 0.4000000059604644775390625*2
for i in range(0,NumberOfPixels):
    if x < ImageWidth:
        x += 1
    if i == 0:
        x = 0
    if x == ImageWidth: #Counts up to imageWidth, resets horizonal and increments vertical
        x = 0
        y += 1
    color = pixel[x,y]
    ColorCode = ColorCodes[color-41]
    Brick = ET.SubElement(Bricks,"Brick",refID=str(i),designID="3005")
    Part = ET.SubElement(Brick,"Part",refID=str(i),designID="3005",materials=str(ColorCode)+",0", decoration="0")
    ET.SubElement(Part,"Bone",refID=str(i),transformation="1,0,0,0,1,0,0,0,1,"+str(-value*x - offset)+",0,"+str(-value*y - offset)+"").text = " "
#Produces RigidSystems elements
    RigidSystem = ET.SubElement(RigidSystems,"RigidSystem")
    ET.SubElement(RigidSystem,"Rigid", refID=str(i), transformation="1,0,0,0,1,0,0,0,1,"+str(-value*x - offset)+",0,"+str(-value*y - offset)+"", boneRefs=str(i)).text = " "

#Produces GroupSystems elements
GroupSystems = ET.SubElement(LXFML, "GroupSystems")
ET.SubElement(GroupSystems,"GroupSystem").text = " "

#Produces BuildingInstruction elements
BuildingInstructions = ET.SubElement(LXFML, "BuildingInstructions").text = " "

#Generates output file
#Prompts user to select .jpg image
root = Tk()
root.withdraw()
root.fileName = filedialog.asksaveasfile(title = "Select Save Location", defaultextension=".lxfml")
tree = ET.ElementTree(LXFML)
tree.write(root.fileName.name,encoding='UTF-8', xml_declaration=True)
