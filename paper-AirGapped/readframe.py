from PIL import Image
import os, sys

dir = sys.argv[1]

# led1
def calcola_luminosita_media(image, x, y, width, height):
    area = image.crop((x, y, x + width, y + height))
    grayscale_area = area.convert("L")  # Converti l'area in scala di grigi
    luminosita_media = sum(grayscale_area.getdata()) / (width * height)
    return luminosita_media

# elenco file da analizzare
files_in_dir = os.listdir(dir)
crop_files = sorted([file for file in files_in_dir if file.startswith("crop")])
for file in crop_files:

    image_path = "{}/{}".format(dir, file)
    image = Image.open(image_path)

    x_area1 = 0  # Coordinata x dell'angolo superiore sinistro dell'area 1
    y_area1 = 100  # Coordinata y dell'angolo superiore sinistro dell'area 1
    width_area1 = 75  # Larghezza dell'area 1
    height_area1 = 50  # Altezza dell'area 1
    luminosita_media_area1 = calcola_luminosita_media(image, x_area1, y_area1, width_area1, height_area1)

    x_area2 = 100 
    y_area2 = 100  
    width_area2 = 75  
    height_area2 = 50 
    luminosita_media_area2 = calcola_luminosita_media(image, x_area2, y_area2, width_area2, height_area2)

    x_area3 = 240 
    y_area3 = 100  
    width_area3 = 75  
    height_area3 = 50 
    luminosita_media_area3 = calcola_luminosita_media(image, x_area3, y_area3, width_area3, height_area3)
    
    print("File {}: {}\t{}\t{}".format(file, int(luminosita_media_area1), int(luminosita_media_area2), int(luminosita_media_area3)))


'''
# Definisci il percorso dell'immagine e le coordinate delle due aree
image_path = "percorso/all/immagine.jpg"
x_area1 = 100  # Coordinata x dell'angolo superiore sinistro dell'area 1
y_area1 = 150  # Coordinata y dell'angolo superiore sinistro dell'area 1
width_area1 = 50  # Larghezza dell'area 1
height_area1 = 50  # Altezza dell'area 1

x_area2 = 200  # Coordinata x dell'angolo superiore sinistro dell'area 2
y_area2 = 150  # Coordinata y dell'angolo superiore sinistro dell'area 2
width_area2 = 50  # Larghezza dell'area 2
height_area2 = 50  # Altezza dell'area 2

# Apri l'immagine
image = Image.open(image_path)

# Calcola la luminosità media delle due aree
luminosita_media_area1 = calcola_luminosita_media(image, x_area1, y_area1, width_area1, height_area1)
luminosita_media_area2 = calcola_luminosita_media(image, x_area2, y_area2, width_area2, height_area2)

# Confronta le luminosità medie delle due aree
if luminosita_media_area1 > luminosita_media_area2:
    print("L'area 1 è più chiara dell'area 2.")
elif luminosita_media_area1 < luminosita_media_area2:
    print("L'area 1 è più scura dell'area 2.")
else:
    print("Le due aree hanno la stessa luminosità media.")
'''