import sys 
import os
from PIL import Image

# grab first and second argument
image_folder = sys.argv[1]
new_folder = sys.argv[2]

# check if new exists, if not, create it
if not os.path.exists(new_folder):
    os.makedirs(new_folder)

# loop through pokedexi, convert images to png
for filename in os.listdir(image_folder):
    img = Image.open(f'{image_folder}{filename}')
    clean_name = os.path.splitext(filename)[0]
    print(clean_name)
    img.save(f'{new_folder}{clean_name}.png', 'png')
    print('all done!')

