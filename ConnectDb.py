import os

import TestThreshold
import DataserToSpectogram
import CNN
from pymongo import MongoClient

from CNN import patients
from DataserToSpectogram import pathDataSet

def insertData(data):
    client = MongoClient("mongodb+srv://puneetjyot:handshake@handshake-mongo-zu6wh.mongodb.net/Handshake?retryWrites=true"
                         "&w=majority")
    db = client.Handshake
    result = db.seizure.insert_one(data)


pathDataSet = ''
def loadParametersFromFile(filePath):
    global pathDataSet
    global FirstPartPathOutput
    if(os.path.isfile(filePath)):
        with open(filePath, "r") as f:
                line=f.readline()
                if(line.split(":")[0]=="pathDataSet"):
                    pathDataSet=line.split(":")[1].strip()


loadParametersFromFile("PARAMETERS_DATA_EDITING.txt")

#DataserToSpectogram.main()
CNN.main()
#TestThreshold.main()

for indexPat in range(0, len(patients)):
    datax = {}
    f = open(pathDataSet + 'chb' + patients[indexPat] + '/chb' + patients[indexPat] + '-summary.txt', 'r')
    lines = f.readlines()
    datax['patientId'] = indexPat
    dat = {}
    sth = []
    for index, line in enumerate(lines):
        if 'Number of Seizures in File: 1' in line:
            dat['startTime'] = lines[index+1].split(':')[1].split(' ')[1]
            dat['endTime'] = lines[index+2].split(':')[1].split(' ')[1]
            sth.append(dat.copy())
    datax['time'] = sth
    # insertData(datax)


