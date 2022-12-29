from distutils.command.clean import clean
import os
import shutil



image_types = ["png", "jpeg", "gif", "jpg"]
dir = "E:/Projects/CURRENT_PROJECTS/Discord Bot/"
dest_dir = 'C:/Users/andys/Desktop/School Photo Dock'

cur_files = os.listdir(dir)
dest_files = os.listdir(dest_dir)

def move_images(image_types):
    saved_files = []

    for filename in os.listdir(dir):
        for image in image_types:
            if filename.lower().endswith(image):
                word = dir+filename
                saved_files.append(word)
    clean_copy()

    for cur_dir in saved_files:
        shutil.move(cur_dir, dest_dir)

import openai

openai.api_key = "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"

def openAiReponse(prompt):
  response = openai.Completion.create(
    engine = "text-davinci-003",
    prompt=prompt,
    temperature=0.4,
    max_tokens=64
  )
  return response.choices[0].text


def clean_copy():
    for d_files in dest_files:
        for c_files in cur_files:
            if d_files == c_files:
                print(c_files)
                os.remove(dir+c_files)
clean_copy()