####################
# This script takes in all the images in 'task_img' and outputs a .json file.
# The output will contain (1) the filename (./task_img/filename.png), (2) the category
# that the image belongs to, and (3) the manipulation applied.
#
# With masking: the script will also add the name of the mask
# to be applied for each image.
#
# This script does the same with images in 'train_img'.
####################
import pathlib
import glob
import pandas as pd
import csv
import json 

def csv_to_json(csvFilePath, jsonFilePath):
    jsonArray = []
      
    #read csv file
    with open(csvFilePath, encoding='utf-8') as csvf: 
        #load csv file data using csv library's dictionary reader
        csvReader = csv.DictReader(csvf) 

        #convert each csv row into python dict
        for row in csvReader: 
            #add this python dict to json array
            jsonArray.append(row)
  
    #convert python jsonArray to JSON String and write to file
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf: 
        jsonString = json.dumps(jsonArray, indent=4)
        jsonf.write(jsonString)

files = glob.glob('./online_version_mask/task_img/*.png')
mask_files = glob.glob('./online_version_mask/mask_img/*.png')

filenames = []
mask_filenames = []
category = []
manipulation = []


# train_img/lightcluttermatched_person1905.png
# https://www.psytests.be/timages/instructions_img/control_person1.png

for i in range(len(files)):
    # adding the name of the file to the list
    file = pathlib.Path(files[i])
    filenames.append("https://www.psytests.be/timages/" + str(file.parts[-2]) + '/' + file.name)
    # adding the name of the mask file to the list
    mask_file = pathlib.Path(mask_files[i])
    mask_filenames.append("https://www.psytests.be/timages/" + str(mask_file.parts[-2]) + '/' + mask_file.name)

    # adding the category and correct response
    if 'person' in str(file.name):
        category.append('person')
        # correct_response.append('l')
    elif 'cat' in str(file.name):
        category.append('cat')
        # correct_response.append('j')
    elif 'bird' in str(file.name):
        category.append('bird')
        # correct_response.append('d')
    elif 'banana' in str(file.name):
        category.append('banana')
        # correct_response.append('q')
    elif 'firehydrant' in str(file.name):
        category.append('firehydrant')
        # correct_response.append('s')
    elif 'bus' in str(file.name):
        category.append('bus')
        # correct_response.append('k')
    elif 'building' in str(file.name):
        category.append('building')
        # correct_response.append('f')
    elif 'tree' in str(file.name):
        category.append('tree')
        # correct_response.append('m')
    
    # adding the manipulation
    if 'blob' in str(file.name):
        manipulation.append('occlusion')
    elif 'control' in str(file.name):
        manipulation.append('control')
    elif 'clutter' in str(file.name):
        manipulation.append('clutter')
    elif 'lp' in str(file.name):
        manipulation.append('low-pass')
    elif 'hp' in str(file.name):
        manipulation.append('high-pass')

# csvFilePath = r'data.csv'
# jsonFilePath = r'data.json'
# csv_to_json(csvFilePath, jsonFilePath)

# creating a dictionary that includes all the lists
# dict = {"filename": filename,"category": category, "manipulation": manipulation, "correct_response": correct_response}
dict = {"filename": filenames, "mask_filename": mask_filenames, "category": category, "manipulation": manipulation}
# transforming it to a dataframe
df = pd.DataFrame(dict)
df.to_csv('./online_version_mask/img_stimuli.csv')
csv_to_json('./online_version_mask/img_stimuli.csv', './online_version_mask/img_stimuli.js')

####################################
# Once the img_stimuli.js file is created, remember to add 'var img_stimuli = ' on the first line, so JsPsych can read it.
####################################


train_files = glob.glob('./online_version_mask/train_img/*.png')
train_mask_files = glob.glob('./online_version_mask/train_mask_img/*.png')

train_filenames = []
train_mask_filenames = []
train_category = []
train_manipulation = []

for i in range(len(train_files)):
    # adding the name of the file to the list
    train_file = pathlib.Path(train_files[i])
    train_filenames.append("https://www.psytests.be/timages/" + str(train_file.parts[-2]) + '/' + train_file.name)
    # adding the name of the mask file to the list
    train_mask_file = pathlib.Path(train_mask_files[i])
    train_mask_filenames.append("https://www.psytests.be/timages/" + str(train_mask_file.parts[-2]) + '/' + train_mask_file.name)

    # adding the category and correct response
    if 'person' in str(train_file.name):
        train_category.append('person')
        # correct_response.append('l')
    elif 'cat' in str(train_file.name):
        train_category.append('cat')
        # correct_response.append('j')
    elif 'bird' in str(train_file.name):
        train_category.append('bird')
        # correct_response.append('d')
    elif 'banana' in str(train_file.name):
        train_category.append('banana')
        # correct_response.append('q')
    elif 'firehydrant' in str(train_file.name):
        train_category.append('firehydrant')
        # correct_response.append('s')
    elif 'bus' in str(train_file.name):
        train_category.append('bus')
        # correct_response.append('k')
    elif 'building' in str(train_file.name):
        train_category.append('building')
        # correct_response.append('f')
    elif 'tree' in str(train_file.name):
        train_category.append('tree')
        # correct_response.append('m')
    
    # adding the manipulation
    if 'blob' in str(train_file.name):
        train_manipulation.append('occlusion')
    elif 'control' in str(train_file.name):
        train_manipulation.append('control')
    elif 'clutter' in str(train_file.name):
        train_manipulation.append('clutter')
    elif 'lp' in str(train_file.name):
        train_manipulation.append('low-pass')
    elif 'hp' in str(train_file.name):
        train_manipulation.append('high-pass')

# csvFilePath = r'data.csv'
# jsonFilePath = r'data.json'
# csv_to_json(csvFilePath, jsonFilePath)

# creating a dictionary that includes all the lists
# dict = {"filename": filename,"category": category, "manipulation": manipulation, "correct_response": correct_response}
train_dict = {"train_filename": train_filenames,"train_mask_filename": train_mask_filenames, "train_category": train_category, "train_manipulation": train_manipulation}
# transforming it to a dataframe
train_df = pd.DataFrame(train_dict)
train_df.to_csv('./online_version_mask/train_img_stimuli.csv')
csv_to_json('./online_version_mask/train_img_stimuli.csv', './online_version_mask/train_img_stimuli.js')


####################################
# Once the train_img_stimuli.js file is created, remember to add 'var train_img_stimuli = ' on the first line, so JsPsych can read it.
####################################
