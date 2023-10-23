import csv
from dataclasses import dataclass

@dataclass
class Computer():
    asset: str = ""
    name:  str = ""

class Computers(list):
    
    def load(filename = "computers.csv"):
        newList = Computers() 
        with open(filename, newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                newList.append(Computer(row[0], row[1]))
            return newList
           
    def save(self, filename = "computers.csv"): 
        with open(filename, 'w', newline='') as csvfile:
            spamwriter = csv.writer(csvfile)
            for row in self:
                spamwriter.writerow(row)
    
    
    def getComputer(self, text):
        for computer in self:
            if trim(computer.asset).lower() == trim(text).lower():
                return computer
            
        for computer in self:
            if trim(computer.name).lower() == trim(text).lower():
                return computer
            
            return False
    
    def add(self, asset, name):
        self.append(Computer(asset , name))     


computers = Computers()

while True:
    asset = input("Scan Asset Tag : ")
    computer = computers.getComputer(asset)
    if computer:
        print(computer)
    else :
        print("Not Found")
        name = input("Scan Name Tag : ")
        if(name):
            print("Saving ", asset , name) 
            computers.add(asset , name)
            computers.save()
        else :
            print("Nothing to save.")
