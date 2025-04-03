import csv
import re
from dataclasses import dataclass

@dataclass
class Computer():
    asset: str = ""
    name:  str = ""
    
    def getIterable(self):
        return [self.asset, self.name]
    
    def __str__(self):
        return self.asset + ": " + self.name

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
                spamwriter.writerow(row.getIterable())
    
    def summarize(self):
        summary = {}
        for computer in self:
            trolley = re.sub('\d', '', computer.name.strip().upper())
            #print(trolley, summary)
            if(trolley not in summary):
                #print("if(trolley not in self)")
                summary[trolley] = 0
            summary[trolley] += 1
        print ("Summary", summary)
        print("Target  {'OLP-CR-EN': 1, 'INCLUSION': 8, 'HEALTH': 20, 'OLP-CR-CON': 8, 'SPORT': 26, 'OLP-CR-SP': 26}")
        print("Total",len(self))
    
    def getComputer(self, text):
        for computer in self:
            if computer.asset.strip().upper() == text.strip().upper():
                return computer
            
        for computer in self:
            if computer.name.strip().upper() == text.strip().upper():
                return computer
            
        return False
    
    def add(self, asset, name):
        self.append(Computer(asset.strip().upper() , name.strip().upper()))
        return self.getComputer(asset)  


computers = Computers.load()
computers.summarize()

while True:
    asset = input("Scan Asset Tag : ")
    computer = computers.getComputer(asset)
    if computer:
        print(computer)
    else :
        print("Not Found")
        name = input("Scan Name Tag : ")
        if(name and name.strip().upper() != "ERROR"):
            newComputer = computers.add(asset , name)
            print("Saving ", newComputer) 
            computers.save()
        else :
            print("Nothing to save.")
