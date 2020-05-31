import smtplib as sl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import pymongo
def sendMail(indexPat):
    myclient = pymongo.MongoClient(
        "mongodb+srv://puneetjyot:handshake@handshake-mongo-zu6wh.mongodb.net/Handshake?retryWrites=true&w=majority")
    mydb = myclient["Handshake"]
    mycol = mydb["users"]
    server = sl.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('archit2195@gmail.com', pd)
    geoLocation = "190 Ryland Street. Location: https://goo.gl/maps/vJSCnrqbZniG9D2i6"
    for x in mycol.find({"patient_id": str(indexPat)}, {"name": 1, "emergencyContacts.email": 1, "emergencyContacts.name": 1, "emergencyContacts.relation": 1}):
        name = x['name']
        for mail in x['emergencyContacts']:
            emails = (mail['email'])
            print(emails)
            emerName = (mail['name'])
            relation = (mail['relation'])
            message = "Hi " + emerName + ",\n\n\n Please consider this email as an immediate emergency. We have detected that " + name + " is going to have a seizure in a few minutes or is already suffering from one. You are listed as an emergency contact to this person as a " + relation + ", hence we request you to please take immediate action to help him. We have intimated emergency services as well and request you to reach this location ASAP.\n\n Location - " + geoLocation + "\n\nRegards,\nSeizure Detection\nTeam 18"
            data = MIMEMultipart()
            data['Subject'] = "EMERGENCY! Seizure Detected for " + name
            data.attach(MIMEText(message, 'plain'))
            print("Sending mail.")
            server.sendmail('archit2195@gmail.com', emails, data.as_string())

pd = 'Fastrack_2195'
sendMail(1)