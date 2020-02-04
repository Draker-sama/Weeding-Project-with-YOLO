import numpy as np
import json as js
import os


fichier = open("Annotation.vott", "r")

lines=fichier.readlines()

fichier.close()

Listeimage=[]
Listeid=[]
identifiant=""
image=""
str=""
for line in lines:
	tuple=('','')
	str=line.strip()
	if '"id"' in str and len(str)==41:
		identifiant=str[7:39]
	if '"name"' in str and 'jpg' in str:
		image=str[9:14]
		Listeid.append(identifiant)
		Listeimage.append(image)

for element in os.listdir('./'):
	if element.endswith('.json'):
		with open(element,"r") as f:
			data=js.load(f)

		assert type(data) is dict
		path=data["asset"]['path']
		n=len(path)
		imagejson=path[n-9:n-4]
		data["asset"]['path']="file:/home/draker/TrainYourOwnYOLO/VOTT/Images_non_modif/"+imagejson+".jpg"
		index=Listeimage.index(imagejson)
		data["asset"]['id']=Listeid[index]
		
		with open('./'+data["asset"]['id']+'-asset.json',"w") as f:
			js.dump(data,f, sort_keys=True, indent=4, ensure_ascii=False)

		os.remove(element)







