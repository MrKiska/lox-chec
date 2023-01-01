import importlib
import json
import os
from lib.voter import askForOptions

root = os.getcwd()


pkgListFile = open(root +"/Launcher/pkgList.json")
greeting = open(root + "/resources/greeting.txt").read()

packages = os.listdir("Packages")
print(packages)
pkgsInfo = []

for i in range(0,len(packages)):

    with open("Packages/"+packages[i]+"/info.json") as f:
        moduleInfo = list(json.load(f).items())
    pkgsInfo.append(moduleInfo)



while True:
    try:

        print(greeting)
        print( pkgsInfo)
        for i in range(0,len(pkgsInfo)):
            info = [
                str(i) + " - " + pkgsInfo[i][0][1], # name of package
                "  * " + pkgsInfo[i][1][1]
            ]
            print("\n".join(info))
        chosenPkg = input(":")

        if chosenPkg == "q":
            exit()

        if chosenPkg.isdigit():
            pkgIndex = int(chosenPkg)

        __import__(pkgsInfo[pkgIndex][3][1])
        # importlib.import_module(pkgPath)

    except KeyboardInterrupt:
        print("exit")