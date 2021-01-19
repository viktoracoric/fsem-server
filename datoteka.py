import os.path
import sys
import csv

if os.path.exists("podaci.csv") == 0:
    f = open("podaci.csv", "x")
    f.close()

def zapis():

    f = open("podaci.csv", "a")

    string = sys.argv[2] + "," +  sys.argv[3] + "\n"
    f.write(string)
    f.close()

def pretraga():
    f = open("podaci.csv", "r")
    citaj = csv.reader(f, delimiter=',')
    for redak in citaj:
        return redak[1]

if sys.argv[1] == 'PUBLISH':
    sys.exit(zapis())

if sys.argv[1] == 'GET':
    print(pretraga())
