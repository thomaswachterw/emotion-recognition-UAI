#Script for changing the different parametrs of wuickshift, saving those images and then using them in for theining the model


import cv2
import matplotlib.pyplot as plt
import skimage
from skimage import color
from sklearn.cluster import MeanShift
from skimage.segmentation import slic
import os 




#Load OASIS dataset

os.chdir("")
pos_img = []

for i in range(len(os.listdir())):
    
    name = os.listdir()[i]
    
    try:
        #print(name)
        img = cv2.imread(os.listdir()[i])
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = cv2.resize(img, (224,224))

        pos_img.append(img)
    except:
        print("fallé: ", name)

os.chdir("")

neg_img = []

for i in range(len(os.listdir())):
    
    name = os.listdir()[i]
    
    try:
        #print(name)
        img = cv2.imread(os.listdir()[i])
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = cv2.resize(img, (224,224))

        neg_img.append(img)
    except:
        print("falle: ", name)
        

#STILES
############################RENASSAINCE####################################

dir_pos_ren = ""
dir_neg_ren = ""

os.chdir(dir_pos_ren)

pos_ren = []


for i in range(len(os.listdir(dir_pos_ren))):
    
    nombre= os.listdir(dir_pos_ren)[i]
    #print(nombre)
    try:
        
        img = cv2.imread(nombre)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = cv2.resize(img, (224,224))
        
        pos_ren.append(img)

        

    except:
        print("error")
        


os.chdir(dir_neg_ren)

neg_ren = []


for i in range(len(os.listdir(dir_neg_ren))):
    
    nombre= os.listdir(dir_neg_ren)[i]
    #print(nombre)
    try:
        
        img = cv2.imread(nombre)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = cv2.resize(img, (224,224))
        
        neg_ren.append(img)

    
    except:
        print("error")



#################################CONTEMPORARY###########################

dir_pos_con = ""
dir_neg_con = ""

os.chdir(dir_pos_con)

pos_con = []


for i in range(len(os.listdir(dir_pos_con))):
    
    nombre= os.listdir(dir_pos_con)[i]
    #print(nombre)
    try:
        
        img = cv2.imread(nombre)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = cv2.resize(img, (224,224))
        
        pos_con.append(img)

    except:
        print("error")
        


os.chdir(dir_neg_con)

neg_con = []


for i in range(len(os.listdir(dir_neg_con))):
    
    nombre= os.listdir(dir_neg_con)[i]
    #print(nombre)
    try:
        
        img = cv2.imread(nombre)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = cv2.resize(img, (224,224))
        
        neg_con.append(img)

    except:
        print("error")




    



############################MODERN#####################



dir_pos_modern = ""
dir_neg_modern = ""



os.chdir(dir_pos_modern)

pos_modern = []


for i in range(len(os.listdir(dir_pos_modern))):
    
    nombre= os.listdir(dir_pos_modern)[i]
    #print(nombre)
    try:
        
        img = cv2.imread(nombre)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = cv2.resize(img, (224,224))
        
        pos_modern.append(img)

        
        

    except:
        print("error")
        


os.chdir(dir_neg_modern)

neg_modern = []

for i in range(len(os.listdir(dir_neg_modern))):
    
    nombre= os.listdir(dir_neg_modern)[i]
    #print(nombre)
    try:
        
        img = cv2.imread(nombre)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = cv2.resize(img, (224,224))
        
        neg_modern.append(img)

        
    except:
        print("error")




############################POST-REN########################
dir_pos_postren = ""
dir_neg_postren = ""



os.chdir(dir_pos_postren)

pos_postren = []


for i in range(len(os.listdir(dir_pos_postren))):
    
    nombre= os.listdir(dir_pos_postren)[i]
    #print(nombre)
    try:
        
        img = cv2.imread(nombre)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = cv2.resize(img, (224,224))
        
        pos_postren.append(img)

        

    except:
        print("error")
        
os.chdir(dir_neg_postren)

neg_postren = []

for i in range(len(os.listdir(dir_neg_postren))):
    
    nombre= os.listdir(dir_neg_postren)[i]
    #print(nombre)
    try:
        
        img = cv2.imread(nombre)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = cv2.resize(img, (224,224))
        
        neg_postren.append(img)

        
    except:
        print("error")







################################################################################################################
#seg = skimage.segmentation.quickshift(X[0], ratio = 1.0, kernel_size=10, max_dist=2,sigma=0)
#parameters for changing the image 


max_dist = [12, 16,2,4,6,8,10,14,18,20]
categorias = ["pos", "neg"]
imagenes = [pos_img[:10], neg_img[:10], pos_ren[:10], neg_ren[:10], pos_con[:10], neg_con[:10], pos_modern[:10], neg_modern[:10], pos_postren[:10], neg_postren[:10]]
path = ["/Users/thomaswachter/Desktop/Tesis/new_data/oasis/pos", "/Users/thomaswachter/Desktop/Tesis/new_data/oasis/neg",
       "/Users/thomaswachter/Desktop/Tesis/new_data/renacimiento/pos", "/Users/thomaswachter/Desktop/Tesis/new_data/renacimiento/neg", 
       "/Users/thomaswachter/Desktop/Tesis/new_data/contemporaneo/pos", "/Users/thomaswachter/Desktop/Tesis/new_data/contemporaneo/neg",
       "/Users/thomaswachter/Desktop/Tesis/new_data/moderno/pos", "/Users/thomaswachter/Desktop/Tesis/new_data/moderno/neg", 
       "/Users/thomaswachter/Desktop/Tesis/new_data/postren/pos", "/Users/thomaswachter/Desktop/Tesis/new_data/postren/neg"]

imagenes_2 = ["OASIS Positive", "OASIS Negative", "pos_ren", "neg_ren", "pos_con", "neg_con", "pos_modern"," neg_modern", "pos_postren", "neg_postren" ]




x = 0


path_padres = ["oasis",
       "/renacimiento", 
       "/contemporaneo",
       "/moderno",  
       "/postren"]

for i in range(len(path_padres)):
    os.mkdir(path_padres[i])

for i in range(len(path)):
    
    os.mkdir(path[i])

def experimento(distancia, ruta, lista):
    
    os.chdir(ruta)
    print(ruta)
    
    for i in range(len(lista)):
        
       
        img = lista[i]
        nombre_original = "original"+str(i)+".jpg"
        img_2 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        cv2.imwrite(nombre_original, img_2)

        seg = skimage.segmentation.quickshift(img, ratio = 1.0, kernel_size=10, max_dist=distancia,sigma=0)
        out = color.label2rgb(seg, img, kind="avg", bg_label=0)
        out = cv2.resize(out, (224, 224), interpolation=cv2.INTER_AREA)
        out = cv2.cvtColor(out, cv2.COLOR_BGR2RGB)
        nombre = "shifted" + str(i) + ".jpg"
        cv2.imwrite(nombre, out)

for i in range(0,len(path)):
    
    print("*********************************")
    print(x,i,i)
    print(f"Distancia: {max_dist[x]}")
    print(f"Path:{path[i]}")
    print(f"Lista: {imagenes_2[i]}")
    
    experimento(max_dist[x], path[i], imagenes[i])
    
    
        




        






    
