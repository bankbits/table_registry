import urllib2
import json
import pprint
import sys

collection = "bfapplogs-prod-all"
host       = "http://bflsolr.innovate.ibm.com"

query = sys.argv[1]

connection = urllib2.urlopen(query)
response = json.load(connection)


# print (response['response']['numFound'], "documents found.")

doc_first = response['response']['docs'][0]

columns = list(doc_first.keys())
#print(columns)

def columnSchema(cols):
    col = []
    for c in columns:
        col.append({"title": c, "adjust": "left", "hint": "proportional"})
    return col

col_json = columnSchema(columns)
#print(col_json)

'''
for document in response['response']['docs']:
  print (document)'''

collection = "test"

gen_table = {
   
    "ID": collection,
    "Name": collection,
    "Description": "Logs",
    "Columns": {
         "columns": col_json
    },
    "RequiredRoles":None,
    "Sources": {
        "sources":[{
            "type": "SOLR",
            "lowTime": 34565,
            "highTime": 26786875,
            "host": host,
            "port": "",
            "database": collection
        }]
    },
    "Filters": {
        "filters":[{
            "id": "",
            "name": "",
            "description": "",
            "parameters": {},
            "queries": {
                "solr": "*:*"
            }
        }]
    },
    "Parameters": {
        "test1":"testtest1"
    },
    "Metadata": {}
}   

# "bluefringe CRUDReportRegistry createReportRegistry --data \'" + 

final_cmd = json.dumps(gen_table)
print(json.dumps(gen_table))
#print(json.dumps(gen_table))

with open(collection + '.json', 'w') as outfile:
    json.dump(gen_table, outfile)
