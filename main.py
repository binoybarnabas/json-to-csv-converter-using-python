import json
import csv

dict = {
    'student1' : ['binoy',21,False]
}

print(dict['student1'][0]) # just checking
print(dict)


json_obj = json.dumps(dict,indent = 4)      # parsing into json object

print(json_obj)    #checking

json_file = open('converted.json','r+')       #creating the json file

json_file.write(json_obj)                     #writing into the json file(converted.json)

json_file.close()

with open('converted.json') as json_file:     # Opening JSON file and loading the data into the variable
    data = json.load(json_file)

student_data = data['student1']

# print(student_data)

data_file = open('converted.csv', 'r+')  # now we will open a file for writing
csv_writer = csv.writer(data_file)      # create the csv writer object

count = 0     # Counter variable used for writing headers to the CSV file
 
for student in student_data:
    if count == 0:
 
        # Writing headers of CSV file
        header = student.keys()
        csv_writer.writerow(header)
        count += 1
 
    # Writing data of CSV file
    csv_writer.writerow(student.values())
 
data_file.close()

