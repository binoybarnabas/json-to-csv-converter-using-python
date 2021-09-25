import json
import csv
import pandas as pd

dict = {
    'student1' : ['binoy',21,False],
    'student2' : ['abc',22,True]
}

print(dict['student1'][0]) # just checking
print(dict)


json_obj = json.dumps(dict,indent = 4)      # parsing into json object

print(json_obj)    #checking

json_file = open('converted.json','r+')       #creating the json file

json_file.write(json_obj)                     #writing into the json file(converted.json)

json_file.close()

#using panda library for json to csv conversion

data_file = pd.read_json(r'converted.json')
data_file.to_csv(r'converted.csv',index = None)