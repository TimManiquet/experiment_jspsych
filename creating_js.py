####################
# This script takes in all the images in 'my_img' and outputs a .json file
# that contains 1. the file name (./my_img/filename.png), 2. the category
# the image belongs to, and 3. the manipulation applied.
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

files = glob.glob('./my_img/*.png')

filename = []
category = []
manipulation = []
# correct_response = []

for i in range(len(files)):
    # adding the name of the file to the list
    file = pathlib.Path(files[i])
    filename.append(str(file.parents[0]) + '/' + file.name)

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
dict = {"filename": filename,"category": category, "manipulation": manipulation}
# transforming it to a dataframe
df = pd.DataFrame(dict)
df.to_csv('img_stimuli.csv')
csv_to_json('img_stimuli.csv', 'img_stimuli.js')

####################################
# Once the im_stimuli.js file is created, remember to add 'var im_stimuli = ' on the first line, so JsPsych can read it.
####################################