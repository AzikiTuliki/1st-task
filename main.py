import self as self
from datetime import datetime
from elasticsearch import Elasticsearch
import pprint

et = Elasticsearch("http://192.168.56.101:9200")

if et.indices.exists(index="security_events_1_19127"):
    print("True")
else:
    print("False")

query_body = {
    "query": {
            "bool": {
                "should": [
                    {"match": { "what.text": "Successful Logon"}},
                ]
            }
    }
}

result = et.search(index="security_events_1_19127", body=query_body, size=3)
pprint(result)