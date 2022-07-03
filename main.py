import pymongo
import pandas as pd

macb = pd.read_csv('MACBs.csv', encoding='ISO-8859-1')
macb.head()
macb.to_json('MACBs.json')
macbs = open('MACBs.json')
macbs.read()
data = macb.to_dict(orient='records')


tf = pd.read_csv('TFs.csv', encoding='ISO-8859-1')
tf.to_json('TFs.json')
tfs = open('TFs.json')
tfs.read()
data1 = tf.to_dict(orient='records')

af = pd.read_csv('ASFRs.csv', encoding='ISO-8859-1')
af.to_json('ASFRs.json')
afs = open('ASFRs.json')
afs.read()
data2 = tf.to_dict(orient='records')

client = pymongo.MongoClient()

my_db = client['CEN']

my_col = my_db['MACBs']
my_col1 = my_db['TFs']
my_col2 = my_db['ASFRs']

# my_col.insert_many(data)
# my_col1.insert_many(data1)
# my_col2.insert_many(data2)


try:
    print(my_db.list_collection_names())
    for x in my_col2.find({'Location':'Angola'}):
        print(x)
except Exception:
    print("Unable to connect to the server.")
