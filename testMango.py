import pymongo

myclient = pymongo.MongoClient(
    "mongodb+srv://puneetjyot:handshake@handshake-mongo-zu6wh.mongodb.net/Handshake?retryWrites=true&w=majority")
mydb = myclient["Handshake"]
mycol = mydb["users"]
emails = []
for x in mycol.find({"patient_id": "1"}, {"emergencyContacts.email" : 1}):
    for mail in x['emergencyContacts']:
        emails.append(mail['email'])
print(emails)