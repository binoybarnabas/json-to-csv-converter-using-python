import json

dict = {
    'student1' : ['binoy',21,False]
}

print(dict['student1'][0]) # just checking
print(dict)


json_obj = json.dumps(dict,indent = 4)  # parsing into json object

print(json_obj)    #checking

file = open('converted.json','r+')     #creating the json file

file.write(json_obj)                    #writing into the json file(converted.json)