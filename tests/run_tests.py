import os

curDir = os.path.dirname(os.path.realpath(__file__))
os.mkdir(curDir+"/logs")

f = open(f"{curDir+'/logs/'}myfile.txt", "w")
print("Hello world")

sdfk