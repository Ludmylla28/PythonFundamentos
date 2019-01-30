import urllib
proxy = {"http" : "http://10.1.6.120:80"}
site = urllib(proxy)
site.read()

from pymongo import MongoClient
client = MongoClient('mongodb://admin:EWKBQVEIDCVQHUNZ@portal-ssl1498-6.bmix-dal-yp-16a223c0-40c3-409f-862f-c197f6f7ffb9'
                     '.1008755356.composedb.com:54954,portal-ssl1105-31.bmix-dal-yp-16a223c0-40c3-409f-862f-c197f6f7ffb9'
                     '.1008755356.composedb.com:54954/compose?authSource=admin&ssl=true')
db = client['db-poupinha']
docs = db['historico_conversation'].count()

def skiplimit(page_size, page_num):
    skips = page_size * page_num
    cursor = db['historico_conversation'].find().skip(skips).limit(page_size)

    return [x for x in cursor]

row_for_page = 10
total_pages = (docs // row_for_page)

for page in range(total_pages):
    collection = skiplimit(row_for_page, page)
    for doc in collection:
        print(doc)
