from PIL import Image
import sys, os

dir = sys.argv[1]
left = int(sys.argv[2])
top = int(sys.argv[3])
right = int(sys.argv[4])
bottom = int(sys.argv[5])

def crop_and_save(input_image_path, output_image_path, left, top, right, bottom):
    # Apri l'immagine
    image = Image.open(input_image_path)
    
    # Ritaglia l'area specificata
    cropped_image = image.crop((left, top, right, bottom))
    
    # Salva l'immagine ritagliata come file JPG
    cropped_image.save(output_image_path, "JPEG")

# Specifica il percorso dell'immagine di input, l'area da ritagliare e il percorso dell'immagine di output
input_image_path = dir

# elenco file da analizzare
files_in_dir = os.listdir(dir)
frames_files = sorted([file for file in files_in_dir if file.startswith("frame")])
for file in frames_files:
    image_path = f"{dir}/{file}"
    output_path = f"{dir}/crop_{file}"
    crop_and_save(image_path, output_path, left, top, right, bottom)
