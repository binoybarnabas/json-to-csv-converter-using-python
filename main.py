import json
import csv
import pandas 
from copy import deepcopy

dict = {

"items":[
        {
            "crawl_count": 0,
            "crawl_start_time": "09/02/2021 15:15:07",
            "attempt_count": 0,
            "tenant_name": "Tenant Admin",
            "draft_status": "published",
            "scraped_count": 0,
            "download_delay": "0.217",
            "hier": "f747323e-9a5b-49dc-a6e9-a0a4e6c5f513",
            "website_name": "TestSite101",
            "S3_url": "s3://inscrape-bucket-develop/tenantAdmin/testsite101-bf65e2a3-7f44-4c5e-9df1-b771e522bf81",
            "is_stop_site": False,
            "spider_status": "Scraping Completed",
            "crawl_end_time": "09/02/2021 15:15:50",
            "is_error": True,
            "is_refused": True,
            "website_url": "www.testsite.com",
            "project_id": "1b7b9205-efbe-4cb4-bb4a-fb398095ed19",
            "upload_type": "instant_upload",
            "id": "bf65e2a3-7f44-4c5e-9df1-b771e522bf81",
            "node_count": 0,
            "site_id": 61,
            "type": "url",
            "project_name": "News",
            "scraping_time": "0:00:43",
            "uploader_time": ""
        },
        {
            "crawl_count": 0,
            "crawl_start_time": "09/24/2021 19:39:18",
            "attempt_count": 469,
            "tenant_name": "Tenant Admin",
            "draft_status": "published",
            "scraped_count": 469,
            "download_delay": "0.25",
            "hier": "f747323e-9a5b-49dc-a6e9-a0a4e6c5f513",
            "website_name": "BCBS_TN",
            "S3_url": "s3://inscrape-bucket-develop/tenantAdmin/bcbsTn-d12f0b53-66d4-4037-b9d7-6aa9ed7c2432",
            "is_stop_site": False,
            "spider_status": "Stopped",
            "crawl_end_time": "09/24/2021 19:39:18",
            "is_error": False,
            "is_refused": False,
            "website_url": "https://www.bcbst.com/mpmanual/!SSL!/WebHelp/Welcome.htm",
            "upload_type": "instant_upload",
            "project_id": "1e989559-c5ba-4d9d-8e0e-7d967f78d17d",
            "id": "d12f0b53-66d4-4037-b9d7-6aa9ed7c2432",
            "node_count": None,
            "site_id": 4,
            "type": "url",
            "project_name": "Demo",
            "scraping_time": "0:00:00",
            "uploader_time": ""
        },
        {
            "crawl_count": 406,
            "attempt_count": 470,
            "crawl_start_time": "09/02/2021 19:12:25",
            "tenant_name": "Tenant Admin",
            "draft_status": "published",
            "scraped_count": 470,
            "download_delay": "0.25",
            "hier": "f747323e-9a5b-49dc-a6e9-a0a4e6c5f513",
            "website_name": "Amerigroup",
            "S3_url": "s3://inscrape-bucket-develop/tenantAdmin/amerigroup-09cecaf9-102d-4d87-8615-086c4ce30f92",
            "is_stop_site": False,
            "spider_status": "Scraping Completed",
            "crawl_end_time": "09/02/2021 19:46:29",
            "is_error": True,
            "is_refused": False,
            "website_url": "https://medpol.providers.amerigroup.com/green-provider/medical-policies-and-clinical-guidelines-full-list",
            "upload_type": "instant_upload",
            "project_id": "1e989559-c5ba-4d9d-8e0e-7d967f78d17d",
            "id": "09cecaf9-102d-4d87-8615-086c4ce30f92",
            "node_count": 1,
            "site_id": 31,
            "type": "url",
            "project_name": "Demo",
            "scraping_time": "0:34:04",
            "uploader_time": ""
        }

    ],
    "msg":"hai",
    "count":3,
    "endpage": False

}




json_obj = json.dumps(dict,indent = 4)        #parsing into json object

# print(json_obj)                             #checking

json_file = open('converted.json','r+')       #opening and creating the json file

json_file.write(json_obj)                     #writing into the json file(converted.json)

json_file.close()



def cross_join(left, right):
    new_rows = [] if right else left
    for left_row in left:
        for right_row in right:
            temp_row = deepcopy(left_row)
            for key, value in right_row.items():
                temp_row[key] = value
            new_rows.append(deepcopy(temp_row))
    return new_rows



def flatten_list(data):
    for elem in data:
        if isinstance(elem, list):
            yield from flatten_list(elem)
        else:
            yield elem



def json_to_dataframe(data_in):
    def flatten_json(data, prev_heading=''):
        if isinstance(data, dict):
            rows = [{}]
            for key, value in data.items():
                rows = cross_join(rows, flatten_json(value, prev_heading + '.' + key))
        elif isinstance(data, list):
            rows = []
            for i in range(len(data)):
                [rows.append(elem) for elem in flatten_list(flatten_json(data[i], prev_heading))]
        else:
            rows = [{prev_heading[1:]: data}]
        return rows

    return pandas.DataFrame(flatten_json(data_in))



if __name__ == '__main__':

    #using panda library for json to csv conversion

    data_file_jsonObj = open('converted.json','r+')
    data_files = json.load(data_file_jsonObj)

    csv_data = json_to_dataframe(data_files)

    csv_file = open("converted.csv","r+")

    csv_file.write(csv_data)


