import sys
from pymongo import MongoClient

print('Connectando com banco de dados Local!')
local = MongoClient()
dbLocal = local['db-poupinha']
collectionLocal = dbLocal['historico_conversation']


print('Connectando com banco de dados nas Nuvens!')
nuvens = MongoClient('mongodb://admin:EWKBQVEIDCVQHUNZ@portal-ssl1498-6.bmix-dal-yp-16a223c0-40c3-409f-862f-c197f6f7ffb9.1008755356.composedb.com:54954,portal-ssl1105-31.bmix-dal-yp-16a223c0-40c3-409f-862f-c197f6f7ffb9.1008755356.composedb.com:54954/compose?authSource=admin&ssl=true')
dbNuvem = nuvens['db-poupinha']

print('Identificando a quantidade de docs a ser importados!')
docs = dbNuvem['historico_conversation'].count()

# Função de paginação ou search por demanda
def skiplimit(page_size, page_num):
        skips = page_size * page_num
        cursor = dbNuvem['historico_conversation'].find().skip(skips).limit(page_size)

        return [x for x in cursor]

# Função de identificar progresso dp trabalho
def progress_bar(value, max, barsize):
    chars = int(value * barsize / float(max))
    percent = int((value / float(max)) * 100)
    sys.stdout.write("#" * chars)
    sys.stdout.write(" " * (barsize - chars + 2))
    if value >= max:
        sys.stdout.write("fim. \n")
    else:
        sys.stdout.write("[%3i%%] \r" % (percent))
        sys.stdout.flush()

print('Iniciando a importação de %s docs!', docs)
row_for_page = 100
total_pages = (docs // row_for_page)

count_docs = 0
for page in range(total_pages):
        collection = skiplimit(row_for_page, page)
        for doc in collection:
                progress_bar((count_docs), docs, 40)

                searchLocal = collectionLocal.count_documents(doc)
                if(searchLocal == 0):
                        collectionLocal.insert_one(doc)

                count_docs = (count_docs + 1)

print('Fim da importação!')