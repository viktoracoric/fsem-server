import os.path
import sys
import csv
import subprocess

if os.path.exists("podaci.csv") == 0:
    f = open("podaci.csv", "x")
    f.close()

def provjeraDuplikata():
    f = open("podaci.csv", "r+")
    citaj = csv.reader(f, delimiter=',')
    for redak in citaj:
        if redak[0] == sys.argv[2]:
            komanda = "sed -i -e 's/" + redak[1] + "/" + sys.argv[3] + "/' podaci.csv"
            subprocess.call([komanda], shell=True)
            return 1

def zapis():
    f = open("podaci.csv", "a")
    string = sys.argv[2] + "," +  sys.argv[3] + "\n"
    f.write(string)
    f.close()

def pretraga():
    f = open("podaci.csv", "r")
    citaj = csv.reader(f, delimiter=',')
    for redak in citaj:
        if redak[0] == sys.argv[2]:
            return redak[1]

if sys.argv[1] == 'PUBLISH':
    if provjeraDuplikata():
        sys.exit(1)
    sys.exit(zapis())

if sys.argv[1] == 'GET':
    print(pretraga())
