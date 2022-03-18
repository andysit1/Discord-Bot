import os
import shutil
import os

image_types = ["png", "jpeg", "gif", "jpg"]
dir = "E:/Projects/Discord Bot/"
dest_dir = 'C:/Users/andys/Desktop/Directory Lord/Bad'

def move_images(image_types):
    saved_files = []
    for filename in os.listdir(dir):
        for image in image_types:
            if filename.lower().endswith(image):
                word = dir+filename
                saved_files.append(word)
    
    for cur_dir in saved_files:
        shutil.move(cur_dir, dest_dir)
   